#!/usr/bin/env python

"""measures.py: Calculations for the Time, Number of Clicks and Number of Errors."""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "ACADEMIC & COMMERCIAL"
__version__     = "1.0.1"
__status__      = "Production"
__copyright__   = "Copyright 2017, Instituto Superior Técnico (IST)"
__credits__     = [
  "Carlos Santiago",
  "Jacinto C. Nascimento",
  "Pedro Miraldo",
  "Nuno Nunes"
]

import sys, os.path

pathDirname = os.path.dirname(__file__)
joinPath = os.path.join(pathDirname, '..', '..', '..')
pathAbsPath = os.path.abspath(joinPath)

sa_techniques_dir = os.path.join(pathAbsPath, 'statistical-analysis', 'src', 'techniques')
sa_constants_dir = os.path.join(pathAbsPath, 'statistical-analysis', 'src', 'constants')
sa_methods_dir = os.path.join(pathAbsPath, 'statistical-analysis', 'src', 'methods')
src_dir = os.path.join(pathAbsPath, 'sheet-reader', 'src', 'core')
constants_dir = os.path.join(pathAbsPath, 'sheet-reader', 'src', 'constants')
techniques_dir = os.path.join(pathAbsPath, 'sheet-reader', 'src', 'techniques')

sys.path.append(sa_techniques_dir)
sys.path.append(sa_constants_dir)
sys.path.append(sa_methods_dir)
sys.path.append(src_dir)
sys.path.append(constants_dir)
sys.path.append(techniques_dir)

from nasa import *
from sheets import *
from special import *
from structures import *
from iterators import *
from ploters import *

import main_variables
import sheetReaders

MV_N = main_variables.N
sm_num_img_94662 = special.sm_num_img_94662
sm_num_img_607376 = special.sm_num_img_607376
sm_num_img_737037 = special.sm_num_img_737037
mm_num_img_94662 = special.mm_num_img_94662
mm_num_img_607376 = special.mm_num_img_607376
mm_num_img_737037 = special.mm_num_img_737037
sm_birads_labels = structures.sm_birads_labels
mm_birads_labels = structures.mm_birads_labels
filterByColumn = structures.filterByColumn
figSizeX = structures.figSizeX
figSizeY = structures.figSizeY

main_sheet_dir = os.path.join(pathAbsPath, 'sheet-reader', 'data', 'temp', 'main_sheet.csv')
fs_sheet_dir = os.path.join(pathAbsPath, 'sheet-reader', 'data', 'temp', 'fs_sheet.csv')
fm_sheet_dir = os.path.join(pathAbsPath, 'sheet-reader', 'data', 'temp', 'fm_sheet.csv')

sys.path.append(main_sheet_dir)
sys.path.append(fs_sheet_dir)
sys.path.append(fm_sheet_dir)

import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly import figure_factory as FF

import pandas as pd
import scipy
from scipy import stats

import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})

import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np

datafile_fs = sheets.datafile_fs
datafile_fm = sheets.datafile_fm

# ============================================== #
#                                                #
#                  DEFINITIONS                   #
#                                                #
# ============================================== #

# Normalization of the data per image.

def dataImageNorm(dfList, numberOfImages):
  dfNewList = []
  for i in range(len(dfList)):
    dfListSalcDiv = dfList[i] / numberOfImages
    dfNewList.insert(len(dfList), dfListSalcDiv)
  return dfNewList

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                                                #
#                      VARS                      #
#                                                #
# ============================================== #

# ============================================== #
#                SINGLE-MODALITY                 #
# ============================================== #

# ------------------ TIME ---------------------- #

sm_time_94662 = datafile_fs.time_94662[:MV_N]
sm_time_607376 = datafile_fs.time_607376[:MV_N]
sm_time_737037 = datafile_fs.time_737037[:MV_N]

sm_time_94662_list = sm_time_94662.tolist()
sm_time_607376_list = sm_time_607376.tolist()
sm_time_737037_list = sm_time_737037.tolist()

sm_time_94662_sorted_list = sorted(sm_time_94662_list)
sm_time_607376_sorted_list = sorted(sm_time_607376_list)
sm_time_737037_sorted_list = sorted(sm_time_737037_list)

smt94662c = dataImageNorm(sm_time_94662_list, sm_num_img_94662)
smt607376c = dataImageNorm(sm_time_607376_list, sm_num_img_607376)
smt737037c = dataImageNorm(sm_time_737037_list, sm_num_img_737037)

sm_time_94662_charted = smt94662c
sm_time_607376_charted = smt607376c
sm_time_737037_charted = smt737037c

# ---------------------------------------------- #

# ----------------- CLICKS --------------------- #

sm_clicks_94662 = datafile_fs.clicks_94662[:MV_N]
sm_clicks_607376 = datafile_fs.clicks_607376[:MV_N]
sm_clicks_737037 = datafile_fs.clicks_737037[:MV_N]

sm_clicks_94662_list = sm_clicks_94662.tolist()
sm_clicks_607376_list = sm_clicks_607376.tolist()
sm_clicks_737037_list = sm_clicks_737037.tolist()

sm_clicks_94662_sorted_list = sorted(sm_time_94662_list)
sm_clicks_607376_sorted_list = sorted(sm_time_607376_list)
sm_clicks_737037_sorted_list = sorted(sm_time_737037_list)

smc94662c = dataImageNorm(sm_clicks_94662_list, sm_num_img_94662)
smc607376c = dataImageNorm(sm_clicks_607376_list, sm_num_img_607376)
smc737037c = dataImageNorm(sm_clicks_737037_list, sm_num_img_737037)

sm_clicks_94662_charted = smc94662c
sm_clicks_607376_charted = smc607376c
sm_clicks_737037_charted = smc737037c

# ---------------------------------------------- #

# ----------------- ERRORS --------------------- #

sm_errors_94662 = datafile_fs.errors_94662[:MV_N]
sm_errors_607376 = datafile_fs.errors_607376[:MV_N]
sm_errors_737037 = datafile_fs.errors_737037[:MV_N]

sm_errors_94662_list = sm_errors_94662.tolist()
sm_errors_607376_list = sm_errors_607376.tolist()
sm_errors_737037_list = sm_errors_737037.tolist()

sm_errors_94662_sorted_list = sorted(sm_time_94662_list)
sm_errors_607376_sorted_list = sorted(sm_time_607376_list)
sm_errors_737037_sorted_list = sorted(sm_time_737037_list)

sme94662c = dataImageNorm(sm_errors_94662_list, sm_num_img_94662)
sme607376c = dataImageNorm(sm_errors_607376_list, sm_num_img_607376)
sme737037c = dataImageNorm(sm_errors_737037_list, sm_num_img_737037)

sm_errors_94662_charted = sme94662c
sm_errors_607376_charted = sme607376c
sm_errors_737037_charted = sme737037c

# ---------------------------------------------- #

# ============================================== #
# ============================================== #

# ============================================== #
#                 MULTI-MODALITY                 #
# ============================================== #

# ------------------ TIME ---------------------- #

mm_time_94662 = datafile_fm.time_94662[:MV_N]
mm_time_607376 = datafile_fm.time_607376[:MV_N]
mm_time_737037 = datafile_fm.time_737037[:MV_N]

mm_time_94662_list = mm_time_94662.tolist()
mm_time_607376_list = mm_time_607376.tolist()
mm_time_737037_list = mm_time_737037.tolist()

mm_time_94662_sorted_list = sorted(mm_time_94662_list)
mm_time_607376_sorted_list = sorted(mm_time_607376_list)
mm_time_737037_sorted_list = sorted(mm_time_737037_list)

mmt94662c = dataImageNorm(mm_time_94662_list, mm_num_img_94662)
mmt607376c = dataImageNorm(mm_time_607376_list, mm_num_img_607376)
mmt737037c = dataImageNorm(mm_time_737037_list, mm_num_img_737037)

mm_time_94662_charted = mmt94662c
mm_time_607376_charted = mmt607376c
mm_time_737037_charted = mmt737037c

# ---------------------------------------------- #

# ----------------- CLICKS --------------------- #

mm_clicks_94662 = datafile_fm.clicks_94662[:MV_N]
mm_clicks_607376 = datafile_fm.clicks_607376[:MV_N]
mm_clicks_737037 = datafile_fm.clicks_737037[:MV_N]

mm_clicks_94662_list = mm_clicks_94662.tolist()
mm_clicks_607376_list = mm_clicks_607376.tolist()
mm_clicks_737037_list = mm_clicks_737037.tolist()

mm_clicks_94662_sorted_list = sorted(mm_clicks_94662_list)
mm_clicks_607376_sorted_list = sorted(mm_clicks_607376_list)
mm_clicks_737037_sorted_list = sorted(mm_clicks_737037_list)

mmc94662c = dataImageNorm(mm_clicks_94662_list, mm_num_img_94662)
mmc607376c = dataImageNorm(mm_clicks_607376_list, mm_num_img_607376)
mmc737037c = dataImageNorm(mm_clicks_737037_list, mm_num_img_737037)

mm_clicks_94662_charted = mmc94662c
mm_clicks_607376_charted = mmc607376c
mm_clicks_737037_charted = mmc737037c

# ---------------------------------------------- #

# ----------------- ERRORS --------------------- #

mm_errors_94662 = datafile_fm.errors_94662[:MV_N]
mm_errors_607376 = datafile_fm.errors_607376[:MV_N]
mm_errors_737037 = datafile_fm.errors_737037[:MV_N]

mm_errors_94662_list = mm_errors_94662.tolist()
mm_errors_607376_list = mm_errors_607376.tolist()
mm_errors_737037_list = mm_errors_737037.tolist()

mm_errors_94662_sorted_list = sorted(mm_errors_94662_list)
mm_errors_607376_sorted_list = sorted(mm_errors_607376_list)
mm_errors_737037_sorted_list = sorted(mm_errors_737037_list)

mme94662c = dataImageNorm(mm_errors_94662_list, mm_num_img_94662)
mme607376c = dataImageNorm(mm_errors_607376_list, mm_num_img_607376)
mme737037c = dataImageNorm(mm_errors_737037_list, mm_num_img_737037)

mm_errors_94662_charted = mme94662c
mm_errors_607376_charted = mme607376c
mm_errors_737037_charted = mme737037c

# ---------------------------------------------- #

# ============================================== #
# ============================================== #

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

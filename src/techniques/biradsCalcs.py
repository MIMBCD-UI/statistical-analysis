#!/usr/bin/env python

"""biradsCalcs.py: Calculations for the BI-RADS."""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "ACADEMIC & COMMERCIAL"
__version__     = "1.0.0"
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

sa_techniques_dir = (pathAbsPath + '/statistical-analysis/src/techniques/')
sa_constants_dir = (pathAbsPath + '/statistical-analysis/src/constants/')
sa_methods_dir = (pathAbsPath + '/statistical-analysis/src/methods/')
src_dir = (pathAbsPath + '/sheet-reader/src/core/')
constants_dir = (pathAbsPath + '/sheet-reader/src/constants/')
techniques_dir = (pathAbsPath + '/sheet-reader/src/techniques/')

sys.path.append(sa_techniques_dir)
sys.path.append(sa_constants_dir)
sys.path.append(sa_methods_dir)
sys.path.append(src_dir)
sys.path.append(constants_dir)
sys.path.append(techniques_dir)

from nasa import nasaColMean

import main_variables
import sheets
import special
import structures
import sheetReaders
import iterators

MV_N = main_variables.N
birads_columns = structures.birads_columns
sm_birads_labels = structures.sm_birads_labels
mm_birads_labels = structures.mm_birads_labels
filterByColumn = structures.filterByColumn
figSizeX = structures.figSizeX
figSizeY = structures.figSizeY

main_sheet_dir = pathAbsPath + '/sheet-reader/data/temp/main_sheet.csv'
fs_sheet_dir = pathAbsPath + '/sheet-reader/data/temp/fs_sheet.csv'
fm_sheet_dir = pathAbsPath + '/sheet-reader/data/temp/fm_sheet.csv'

import plotly
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly import figure_factory as FF

plotly.tools.set_credentials_file(username='FMCalisto', api_key='nYNjIeeTiMtCSI24Hnav')

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

def biradsAbsList(df_birads_list, real_birads):
  gt_list = []
  for i in range(len(df_birads_list)):
    gt_calc_sub = df_birads_list[i] - real_birads
    gt_calc_alg = gt_calc_sub / real_birads
    gt_calc_abs = abs(gt_calc_sub)
    gt_list.insert(len(df_birads_list), gt_calc_abs)
  return gt_list

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                                                #
#                      VARS                      #
#                                                #
# ============================================== #

real_birads_94662 = special.real_birads_94662
real_birads_607376 = special.real_birads_607376
real_birads_737037 = special.real_birads_737037

# ============================================== #
#                SINGLE-MODALITY                 #
# ============================================== #

df_fs_birads_94662 = datafile_fs.birads_94662[:MV_N]
df_fs_birads_607376 = datafile_fs.birads_607376[:MV_N]
df_fs_birads_737037 = datafile_fs.birads_737037[:MV_N]

df_fs_birads_94662_list = df_fs_birads_94662.tolist()
df_fs_birads_607376_list = df_fs_birads_607376.tolist()
df_fs_birads_737037_list = df_fs_birads_737037.tolist()

gt_fs_birads_94662_list = biradsAbsList(df_fs_birads_94662_list, real_birads_94662)
gt_fs_birads_607376_list = biradsAbsList(df_fs_birads_607376_list, real_birads_607376)
gt_fs_birads_737037_list = biradsAbsList(df_fs_birads_737037_list, real_birads_737037)

# ============================================== #
# ============================================== #

# ============================================== #
#                 MULTI-MODALITY                 #
# ============================================== #

df_fm_birads_94662 = datafile_fm.birads_94662[:MV_N]
df_fm_birads_607376 = datafile_fm.birads_607376[:MV_N]
df_fm_birads_737037 = datafile_fm.birads_737037[:MV_N]

df_fm_assis_94662 = datafile_fm.assis_94662[:MV_N]
df_fm_assis_607376 = datafile_fm.assis_607376[:MV_N]
df_fm_assis_737037 = datafile_fm.assis_737037[:MV_N]

df_fm_birads_94662_list = df_fm_birads_94662.tolist()
df_fm_birads_607376_list = df_fm_birads_607376.tolist()
df_fm_birads_737037_list = df_fm_birads_737037.tolist()

df_fm_assis_94662_list = df_fm_assis_94662.tolist()
df_fm_assis_607376_list = df_fm_assis_607376.tolist()
df_fm_assis_737037_list = df_fm_assis_737037.tolist()

gt_fm_birads_94662_list = biradsAbsList(df_fm_birads_94662_list, real_birads_94662)
gt_fm_birads_607376_list = biradsAbsList(df_fm_birads_607376_list, real_birads_607376)
gt_fm_birads_737037_list = biradsAbsList(df_fm_birads_737037_list, real_birads_737037)

gt_fm_assis_94662_list = biradsAbsList(df_fm_assis_94662_list, real_birads_94662)
gt_fm_assis_607376_list = biradsAbsList(df_fm_assis_607376_list, real_birads_607376)
gt_fm_assis_737037_list = biradsAbsList(df_fm_assis_737037_list, real_birads_737037)

# ============================================== #
# ============================================== #

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

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
joinPath = os.path.join(pathDirname, '..', '..')
pathAbsPath = os.path.abspath(joinPath)

sa_scripts_dir = (pathAbsPath + '/statistical-analysis/scripts/')
sa_constants_dir = (pathAbsPath + '/statistical-analysis/constants/')
sa_methods_dir = (pathAbsPath + '/statistical-analysis/methods/')
src_dir = (pathAbsPath + '/sheet-reader/src/')
constants_dir = (pathAbsPath + '/sheet-reader/constants/')
scripts_dir = (pathAbsPath + '/sheet-reader/scripts/')

sys.path.append(sa_scripts_dir)
sys.path.append(sa_constants_dir)
sys.path.append(sa_methods_dir)
sys.path.append(src_dir)
sys.path.append(constants_dir)
sys.path.append(scripts_dir)

from nasa import nasaColMean

import main_variables
import structures
import sheet
import sheetReaders
import iterators
import ploters

birads_columns = structures.birads_columns
birads_labels = structures.birads_labels
filterByColumn = structures.filterByColumn
figSizeX = structures.figSizeX
figSizeY = structures.figSizeY

main_sheet_dir = pathAbsPath + '/sheet-reader/temp/main_sheet.csv'
fs_sheet_dir = pathAbsPath + '/sheet-reader/temp/fs_sheet.csv'
fm_sheet_dir = pathAbsPath + '/sheet-reader/temp/fm_sheet.csv'

import plotly.plotly as py
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

datafile_fs = sheet.datafile_fs
datafile_fm = sheet.datafile_fm

createBoxplot = ploters.createBoxplot

# ============================================== #
#                                                #
#                 CREATE BOXPLOT                 #
#                                                #
# ============================================== #

# ============================================== #
#                SINGLE-MODALITY                 #
# ============================================== #

# createBoxplot(datafile_fs, filterByColumn, nasatlx_columns)
# createBoxplot(datafile_fs, filterByColumn, sus_columns)
# createBoxplot(datafile_fs, filterByColumn, measures_columns)
# createBoxplot(datafile_fs, filterByColumn, birads_columns)

# ============================================== #
# ============================================== #

# ============================================== #
#                 MULTI-MODALITY                 #
# ============================================== #

# createBoxplot(datafile_fm, filterByColumn, nasatlx_columns)
# createBoxplot(datafile_fm, filterByColumn, sus_columns)
# createBoxplot(datafile_fm, filterByColumn, measures_columns)
# createBoxplot(datafile_fm, filterByColumn, birads_columns)

# ============================================== #
# ============================================== #

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

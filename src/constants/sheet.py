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
import structures
import sheetReaders
import iterators

MV_N = main_variables.N
experience = structures.experience
nasatlx_columns = structures.nasatlx_columns
sus_columns = structures.sus_columns
sus_questions = structures.sus_questions
measures_columns = structures.measures_columns
birads_columns = structures.birads_columns
filterByColumn = structures.filterByColumn
figSizeX = structures.figSizeX
figSizeY = structures.figSizeY
datafileIteratorPerGroup = iterators.datafileIteratorPerGroup

main_sheet_dir = pathAbsPath + '/sheet-reader/data/temp/main_sheet.csv'
fs_sheet_dir = pathAbsPath + '/sheet-reader/data/temp/fs_sheet.csv'
fm_sheet_dir = pathAbsPath + '/sheet-reader/data/temp/fm_sheet.csv'

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

datafile_fs = pd.read_csv(fs_sheet_dir)
datafile_fm = pd.read_csv(fm_sheet_dir)

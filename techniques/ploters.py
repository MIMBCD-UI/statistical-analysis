#!/usr/bin/env python

"""ploters.py: Generators of several plots."""

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
joinPath = os.path.join(pathDirname, '..', '..')
pathAbsPath = os.path.abspath(joinPath)

sa_constants_dir = (pathAbsPath + '/statistical-analysis/constants/')
sa_methods_dir = (pathAbsPath + '/statistical-analysis/methods/')

sys.path.append(sa_constants_dir)
sys.path.append(sa_methods_dir)

from listGroups import *
from dataFileVectors import *
from replacers import *

import structures
import sheet

experience = structures.experience
nasatlx_columns = structures.nasatlx_columns
sus_columns = structures.sus_columns
measures_columns = structures.measures_columns
birads_columns = structures.birads_columns
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

# ============================================== #
#                                                #
#              BOXPLOT DEFINITIONS               #
#                                                #
# ============================================== #

# ============================================== #
#                   CREATORS                     #
# ============================================== #

def createBoxplot(dataFile, filterBy, array):
  i = 0
  for i in range(len(array)):
    dataFile.boxplot(array[i], by=filterByColumn, figsize=(figSizeX, figSizeY))

# ============================================== #
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
#             SUS: Grouped Box Plots             #
# ============================================== #

x = datafile_vec
x_fs = datafile_fs_vec
x_fm = datafile_fm_vec

trace_fs_intern = go.Box(
  y=lg_fs_sus_intern,
  x=varReplacer_fs_intern,
  name='SM: Intern',
  boxpoints = False,
  marker=dict(
    color='#1E824C'
  )
)

trace_fm_intern = go.Box(
  y=lg_fm_sus_intern,
  x=varReplacer_fm_intern,
  name='MM: Intern',
  boxpoints = False,
  marker=dict(
    color='#049372'
  )
)

trace_fs_junior = go.Box(
  y=lg_fs_sus_junior,
  x=varReplacer_fs_junior,
  name='SM: Junior',
  boxpoints = False,
  marker=dict(
    color='#663399'
  )
)

trace_fm_junior = go.Box(
  y=lg_fm_sus_junior,
  x=varReplacer_fm_junior,
  name='MM: Junior',
  boxpoints = False,
  marker=dict(
    color='#913D88'
  )
)

trace_fs_middle = go.Box(
  y=lg_fs_sus_middle,
  x=varReplacer_fs_middle,
  name='SM: Middle',
  boxpoints = False,
  marker=dict(
    color='#4183D7'
  )
)

trace_fm_middle = go.Box(
  y=lg_fm_sus_middle,
  x=varReplacer_fm_middle,
  name='MM: Middle',
  boxpoints = False,
  marker=dict(
    color='#59ABE3'
  )
)

trace_fs_senior = go.Box(
  y=lg_fs_sus_senior,
  x=varReplacer_fs_senior,
  name='SM: Senior',
  boxpoints = False,
  marker=dict(
    color='#F22613'
  )
)

trace_fm_senior = go.Box(
  y=lg_fm_sus_senior,
  x=varReplacer_fm_senior,
  name='MM: Senior',
  boxpoints = False,
  marker=dict(
    color='#C0392B'
  )
)

data = [
  trace_fs_intern,
  trace_fm_intern,
  trace_fs_junior,
  trace_fm_junior,
  trace_fs_middle,
  trace_fm_middle,
  trace_fs_senior,
  trace_fm_senior
]

layout = go.Layout(
  yaxis=dict(
    title='SUS Scores',
    zeroline=False
  ),
  xaxis=dict(
    title='SUS Questions',
    zeroline=False
  ),
  boxmode='group'
)

# REFACTOR!!!

fig = go.Figure(data=data, layout=layout)
#py.plot(fig, filename = "sus_scores_vs_sus_questions")

# ============================================== #
# ============================================== #

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

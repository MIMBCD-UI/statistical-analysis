#!/usr/bin/env python

"""ploters.py: Generators of several plots."""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "ACADEMIC & COMMERCIAL"
__version__     = "1.2.1"
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

sa_constants_dir = os.path.join(pathAbsPath, 'statistical-analysis', 'constants')
sa_methods_dir = os.path.join(pathAbsPath, 'statistical-analysis', 'methods')
techniques_dir = os.path.join(pathAbsPath, 'ssheet-reader', 'techniques')

sys.path.append(sa_constants_dir)
sys.path.append(sa_methods_dir)
sys.path.append(techniques_dir)

from listGroups import *
from dataFileVectors import *
from replacers import *
from biradsCalcs import *

import structures
import sheet

experience = structures.experience
nasatlx_columns = structures.nasatlx_columns
sus_columns = structures.sus_columns
measures_columns = structures.measures_columns
birads_columns = structures.birads_columns
mm_assis_labels = structures.mm_assis_labels
filterByColumn = structures.filterByColumn
figSizeX = structures.figSizeX
figSizeY = structures.figSizeY

main_sheet_dir = os.path.join(pathAbsPath, 'sheet-reader', 'temp', 'main_sheet.csv')
fs_sheet_dir = os.path.join(pathAbsPath, 'sheet-reader', 'temp', 'fs_sheet.csv')
fm_sheet_dir = os.path.join(pathAbsPath, 'sheet-reader', 'temp', 'fm_sheet.csv')

sys.path.append(main_sheet_dir)
sys.path.append(fs_sheet_dir)
sys.path.append(fm_sheet_dir)

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
  for i in range(len(array)):
    dataFile.boxplot(array[i], by=filterByColumn, figsize=(figSizeX, figSizeY))

# ============================================== #
# ============================================== #

# ============================================== #
#                SINGLE-MODALITY                 #
# ============================================== #

createBoxplot(datafile_fs, filterByColumn, nasatlx_columns)
createBoxplot(datafile_fs, filterByColumn, sus_columns)
createBoxplot(datafile_fs, filterByColumn, measures_columns)
createBoxplot(datafile_fs, filterByColumn, birads_columns)

# ============================================== #
# ============================================== #

# ============================================== #
#                 MULTI-MODALITY                 #
# ============================================== #

createBoxplot(datafile_fm, filterByColumn, nasatlx_columns)
createBoxplot(datafile_fm, filterByColumn, sus_columns)
createBoxplot(datafile_fm, filterByColumn, measures_columns)
createBoxplot(datafile_fm, filterByColumn, birads_columns)

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

dataSus = [
  trace_fs_intern,
  trace_fm_intern,
  trace_fs_junior,
  trace_fm_junior,
  trace_fs_middle,
  trace_fm_middle,
  trace_fs_senior,
  trace_fm_senior
]

layoutSus = go.Layout(
  yaxis=dict(
    title='SUS Scores',
    titlefont=dict(
      size=24
    ),
    tickfont=dict(
      size=14
    ),
    zeroline=False
  ),
  xaxis=dict(
    title='SUS Questions',
    titlefont=dict(
      size=24
    ),
    tickfont=dict(
      size=14
    ),
    zeroline=False
  ),
  legend=dict(
    font=dict(
      size=18
    )
  ),
  boxmode='group',
  width=1000,
  height=500,
  boxgap=0.05,
  boxgroupgap=0.25,
)

figSus = go.Figure(data=dataSus, layout=layoutSus)
py.plot(figSus, filename = "sus_scores_vs_sus_questions")

# ============================================== #
# ============================================== #

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                                                #
#                    BIRADS                      #
#                                                #
# ============================================== #

trace0 = go.Box(
  y=gt_fs_birads_94662_list,
  name=sm_birads_labels[0],
  boxpoints = False,
  marker=dict(
    color='rgb(26, 188, 156)',
  ),
  boxmean='sd'
)

trace1 = go.Box(
  y=gt_fm_birads_94662_list,
  name=mm_birads_labels[0],
  boxpoints = False,
  marker=dict(
    color='rgb(22, 160, 133)',
  ),
  boxmean='sd'
)

trace2 = go.Box(
  y=gt_fm_assis_94662_list,
  name=mm_assis_labels[0],
  boxpoints = False,
  marker=dict(
    color='rgb(18, 160, 133)',
  ),
  boxmean='sd'
)

trace3 = go.Box(
  y=gt_fs_birads_607376_list,
  name=sm_birads_labels[1],
  boxpoints = False,
  marker=dict(
    color='rgb(52, 152, 219)',
  ),
  boxmean='sd'
)

trace4 = go.Box(
  y=gt_fm_birads_607376_list,
  name=mm_birads_labels[1],
  boxpoints = False,
  marker=dict(
    color='rgb(41, 128, 185)',
  ),
  boxmean='sd'
)

trace5 = go.Box(
  y=gt_fm_assis_607376_list,
  name=mm_assis_labels[1],
  boxpoints = False,
  marker=dict(
    color='rgb(38, 92, 131)',
  ),
  boxmean='sd'
)

trace6 = go.Box(
  y=gt_fs_birads_737037_list,
  name=sm_birads_labels[2],
  boxpoints = False,
  marker=dict(
    color='rgb(155, 89, 182)',
  ),
  boxmean='sd'
)

trace7 = go.Box(
  y=gt_fm_birads_737037_list,
  name=mm_birads_labels[2],
  boxpoints = False,
  marker=dict(
    color='rgb(142, 68, 173)',
  ),
  boxmean='sd'
)

trace8 = go.Box(
  y=gt_fm_assis_737037_list,
  name=mm_assis_labels[2],
  boxpoints = False,
  marker=dict(
    color='rgb(137, 47, 164)',
  ),
  boxmean='sd'
)

dataBirads = [
  trace0,
  trace1,
  trace2,
  trace3,
  trace4,
  trace5,
  trace6,
  trace7,
  trace8
]

layoutBirads = go.Layout(
  title = "BI-RADS Variation & SD",
  xaxis = dict(
    titlefont=dict(
      size=24
    ),
    tickfont=dict(
      size=14
    ),
  ),
  yaxis = dict(
    titlefont=dict(
      size=24
    ),
    tickfont=dict(
      size=14
    ),
  ),
  legend=dict(
    font=dict(
      size=18
    )
  ),
  width=1000,
  height=500,
  boxgap=0.05,
  boxgroupgap=0.25,
)

layoutBirads2 = go.Layout(
  title = "BI-RADS Variation & SD",
  xaxis = dict(
    titlefont=dict(
      size=24
    ),
    tickfont=dict(
      size=14
    ),
  ),
  yaxis = dict(
    titlefont=dict(
      size=24
    ),
    tickfont=dict(
      size=14
    ),
  ),
  legend=dict(
    font=dict(
      size=18
    )
  )
)

figBirads = go.Figure(data=dataBirads, layout=layoutBirads)
py.plot(figBirads, filename = "birads_variation_sd")

# figBirads = go.Figure(data=dataBirads, layout=layoutBirads2)
# py.plot(figBirads, filename = "birads_variation_sd")

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

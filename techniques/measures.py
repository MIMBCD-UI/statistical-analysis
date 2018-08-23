#!/usr/bin/env python

"""measures.py: Calculations for the Time, Number of Clicks and Number of Errors."""

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

sa_techniques_dir = (pathAbsPath + '/statistical-analysis/techniques/')
sa_constants_dir = (pathAbsPath + '/statistical-analysis/constants/')
sa_methods_dir = (pathAbsPath + '/statistical-analysis/methods/')
src_dir = (pathAbsPath + '/sheet-reader/src/')
constants_dir = (pathAbsPath + '/sheet-reader/constants/')
techniques_dir = (pathAbsPath + '/sheet-reader/techniques/')

sys.path.append(sa_techniques_dir)
sys.path.append(sa_constants_dir)
sys.path.append(sa_methods_dir)
sys.path.append(src_dir)
sys.path.append(constants_dir)
sys.path.append(techniques_dir)

from nasa import nasaColMean

import main_variables
import sheet
import special
import structures
import sheetReaders
import iterators
import ploters

MV_N = main_variables.N
sm_num_img_94662 = special.sm_num_img_94662
sm_num_img_607376 = special.sm_num_img_607376
sm_num_img_737037 = special.sm_num_img_737037
mm_num_img_94662 = special.mm_num_img_94662
mm_num_img_607376 = special.mm_num_img_607376
mm_num_img_737037 = special.mm_num_img_737037
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

# ============================================== #
#                                                #
#                    CHARTS                      #
#                                                #
# ============================================== #

# Create traces

trace0 = go.Scatter(
  x = sm_time_94662_charted,
  y = sm_clicks_94662_charted,
  mode = 'markers',
  name = 'SM: 94662',
  marker=dict(
    color='rgb(26, 188, 156)',
  )
)

trace1 = go.Scatter(
  x = mm_time_94662_charted,
  y = mm_clicks_94662_charted,
  mode = 'markers',
  name = 'MM: 94662',
  marker=dict(
    color='rgb(243, 156, 18)',
  )
)

trace2 = go.Scatter(
  x = sm_time_607376_charted,
  y = sm_clicks_607376_charted,
  mode = 'markers',
  name = 'SM: 607376',
  marker=dict(
    color='rgb(52, 152, 219)',
  )
)

trace3 = go.Scatter(
  x = mm_time_607376_charted,
  y = mm_clicks_607376_charted,
  mode = 'markers',
  name = 'MM: 607376',
  marker=dict(
    color='rgb(192, 57, 43)',
  )
)

trace4 = go.Scatter(
  x = sm_time_737037_charted,
  y = sm_clicks_737037_charted,
  mode = 'markers',
  name = 'SM: 737037',
  marker=dict(
    color='rgb(155, 89, 182)',
  )
)

trace5 = go.Scatter(
  x = mm_time_737037_charted,
  y = mm_clicks_737037_charted,
  mode = 'markers',
  name = 'MM: 737037',
  marker=dict(
    color='rgb(44, 62, 80)',
  )
)

data0 = [
  trace0,
  trace2,
  trace4,
]

data1 = [
  trace1,
  trace3,
  trace5,
]

cluster0 = [dict(type='circle',
  xref='x', yref='y',
  x0=min(sm_time_94662_charted), y0=min(sm_clicks_94662_charted),
  x1=max(sm_time_94662_charted), y1=max(sm_clicks_94662_charted),
  opacity=.25,
  line=dict(color='rgb(26, 188, 156)'),
  fillcolor='rgb(26, 188, 156)')]

cluster1 = [dict(type='circle',
  xref='x', yref='y',
  x0=min(mm_time_94662_charted), y0=min(mm_clicks_94662_charted),
  x1=max(mm_time_94662_charted), y1=max(mm_clicks_94662_charted),
  opacity=.25,
  line=dict(color='rgb(243, 156, 18)'),
  fillcolor='rgb(243, 156, 18)')]

cluster2 = [dict(type='circle',
  xref='x', yref='y',
  x0=min(sm_time_607376_charted), y0=min(sm_clicks_607376_charted),
  x1=max(sm_time_607376_charted), y1=max(sm_clicks_607376_charted),
  opacity=.25,
  line=dict(color='rgb(52, 152, 219)'),
  fillcolor='rgb(52, 152, 219)')]

cluster3 = [dict(type='circle',
  xref='x', yref='y',
  x0=min(mm_time_607376_charted), y0=min(mm_clicks_607376_charted),
  x1=max(mm_time_607376_charted), y1=max(mm_clicks_607376_charted),
  opacity=.25,
  line=dict(color='rgb(192, 57, 43)'),
  fillcolor='rgb(192, 57, 43)')]

cluster4 = [dict(type='circle',
  xref='x', yref='y',
  x0=min(sm_time_737037_charted), y0=min(sm_clicks_737037_charted),
  x1=max(sm_time_737037_charted), y1=max(sm_clicks_737037_charted),
  opacity=.25,
  line=dict(color='rgb(155, 89, 182)'),
  fillcolor='rgb(155, 89, 182)')]

cluster5 = [dict(type='circle',
  xref='x', yref='y',
  x0=min(mm_time_737037_charted), y0=min(mm_clicks_737037_charted),
  x1=max(mm_time_737037_charted), y1=max(mm_clicks_737037_charted),
  opacity=.25,
  line=dict(color='rgb(44, 62, 80)'),
  fillcolor='rgb(44, 62, 80)')]

smAllClusters = cluster0 + cluster2 + cluster4
mmAllClusters = cluster1 + cluster3 + cluster5

smUpdatemenus = list([
  dict(buttons=list([
    dict(label = 'None',
      method = 'relayout',
      args = ['shapes', []]),
    dict(label = 'SM: 94662 Cluster',
      method = 'relayout',
      args = ['shapes', cluster0]),
    dict(label = 'SM: 607376 Cluster',
      method = 'relayout',
      args = ['shapes', cluster2]),
    dict(label = 'SM: 737037 Cluster',
      method = 'relayout',
      args = ['shapes', cluster4]),
    dict(label = 'All',
     method = 'relayout',
     args = ['shapes', smAllClusters])
  ]),
  )
])

mmUpdatemenus = list([
  dict(buttons=list([
    dict(label = 'None',
      method = 'relayout',
      args = ['shapes', []]),
    dict(label = 'Cluster 0',
      method = 'relayout',
      args = ['shapes', cluster1]),
    dict(label = 'Cluster 1',
      method = 'relayout',
      args = ['shapes', cluster3]),
    dict(label = 'Cluster 2',
      method = 'relayout',
      args = ['shapes', cluster5]),
    dict(label = 'All',
     method = 'relayout',
     args = ['shapes', mmAllClusters])
  ]),
  )
])

layout0 = go.Layout(
  title = "[Single-Modality] Measurements: Time vs Number of Clicks",
  xaxis = dict(title = 'Time'),
  yaxis = dict(title = 'Number of Clicks'),
  updatemenus=smUpdatemenus,
)

layout1 = go.Layout(
  title = "[Multi-Modality] Measurements: Time vs Number of Clicks",
  xaxis = dict(title = 'Time'),
  yaxis = dict(title = 'Number of Clicks'),
  updatemenus=mmUpdatemenus,
)

fig0 = go.Figure(data=data0, layout=layout0)
fig1 = go.Figure(data=data1, layout=layout1)
py.plot(fig0, filename='sm_measures_time_vs_clicks')
py.plot(fig1, filename='mm_measures_time_vs_clicks')

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

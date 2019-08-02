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
joinPath = os.path.join(pathDirname, '..', '..', '..')
pathAbsPath = os.path.abspath(joinPath)

sa_constants_dir = os.path.join(pathAbsPath, 'statistical-analysis', 'src', 'constants')
sa_methods_dir = os.path.join(pathAbsPath, 'statistical-analysis', 'src', 'methods')
techniques_dir = os.path.join(pathAbsPath, 'ssheet-reader', 'src', 'techniques')
variables_dir = os.path.join(pathAbsPath, 'ssheet-reader', 'src', 'variables')

sys.path.append(sa_constants_dir)
sys.path.append(sa_methods_dir)
sys.path.append(techniques_dir)
sys.path.append(variables_dir)

from listGroups import *
from dataFileVectors import *
from replacers import *
from biradsCalcs import *

from structures import *
from sheets import *
from dataFrames import *

from baseStatisticalAnalysis import *

experience = structures.experience
nasatlx_columns = structures.nasatlx_columns
sus_columns = structures.sus_columns
measures_columns = structures.measures_columns
birads_columns = structures.birads_columns
mm_assis_labels = structures.mm_assis_labels
filterByColumn = structures.filterByColumn
figSizeX = structures.figSizeX
figSizeY = structures.figSizeY

main_sheet_dir = os.path.join(pathAbsPath, 'sheet-reader', 'data', 'temp', 'main_sheet.csv')
fs_sheet_dir = os.path.join(pathAbsPath, 'sheet-reader', 'data', 'temp', 'fs_sheet.csv')
fm_sheet_dir = os.path.join(pathAbsPath, 'sheet-reader', 'data', 'temp', 'fm_sheet.csv')

sys.path.append(main_sheet_dir)
sys.path.append(fs_sheet_dir)
sys.path.append(fm_sheet_dir)

import plotly
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
#              BOXPLOT DEFINITIONS               #
#                                                #
# ============================================== #

# ============================================== #
#                   CREATORS                     #
# ============================================== #

# def createBoxplot(dataFile, filterBy, array):
#   for i in range(len(array)):
#     stringTo = array[i]
#     dataFile.boxplot(stringTo, by=filterByColumn, figsize=(figSizeX, figSizeY))

# ============================================== #
# ============================================== #

# ============================================== #
#                                                #
#                       UTA7                     #
#                                                #
# ============================================== #

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++++++ SUS +++++++++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

# ++++++++++++++++ Current +++++++++++++++++++++ #

freq_sus_crrnt_01_1 = df_sus_crrnt[fne601][df_sus_crrnt[fne601] == 1]
freq_sus_crrnt_01_2 = df_sus_crrnt[fne601][df_sus_crrnt[fne601] == 2]
freq_sus_crrnt_01_3 = df_sus_crrnt[fne601][df_sus_crrnt[fne601] == 3]
freq_sus_crrnt_01_4 = df_sus_crrnt[fne601][df_sus_crrnt[fne601] == 4]
freq_sus_crrnt_01_5 = df_sus_crrnt[fne601][df_sus_crrnt[fne601] == 5]

freq_sus_crrnt_02_1 = df_sus_crrnt[fne602][df_sus_crrnt[fne602] == 1]
freq_sus_crrnt_02_2 = df_sus_crrnt[fne602][df_sus_crrnt[fne602] == 2]
freq_sus_crrnt_02_3 = df_sus_crrnt[fne602][df_sus_crrnt[fne602] == 3]
freq_sus_crrnt_02_4 = df_sus_crrnt[fne602][df_sus_crrnt[fne602] == 4]
freq_sus_crrnt_02_5 = df_sus_crrnt[fne602][df_sus_crrnt[fne602] == 5]

freq_sus_crrnt_03_1 = df_sus_crrnt[fne603][df_sus_crrnt[fne603] == 1]
freq_sus_crrnt_03_2 = df_sus_crrnt[fne603][df_sus_crrnt[fne603] == 2]
freq_sus_crrnt_03_3 = df_sus_crrnt[fne603][df_sus_crrnt[fne603] == 3]
freq_sus_crrnt_03_4 = df_sus_crrnt[fne603][df_sus_crrnt[fne603] == 4]
freq_sus_crrnt_03_5 = df_sus_crrnt[fne603][df_sus_crrnt[fne603] == 5]

freq_sus_crrnt_04_1 = df_sus_crrnt[fne604][df_sus_crrnt[fne604] == 1]
freq_sus_crrnt_04_2 = df_sus_crrnt[fne604][df_sus_crrnt[fne604] == 2]
freq_sus_crrnt_04_3 = df_sus_crrnt[fne604][df_sus_crrnt[fne604] == 3]
freq_sus_crrnt_04_4 = df_sus_crrnt[fne604][df_sus_crrnt[fne604] == 4]
freq_sus_crrnt_04_5 = df_sus_crrnt[fne604][df_sus_crrnt[fne604] == 5]

freq_sus_crrnt_05_1 = df_sus_crrnt[fne605][df_sus_crrnt[fne605] == 1]
freq_sus_crrnt_05_2 = df_sus_crrnt[fne605][df_sus_crrnt[fne605] == 2]
freq_sus_crrnt_05_3 = df_sus_crrnt[fne605][df_sus_crrnt[fne605] == 3]
freq_sus_crrnt_05_4 = df_sus_crrnt[fne605][df_sus_crrnt[fne605] == 4]
freq_sus_crrnt_05_5 = df_sus_crrnt[fne605][df_sus_crrnt[fne605] == 5]

freq_sus_crrnt_06_1 = df_sus_crrnt[fne606][df_sus_crrnt[fne606] == 1]
freq_sus_crrnt_06_2 = df_sus_crrnt[fne606][df_sus_crrnt[fne606] == 2]
freq_sus_crrnt_06_3 = df_sus_crrnt[fne606][df_sus_crrnt[fne606] == 3]
freq_sus_crrnt_06_4 = df_sus_crrnt[fne606][df_sus_crrnt[fne606] == 4]
freq_sus_crrnt_06_5 = df_sus_crrnt[fne606][df_sus_crrnt[fne606] == 5]

freq_sus_crrnt_07_1 = df_sus_crrnt[fne607][df_sus_crrnt[fne607] == 1]
freq_sus_crrnt_07_2 = df_sus_crrnt[fne607][df_sus_crrnt[fne607] == 2]
freq_sus_crrnt_07_3 = df_sus_crrnt[fne607][df_sus_crrnt[fne607] == 3]
freq_sus_crrnt_07_4 = df_sus_crrnt[fne607][df_sus_crrnt[fne607] == 4]
freq_sus_crrnt_07_5 = df_sus_crrnt[fne607][df_sus_crrnt[fne607] == 5]

freq_sus_crrnt_08_1 = df_sus_crrnt[fne608][df_sus_crrnt[fne608] == 1]
freq_sus_crrnt_08_2 = df_sus_crrnt[fne608][df_sus_crrnt[fne608] == 2]
freq_sus_crrnt_08_3 = df_sus_crrnt[fne608][df_sus_crrnt[fne608] == 3]
freq_sus_crrnt_08_4 = df_sus_crrnt[fne608][df_sus_crrnt[fne608] == 4]
freq_sus_crrnt_08_5 = df_sus_crrnt[fne608][df_sus_crrnt[fne608] == 5]

freq_sus_crrnt_09_1 = df_sus_crrnt[fne609][df_sus_crrnt[fne609] == 1]
freq_sus_crrnt_09_2 = df_sus_crrnt[fne609][df_sus_crrnt[fne609] == 2]
freq_sus_crrnt_09_3 = df_sus_crrnt[fne609][df_sus_crrnt[fne609] == 3]
freq_sus_crrnt_09_4 = df_sus_crrnt[fne609][df_sus_crrnt[fne609] == 4]
freq_sus_crrnt_09_5 = df_sus_crrnt[fne609][df_sus_crrnt[fne609] == 5]

freq_sus_crrnt_10_1 = df_sus_crrnt[fne610][df_sus_crrnt[fne610] == 1]
freq_sus_crrnt_10_2 = df_sus_crrnt[fne610][df_sus_crrnt[fne610] == 2]
freq_sus_crrnt_10_3 = df_sus_crrnt[fne610][df_sus_crrnt[fne610] == 3]
freq_sus_crrnt_10_4 = df_sus_crrnt[fne610][df_sus_crrnt[fne610] == 4]
freq_sus_crrnt_10_5 = df_sus_crrnt[fne610][df_sus_crrnt[fne610] == 5]

ratio_sus_crrnt_01_1 = int(round((len(freq_sus_crrnt_01_1) / len(df_sus_crrnt[fne601])) * 100))
ratio_sus_crrnt_01_2 = int(round((len(freq_sus_crrnt_01_2) / len(df_sus_crrnt[fne601])) * 100))
ratio_sus_crrnt_01_3 = int(round((len(freq_sus_crrnt_01_3) / len(df_sus_crrnt[fne601])) * 100))
ratio_sus_crrnt_01_4 = int(round((len(freq_sus_crrnt_01_4) / len(df_sus_crrnt[fne601])) * 100))
ratio_sus_crrnt_01_5 = int(round((len(freq_sus_crrnt_01_5) / len(df_sus_crrnt[fne601])) * 100))

ratio_sus_crrnt_02_1 = int(round((len(freq_sus_crrnt_02_1) / len(df_sus_crrnt[fne602])) * 100))
ratio_sus_crrnt_02_2 = int(round((len(freq_sus_crrnt_02_2) / len(df_sus_crrnt[fne602])) * 100))
ratio_sus_crrnt_02_3 = int(round((len(freq_sus_crrnt_02_3) / len(df_sus_crrnt[fne602])) * 100))
ratio_sus_crrnt_02_4 = int(round((len(freq_sus_crrnt_02_4) / len(df_sus_crrnt[fne602])) * 100))
ratio_sus_crrnt_02_5 = int(round((len(freq_sus_crrnt_02_5) / len(df_sus_crrnt[fne602])) * 100))

ratio_sus_crrnt_03_1 = int(round((len(freq_sus_crrnt_03_1) / len(df_sus_crrnt[fne603])) * 100))
ratio_sus_crrnt_03_2 = int(round((len(freq_sus_crrnt_03_2) / len(df_sus_crrnt[fne603])) * 100))
ratio_sus_crrnt_03_3 = int(round((len(freq_sus_crrnt_03_3) / len(df_sus_crrnt[fne603])) * 100))
ratio_sus_crrnt_03_4 = int(round((len(freq_sus_crrnt_03_4) / len(df_sus_crrnt[fne603])) * 100))
ratio_sus_crrnt_03_5 = int(round((len(freq_sus_crrnt_03_5) / len(df_sus_crrnt[fne603])) * 100))

ratio_sus_crrnt_04_1 = int(round((len(freq_sus_crrnt_04_1) / len(df_sus_crrnt[fne604])) * 100))
ratio_sus_crrnt_04_2 = int(round((len(freq_sus_crrnt_04_2) / len(df_sus_crrnt[fne604])) * 100))
ratio_sus_crrnt_04_3 = int(round((len(freq_sus_crrnt_04_3) / len(df_sus_crrnt[fne604])) * 100))
ratio_sus_crrnt_04_4 = int(round((len(freq_sus_crrnt_04_4) / len(df_sus_crrnt[fne604])) * 100))
ratio_sus_crrnt_04_5 = int(round((len(freq_sus_crrnt_04_5) / len(df_sus_crrnt[fne604])) * 100))

ratio_sus_crrnt_05_1 = int(round((len(freq_sus_crrnt_05_1) / len(df_sus_crrnt[fne605])) * 100))
ratio_sus_crrnt_05_2 = int(round((len(freq_sus_crrnt_05_2) / len(df_sus_crrnt[fne605])) * 100))
ratio_sus_crrnt_05_3 = int(round((len(freq_sus_crrnt_05_3) / len(df_sus_crrnt[fne605])) * 100))
ratio_sus_crrnt_05_4 = int(round((len(freq_sus_crrnt_05_4) / len(df_sus_crrnt[fne605])) * 100))
ratio_sus_crrnt_05_5 = int(round((len(freq_sus_crrnt_05_5) / len(df_sus_crrnt[fne605])) * 100))

ratio_sus_crrnt_06_1 = int(round((len(freq_sus_crrnt_06_1) / len(df_sus_crrnt[fne606])) * 100))
ratio_sus_crrnt_06_2 = int(round((len(freq_sus_crrnt_06_2) / len(df_sus_crrnt[fne606])) * 100))
ratio_sus_crrnt_06_3 = int(round((len(freq_sus_crrnt_06_3) / len(df_sus_crrnt[fne606])) * 100))
ratio_sus_crrnt_06_4 = int(round((len(freq_sus_crrnt_06_4) / len(df_sus_crrnt[fne606])) * 100))
ratio_sus_crrnt_06_5 = int(round((len(freq_sus_crrnt_06_5) / len(df_sus_crrnt[fne606])) * 100))

ratio_sus_crrnt_07_1 = int(round((len(freq_sus_crrnt_07_1) / len(df_sus_crrnt[fne607])) * 100))
ratio_sus_crrnt_07_2 = int(round((len(freq_sus_crrnt_07_2) / len(df_sus_crrnt[fne607])) * 100))
ratio_sus_crrnt_07_3 = int(round((len(freq_sus_crrnt_07_3) / len(df_sus_crrnt[fne607])) * 100))
ratio_sus_crrnt_07_4 = int(round((len(freq_sus_crrnt_07_4) / len(df_sus_crrnt[fne607])) * 100))
ratio_sus_crrnt_07_5 = int(round((len(freq_sus_crrnt_07_5) / len(df_sus_crrnt[fne607])) * 100))

ratio_sus_crrnt_08_1 = int(round((len(freq_sus_crrnt_08_1) / len(df_sus_crrnt[fne608])) * 100))
ratio_sus_crrnt_08_2 = int(round((len(freq_sus_crrnt_08_2) / len(df_sus_crrnt[fne608])) * 100))
ratio_sus_crrnt_08_3 = int(round((len(freq_sus_crrnt_08_3) / len(df_sus_crrnt[fne608])) * 100))
ratio_sus_crrnt_08_4 = int(round((len(freq_sus_crrnt_08_4) / len(df_sus_crrnt[fne608])) * 100))
ratio_sus_crrnt_08_5 = int(round((len(freq_sus_crrnt_08_5) / len(df_sus_crrnt[fne608])) * 100))

ratio_sus_crrnt_09_1 = int(round((len(freq_sus_crrnt_09_1) / len(df_sus_crrnt[fne609])) * 100))
ratio_sus_crrnt_09_2 = int(round((len(freq_sus_crrnt_09_2) / len(df_sus_crrnt[fne609])) * 100))
ratio_sus_crrnt_09_3 = int(round((len(freq_sus_crrnt_09_3) / len(df_sus_crrnt[fne609])) * 100))
ratio_sus_crrnt_09_4 = int(round((len(freq_sus_crrnt_09_4) / len(df_sus_crrnt[fne609])) * 100))
ratio_sus_crrnt_09_5 = int(round((len(freq_sus_crrnt_09_5) / len(df_sus_crrnt[fne609])) * 100))

ratio_sus_crrnt_10_1 = int(round((len(freq_sus_crrnt_10_1) / len(df_sus_crrnt[fne610])) * 100))
ratio_sus_crrnt_10_2 = int(round((len(freq_sus_crrnt_10_2) / len(df_sus_crrnt[fne610])) * 100))
ratio_sus_crrnt_10_3 = int(round((len(freq_sus_crrnt_10_3) / len(df_sus_crrnt[fne610])) * 100))
ratio_sus_crrnt_10_4 = int(round((len(freq_sus_crrnt_10_4) / len(df_sus_crrnt[fne610])) * 100))
ratio_sus_crrnt_10_5 = int(round((len(freq_sus_crrnt_10_5) / len(df_sus_crrnt[fne610])) * 100))

arr_ratio_sus_crrnt_01 = [ratio_sus_crrnt_01_1,
                          ratio_sus_crrnt_01_2,
                          ratio_sus_crrnt_01_3,
                          ratio_sus_crrnt_01_4,
                          ratio_sus_crrnt_01_5]

arr_ratio_sus_crrnt_02 = [ratio_sus_crrnt_02_1,
                          ratio_sus_crrnt_02_2,
                          ratio_sus_crrnt_02_3,
                          ratio_sus_crrnt_02_4,
                          ratio_sus_crrnt_02_5]


arr_ratio_sus_crrnt_03 = [ratio_sus_crrnt_03_1,
                          ratio_sus_crrnt_03_2,
                          ratio_sus_crrnt_03_3,
                          ratio_sus_crrnt_03_4,
                          ratio_sus_crrnt_03_5]

arr_ratio_sus_crrnt_04 = [ratio_sus_crrnt_04_1,
                          ratio_sus_crrnt_04_2,
                          ratio_sus_crrnt_04_3,
                          ratio_sus_crrnt_04_4,
                          ratio_sus_crrnt_04_5]

arr_ratio_sus_crrnt_01 = [ratio_sus_crrnt_01_1,
                          ratio_sus_crrnt_01_2,
                          ratio_sus_crrnt_01_3,
                          ratio_sus_crrnt_01_4,
                          ratio_sus_crrnt_01_5]


arr_ratio_sus_crrnt_05 = [ratio_sus_crrnt_05_1,
                          ratio_sus_crrnt_05_2,
                          ratio_sus_crrnt_05_3,
                          ratio_sus_crrnt_05_4,
                          ratio_sus_crrnt_05_5]

arr_ratio_sus_crrnt_06 = [ratio_sus_crrnt_06_1,
                          ratio_sus_crrnt_06_2,
                          ratio_sus_crrnt_06_3,
                          ratio_sus_crrnt_06_4,
                          ratio_sus_crrnt_06_5]

arr_ratio_sus_crrnt_07 = [ratio_sus_crrnt_07_1,
                          ratio_sus_crrnt_07_2,
                          ratio_sus_crrnt_07_3,
                          ratio_sus_crrnt_07_4,
                          ratio_sus_crrnt_07_5]


arr_ratio_sus_crrnt_08 = [ratio_sus_crrnt_08_1,
                          ratio_sus_crrnt_08_2,
                          ratio_sus_crrnt_08_3,
                          ratio_sus_crrnt_08_4,
                          ratio_sus_crrnt_08_5]

arr_ratio_sus_crrnt_09 = [ratio_sus_crrnt_09_1,
                          ratio_sus_crrnt_09_2,
                          ratio_sus_crrnt_09_3,
                          ratio_sus_crrnt_09_4,
                          ratio_sus_crrnt_09_5]


arr_ratio_sus_crrnt_10 = [ratio_sus_crrnt_10_1,
                          ratio_sus_crrnt_10_2,
                          ratio_sus_crrnt_10_3,
                          ratio_sus_crrnt_10_4,
                          ratio_sus_crrnt_10_5]

x_data_odd = [arr_ratio_sus_crrnt_09,
              arr_ratio_sus_crrnt_07,
              arr_ratio_sus_crrnt_05,
              arr_ratio_sus_crrnt_03,
              arr_ratio_sus_crrnt_01]

top_labels = ['Strongly<br>disagree',
              'Disagree',
              'Neutral',
              'Agree',
              'Strongly<br>agree']

# Odd Number Questions

colors_odd = ['rgba(192, 57, 43, 1.0)',
              'rgba(230, 126, 34, 1.0)',
              'rgba(241, 196, 15, 1.0)',
              'rgba(41, 128, 185, 1.0)',
              'rgba(39, 174, 96, 1.0)']

y_data_odd = ['msg005',
              'msg004',
              'msg003',
              'msg002',
              'msg001']

fig = go.Figure()

for i in range(0, len(x_data_odd[0])):
    for xd, yd in zip(x_data_odd, y_data_odd):
        fig.add_trace(go.Bar(
            x=[xd[i]], y=[yd],
            orientation='h',
            marker=dict(
                color=colors_odd[i],
                line=dict(color='rgb(248, 248, 249)', width=1)
            )
        ))

fig.update_layout(
    xaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
        domain=[0.15, 1]
    ),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
    ),
    barmode='stack',
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
    margin=dict(l=120, r=10, t=140, b=80),
    showlegend=False,
)

annotations = []

for yd, xd in zip(y_data_odd, x_data_odd):
    # labeling the y-axis
    annotations.append(dict(xref='paper', yref='y',
                            x=0.14, y=yd,
                            xanchor='right',
                            text=str(yd),
                            font=dict(family='Arial', size=12,
                                      color='rgb(67, 67, 67)'),
                            showarrow=False, align='right'))
    # labeling the first percentage of each bar (x_axis)
    annotations.append(dict(xref='x', yref='y',
                            x=xd[0] / 2, y=yd,
                            text=str(xd[0]) + '%',
                            font=dict(family='Arial', size=12,
                                      color='rgb(248, 248, 255)'),
                            showarrow=False))
    # labeling the first Likert scale (on the top)
    if yd == y_data_odd[-1]:
        annotations.append(dict(xref='x', yref='paper',
                                x=xd[0] / 2, y=1.1,
                                text=top_labels[0],
                                font=dict(family='Arial', size=12,
                                          color='rgb(67, 67, 67)'),
                                showarrow=False))
    space = xd[0]
    for i in range(1, len(xd)):
            # labeling the rest of percentages for each bar (x_axis)
            annotations.append(dict(xref='x', yref='y',
                                    x=space + (xd[i]/2), y=yd,
                                    text=str(xd[i]) + '%',
                                    font=dict(family='Arial', size=12,
                                              color='rgb(248, 248, 255)'),
                                    showarrow=False))
            # labeling the Likert scale
            if yd == y_data_odd[-1]:
                annotations.append(dict(xref='x', yref='paper',
                                        x=space + (xd[i]/2), y=1.1,
                                        text=top_labels[i],
                                        font=dict(family='Arial', size=12,
                                                  color='rgb(67, 67, 67)'),
                                        showarrow=False))
            space += xd[i]

fig.update_layout(annotations=annotations)

fig.show()

# figBirads = go.Figure(data=dataBirads_df, layout=layoutBirads)
# py.plot(figBirads, filename = "birads_variation_sd")

# ++++++++++++++++++++++++++++++++++++++++++++++ #

# Even Number Questions

# TODO

# ++++++++++++++++ Assistant +++++++++++++++++++ #

# Odd Number Questions

# TODO

# Even Number Questions

# TODO

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# +++++++++++++++++ END SUS ++++++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                                                #
#                       UTA4                     #
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
#             SUS: Grouped Box Plots             #
# ============================================== #

# x = datafile_vec
# x_fs = datafile_fs_vec
# x_fm = datafile_fm_vec

# trace_fs_intern = go.Box(
#   y=lg_fs_sus_intern,
#   x=varReplacer_fs_intern,
#   name='SM: Intern',
#   boxpoints = False,
#   marker=dict(
#     color='#1E824C'
#   )
# )

# trace_fm_intern = go.Box(
#   y=lg_fm_sus_intern,
#   x=varReplacer_fm_intern,
#   name='MM: Intern',
#   boxpoints = False,
#   marker=dict(
#     color='#049372'
#   )
# )

# trace_fs_junior = go.Box(
#   y=lg_fs_sus_junior,
#   x=varReplacer_fs_junior,
#   name='SM: Junior',
#   boxpoints = False,
#   marker=dict(
#     color='#663399'
#   )
# )

# trace_fm_junior = go.Box(
#   y=lg_fm_sus_junior,
#   x=varReplacer_fm_junior,
#   name='MM: Junior',
#   boxpoints = False,
#   marker=dict(
#     color='#913D88'
#   )
# )

# trace_fs_middle = go.Box(
#   y=lg_fs_sus_middle,
#   x=varReplacer_fs_middle,
#   name='SM: Middle',
#   boxpoints = False,
#   marker=dict(
#     color='#4183D7'
#   )
# )

# trace_fm_middle = go.Box(
#   y=lg_fm_sus_middle,
#   x=varReplacer_fm_middle,
#   name='MM: Middle',
#   boxpoints = False,
#   marker=dict(
#     color='#59ABE3'
#   )
# )

# trace_fs_senior = go.Box(
#   y=lg_fs_sus_senior,
#   x=varReplacer_fs_senior,
#   name='SM: Senior',
#   boxpoints = False,
#   marker=dict(
#     color='#F22613'
#   )
# )

# trace_fm_senior = go.Box(
#   y=lg_fm_sus_senior,
#   x=varReplacer_fm_senior,
#   name='MM: Senior',
#   boxpoints = False,
#   marker=dict(
#     color='#C0392B'
#   )
# )

# dataSus = [
#   trace_fs_intern,
#   trace_fm_intern,
#   trace_fs_junior,
#   trace_fm_junior,
#   trace_fs_middle,
#   trace_fm_middle,
#   trace_fs_senior,
#   trace_fm_senior
# ]

# layoutSus = go.Layout(
#   yaxis=dict(
#     title='SUS Scores',
#     titlefont=dict(
#       size=24
#     ),
#     tickfont=dict(
#       size=14
#     ),
#     zeroline=False
#   ),
#   xaxis=dict(
#     title='SUS Questions',
#     titlefont=dict(
#       size=24
#     ),
#     tickfont=dict(
#       size=14
#     ),
#     zeroline=False
#   ),
#   legend=dict(
#     font=dict(
#       size=18
#     )
#   ),
#   boxmode='group',
#   width=1000,
#   height=500,
#   boxgap=0.05,
#   boxgroupgap=0.25,
# )

# figSus = go.Figure(data=dataSus, layout=layoutSus)
# py.plot(figSus, filename = "sus_scores_vs_sus_questions")

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

# trace0 = go.Box(
#   y=gt_fs_birads_94662_list,
#   name=sm_birads_labels[0],
#   boxpoints = False,
#   marker=dict(
#     color='rgb(26, 188, 156)',
#   ),
#   boxmean='sd'
# )

# trace1 = go.Box(
#   y=gt_fm_birads_94662_list,
#   name=mm_birads_labels[0],
#   boxpoints = False,
#   marker=dict(
#     color='rgb(22, 160, 133)',
#   ),
#   boxmean='sd'
# )

# trace2 = go.Box(
#   y=gt_fm_assis_94662_list,
#   name=mm_assis_labels[0],
#   boxpoints = False,
#   marker=dict(
#     color='rgb(18, 160, 133)',
#   ),
#   boxmean='sd'
# )

# trace3 = go.Box(
#   y=gt_fs_birads_607376_list,
#   name=sm_birads_labels[1],
#   boxpoints = False,
#   marker=dict(
#     color='rgb(52, 152, 219)',
#   ),
#   boxmean='sd'
# )

# trace4 = go.Box(
#   y=gt_fm_birads_607376_list,
#   name=mm_birads_labels[1],
#   boxpoints = False,
#   marker=dict(
#     color='rgb(41, 128, 185)',
#   ),
#   boxmean='sd'
# )

# trace5 = go.Box(
#   y=gt_fm_assis_607376_list,
#   name=mm_assis_labels[1],
#   boxpoints = False,
#   marker=dict(
#     color='rgb(38, 92, 131)',
#   ),
#   boxmean='sd'
# )

# trace6 = go.Box(
#   y=gt_fs_birads_737037_list,
#   name=sm_birads_labels[2],
#   boxpoints = False,
#   marker=dict(
#     color='rgb(155, 89, 182)',
#   ),
#   boxmean='sd'
# )

# trace7 = go.Box(
#   y=gt_fm_birads_737037_list,
#   name=mm_birads_labels[2],
#   boxpoints = False,
#   marker=dict(
#     color='rgb(142, 68, 173)',
#   ),
#   boxmean='sd'
# )

# trace8 = go.Box(
#   y=gt_fm_assis_737037_list,
#   name=mm_assis_labels[2],
#   boxpoints = False,
#   marker=dict(
#     color='rgb(137, 47, 164)',
#   ),
#   boxmean='sd'
# )

# trace0_df = go.Box(
#   y=df_fs_birads_94662_list,
#   name=sm_birads_labels[0],
#   boxpoints = False,
#   marker=dict(
#     color='rgb(26, 188, 156)',
#   ),
#   boxmean='sd'
# )

# trace1_df = go.Box(
#   y=df_fm_birads_94662_list,
#   name=mm_birads_labels[0],
#   boxpoints = False,
#   marker=dict(
#     color='rgb(22, 160, 133)',
#   ),
#   boxmean='sd'
# )

# trace2_df = go.Box(
#   y=df_fm_assis_94662_list,
#   name=mm_assis_labels[0],
#   boxpoints = False,
#   marker=dict(
#     color='rgb(18, 160, 133)',
#   ),
#   boxmean='sd'
# )

# trace3_df = go.Box(
#   y=df_fs_birads_607376_list,
#   name=sm_birads_labels[1],
#   boxpoints = False,
#   marker=dict(
#     color='rgb(52, 152, 219)',
#   ),
#   boxmean='sd'
# )

# trace4_df = go.Box(
#   y=df_fm_birads_607376_list,
#   name=mm_birads_labels[1],
#   boxpoints = False,
#   marker=dict(
#     color='rgb(41, 128, 185)',
#   ),
#   boxmean='sd'
# )

# trace5_df = go.Box(
#   y=df_fm_assis_607376_list,
#   name=mm_assis_labels[1],
#   boxpoints = False,
#   marker=dict(
#     color='rgb(38, 92, 131)',
#   ),
#   boxmean='sd'
# )

# trace6_df = go.Box(
#   y=df_fs_birads_737037_list,
#   name=sm_birads_labels[2],
#   boxpoints = False,
#   marker=dict(
#     color='rgb(155, 89, 182)',
#   ),
#   boxmean='sd'
# )

# trace7_df = go.Box(
#   y=df_fm_birads_737037_list,
#   name=mm_birads_labels[2],
#   boxpoints = False,
#   marker=dict(
#     color='rgb(142, 68, 173)',
#   ),
#   boxmean='sd'
# )

# trace8_df = go.Box(
#   y=df_fm_assis_737037_list,
#   name=mm_assis_labels[2],
#   boxpoints = False,
#   marker=dict(
#     color='rgb(137, 47, 164)',
#   ),
#   boxmean='sd'
# )

# dataBirads = [
#   trace0,
#   trace1,
#   trace2,
#   trace3,
#   trace4,
#   trace5,
#   trace6,
#   trace7,
#   trace8
# ]

# dataBirads_df = [
#   trace0_df,
#   trace1_df,
#   trace2_df,
#   trace3_df,
#   trace4_df,
#   trace5_df,
#   trace6_df,
#   trace7_df,
#   trace8_df
# ]

# layoutBirads = go.Layout(
#   title = "BIRADS Variation & SD",
#   xaxis = dict(
#     titlefont=dict(
#       size=24
#     ),
#     tickfont=dict(
#       size=14
#     ),
#   ),
#   yaxis = dict(
#     titlefont=dict(
#       size=24
#     ),
#     tickfont=dict(
#       size=14
#     ),
#   ),
#   legend=dict(
#     font=dict(
#       size=18
#     )
#   ),
#   width=1000,
#   height=500,
#   boxgap=0.05,
#   boxgroupgap=0.25,
# )

# layoutBirads2 = go.Layout(
#   title = "BIRADS Variation & SD",
#   xaxis = dict(
#     titlefont=dict(
#       size=24
#     ),
#     tickfont=dict(
#       size=14
#     ),
#   ),
#   yaxis = dict(
#     titlefont=dict(
#       size=24
#     ),
#     tickfont=dict(
#       size=14
#     ),
#   ),
#   legend=dict(
#     font=dict(
#       size=18
#     )
#   )
# )

# figBirads = go.Figure(data=dataBirads, layout=layoutBirads)
# py.plot(figBirads, filename = "birads_variation_sd")

# figBirads = go.Figure(data=dataBirads_df, layout=layoutBirads)
# py.plot(figBirads, filename = "birads_variation_sd")

# figBirads = go.Figure(data=dataBirads, layout=layoutBirads2)
# py.plot(figBirads, filename = "birads_variation_sd")

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ==================== END File ==================== #
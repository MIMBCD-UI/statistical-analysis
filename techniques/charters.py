#!/usr/bin/env python

""".py: """

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

techniques_dir = (pathAbsPath + '/sheet-reader/techniques/')


sys.path.append(techniques_dir)

from measures import *

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
  name = sm_birads_labels[0],
  marker=dict(
    color='rgb(26, 188, 156)',
  )
)

trace1 = go.Scatter(
  x = mm_time_94662_charted,
  y = mm_clicks_94662_charted,
  mode = 'markers',
  name = mm_birads_labels[0],
  marker=dict(
    color='rgb(243, 156, 18)',
  )
)

trace2 = go.Scatter(
  x = sm_time_607376_charted,
  y = sm_clicks_607376_charted,
  mode = 'markers',
  name = sm_birads_labels[1],
  marker=dict(
    color='rgb(52, 152, 219)',
  )
)

trace3 = go.Scatter(
  x = mm_time_607376_charted,
  y = mm_clicks_607376_charted,
  mode = 'markers',
  name = mm_birads_labels[1],
  marker=dict(
    color='rgb(192, 57, 43)',
  )
)

trace4 = go.Scatter(
  x = sm_time_737037_charted,
  y = sm_clicks_737037_charted,
  mode = 'markers',
  name = sm_birads_labels[2],
  marker=dict(
    color='rgb(155, 89, 182)',
  )
)

trace5 = go.Scatter(
  x = mm_time_737037_charted,
  y = mm_clicks_737037_charted,
  mode = 'markers',
  name = mm_birads_labels[2],
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
    dict(label = 'SM: P1 Cluster',
      method = 'relayout',
      args = ['shapes', cluster0]),
    dict(label = 'SM: P2 Cluster',
      method = 'relayout',
      args = ['shapes', cluster2]),
    dict(label = 'SM: P3 Cluster',
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
    dict(label = 'SM: P1 Cluster',
      method = 'relayout',
      args = ['shapes', cluster1]),
    dict(label = 'SM: P2 Cluster',
      method = 'relayout',
      args = ['shapes', cluster3]),
    dict(label = 'SM: P3 Cluster',
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

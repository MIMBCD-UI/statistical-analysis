#!/usr/bin/env python

"""anova.py: A python version of ANOVA."""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "ACADEMIC & COMMERCIAL"
__version__     = "1.2.3"
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

from nasa import nasaColMean
from structures import *
from dataFileGroups import *
from dataFileVectors import *
from listGroupStructures import *
from conditions import *
from listGroups import *

import main_variables
import sheets
import special
import sheetReaders
import iterators
import replacers
import ploters

MV_N = main_variables.N
s_Number = special.s_Number
datafileIteratorPerGroup = iterators.datafileIteratorPerGroup
vecReplacer = replacers.vecReplacer
vecReplacePrinter = replacers.vecReplacePrinter

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

# ============================================== #
#                                                #
#                     ANOVA                      #
#                                                #
# ============================================== #

# ============================================== #
#            NASA-TLX: Mental Demand             #
# ============================================== #

F_fs_md, p_fs_md = stats.f_oneway(
  d_data_fs_md['intern'],
  d_data_fs_md['junior'],
  d_data_fs_md['middle'],
  d_data_fs_md['senior']
)

F_fm_md, p_fm_md = stats.f_oneway(
  d_data_fm_md['intern'],
  d_data_fm_md['junior'],
  d_data_fs_md['middle'],
  d_data_fm_md['senior']
)

print("Single-Modality (Mental Demand): F = %f" % (F_fs_md))
print("Single-Modality (Mental Demand): p = %f" % (p_fs_md))
print("Multi-Modality (Mental Demand): F = %f" % (F_fm_md))
print("Multi-Modality (Mental Demand): p = %f" % (p_fm_md))

# ============================================== #
# ============================================== #

# ============================================== #
#           NASA-TLX: Physical Demand            #
# ============================================== #

F_fs_pd, p_fs_pd = stats.f_oneway(
  d_data_fs_pd['intern'],
  d_data_fs_pd['junior'],
  d_data_fs_pd['middle'],
  d_data_fs_pd['senior']
)

F_fm_pd, p_fm_pd = stats.f_oneway(
  d_data_fm_pd['intern'],
  d_data_fm_pd['junior'],
  d_data_fs_pd['middle'],
  d_data_fm_pd['senior']
)

print("Single-Modality (Physical Demand): F = %f" % (F_fs_pd))
print("Single-Modality (Physical Demand): p = %f" % (p_fs_pd))
print("Multi-Modality (Physical Demand): F = %f" % (F_fm_pd))
print("Multi-Modality (Physical Demand): p = %f" % (p_fm_pd))

# ============================================== #
# ============================================== #

# ============================================== #
#           NASA-TLX: Temporal Demand            #
# ============================================== #

F_fs_td, p_fs_td = stats.f_oneway(
  d_data_fs_td['intern'],
  d_data_fs_td['junior'],
  d_data_fs_td['middle'],
  d_data_fs_td['senior']
)

F_fm_td, p_fm_td = stats.f_oneway(
  d_data_fm_td['intern'],
  d_data_fm_td['junior'],
  d_data_fs_td['middle'],
  d_data_fm_td['senior']
)

print("Single-Modality (Temporal Demand): F = %f" % (F_fs_td))
print("Single-Modality (Temporal Demand): p = %f" % (p_fs_td))
print("Multi-Modality (Temporal Demand): F = %f" % (F_fm_td))
print("Multi-Modality (Temporal Demand): p = %f" % (p_fm_td))

# ============================================== #
# ============================================== #

# ============================================== #
#             NASA-TLX: Performance              #
# ============================================== #

F_fs_p, p_fs_p = stats.f_oneway(
  d_data_fs_p['intern'],
  d_data_fs_p['junior'],
  d_data_fs_p['middle'],
  d_data_fs_p['senior']
)

F_fm_p, p_fm_p = stats.f_oneway(
  d_data_fm_p['intern'],
  d_data_fm_p['junior'],
  d_data_fs_p['middle'],
  d_data_fm_p['senior']
)

print("Single-Modality (Performance): F = %f" % (F_fs_p))
print("Single-Modality (Performance): p = %f" % (p_fs_p))
print("Multi-Modality (Performance): F = %f" % (F_fm_p))
print("Multi-Modality (Performance): p = %f" % (p_fm_p))

# ============================================== #
# ============================================== #

# ============================================== #
#                NASA-TLX: Effort                #
# ============================================== #

F_fs_e, p_fs_e = stats.f_oneway(
  d_data_fs_e['intern'],
  d_data_fs_e['junior'],
  d_data_fs_e['middle'],
  d_data_fs_e['senior']
)

F_fm_e, p_fm_e = stats.f_oneway(
  d_data_fm_e['intern'],
  d_data_fm_e['junior'],
  d_data_fs_e['middle'],
  d_data_fm_e['senior']
)

print("Single-Modality (Effort): F = %f" % (F_fs_e))
print("Single-Modality (Effort): p = %f" % (p_fs_e))
print("Multi-Modality (Effort): F = %f" % (F_fm_e))
print("Multi-Modality (Effort): p = %f" % (p_fm_e))

# ============================================== #
# ============================================== #

# ============================================== #
#             NASA-TLX: Frustration              #
# ============================================== #

F_fs_f, p_fs_f = stats.f_oneway(
  d_data_fs_f['intern'],
  d_data_fs_f['junior'],
  d_data_fs_f['middle'],
  d_data_fs_f['senior']
)

F_fm_f, p_fm_f = stats.f_oneway(
  d_data_fm_f['intern'],
  d_data_fm_f['junior'],
  d_data_fs_f['middle'],
  d_data_fm_f['senior']
)

print("Single-Modality (Frustration): F = %f" % (F_fs_f))
print("Single-Modality (Frustration): p = %f" % (p_fs_f))
print("Multi-Modality (Frustration): F = %f" % (F_fm_f))
print("Multi-Modality (Frustration): p = %f" % (p_fm_f))

# ============================================== #
# ============================================== #

# ============================================== #
#                    SUS: 1                      #
# ============================================== #

F_fs_sus_01, p_fs_sus_01 = stats.f_oneway(
  d_data_fs_sus_01['intern'],
  d_data_fs_sus_01['junior'],
  d_data_fs_sus_01['middle'],
  d_data_fs_sus_01['senior']
)

F_fm_sus_01, p_fm_sus_01 = stats.f_oneway(
  d_data_fm_sus_01['intern'],
  d_data_fm_sus_01['junior'],
  d_data_fm_sus_01['middle'],
  d_data_fm_sus_01['senior']
)

print("Single-Modality (SUS_01): F = %f" % (F_fs_sus_01))
print("Single-Modality (SUS_01): p = %f" % (p_fs_sus_01))
print("Multi-Modality (SUS_01): F = %f" % (F_fm_sus_01))
print("Multi-Modality (SUS_01): p = %f" % (p_fm_sus_01))

# ============================================== #
# ============================================== #

# ============================================== #
#                    SUS: 2                      #
# ============================================== #

F_fs_sus_02, p_fs_sus_02 = stats.f_oneway(
  d_data_fs_sus_02['intern'],
  d_data_fs_sus_02['junior'],
  d_data_fs_sus_02['middle'],
  d_data_fs_sus_02['senior']
)

F_fm_sus_02, p_fm_sus_02 = stats.f_oneway(
  d_data_fm_sus_02['intern'],
  d_data_fm_sus_02['junior'],
  d_data_fm_sus_02['middle'],
  d_data_fm_sus_02['senior']
)

print("Single-Modality (SUS_02): F = %f" % (F_fs_sus_02))
print("Single-Modality (SUS_02): p = %f" % (p_fs_sus_02))
print("Multi-Modality (SUS_02): F = %f" % (F_fm_sus_02))
print("Multi-Modality (SUS_02): p = %f" % (p_fm_sus_02))

# ============================================== #
# ============================================== #

# ============================================== #
#                    SUS: 3                      #
# ============================================== #

F_fs_sus_03, p_fs_sus_03 = stats.f_oneway(
  d_data_fs_sus_03['intern'],
  d_data_fs_sus_03['junior'],
  d_data_fs_sus_03['middle'],
  d_data_fs_sus_03['senior']
)

F_fm_sus_03, p_fm_sus_03 = stats.f_oneway(
  d_data_fm_sus_03['intern'],
  d_data_fm_sus_03['junior'],
  d_data_fm_sus_03['middle'],
  d_data_fm_sus_03['senior']
)

print("Single-Modality (SUS_03): F = %f" % (F_fs_sus_03))
print("Single-Modality (SUS_03): p = %f" % (p_fs_sus_03))
print("Multi-Modality (SUS_03): F = %f" % (F_fm_sus_03))
print("Multi-Modality (SUS_03): p = %f" % (p_fm_sus_03))

# ============================================== #
# ============================================== #

# ============================================== #
#                    SUS: 4                      #
# ============================================== #

F_fs_sus_04, p_fs_sus_04 = stats.f_oneway(
  d_data_fs_sus_04['intern'],
  d_data_fs_sus_04['junior'],
  d_data_fs_sus_04['middle'],
  d_data_fs_sus_04['senior']
)

F_fm_sus_04, p_fm_sus_04 = stats.f_oneway(
  d_data_fm_sus_04['intern'],
  d_data_fm_sus_04['junior'],
  d_data_fm_sus_04['middle'],
  d_data_fm_sus_04['senior']
)

print("Single-Modality (SUS_04): F = %f" % (F_fs_sus_04))
print("Single-Modality (SUS_04): p = %f" % (p_fs_sus_04))
print("Multi-Modality (SUS_04): F = %f" % (F_fm_sus_04))
print("Multi-Modality (SUS_04): p = %f" % (p_fm_sus_04))

# ============================================== #
# ============================================== #

# ============================================== #
#                    SUS: 5                      #
# ============================================== #

F_fs_sus_05, p_fs_sus_05 = stats.f_oneway(
  d_data_fs_sus_05['intern'],
  d_data_fs_sus_05['junior'],
  d_data_fs_sus_05['middle'],
  d_data_fs_sus_05['senior']
)

F_fm_sus_05, p_fm_sus_05 = stats.f_oneway(
  d_data_fm_sus_05['intern'],
  d_data_fm_sus_05['junior'],
  d_data_fm_sus_05['middle'],
  d_data_fm_sus_05['senior']
)

print("Single-Modality (SUS_05): F = %f" % (F_fs_sus_05))
print("Single-Modality (SUS_05): p = %f" % (p_fs_sus_05))
print("Multi-Modality (SUS_05): F = %f" % (F_fm_sus_05))
print("Multi-Modality (SUS_05): p = %f" % (p_fm_sus_05))

# ============================================== #
# ============================================== #

# ============================================== #
#                    SUS: 6                      #
# ============================================== #

F_fs_sus_06, p_fs_sus_06 = stats.f_oneway(
  d_data_fs_sus_06['intern'],
  d_data_fs_sus_06['junior'],
  d_data_fs_sus_06['middle'],
  d_data_fs_sus_06['senior']
)

F_fm_sus_06, p_fm_sus_06 = stats.f_oneway(
  d_data_fm_sus_06['intern'],
  d_data_fm_sus_06['junior'],
  d_data_fm_sus_06['middle'],
  d_data_fm_sus_06['senior']
)

print("Single-Modality (SUS_06): F = %f" % (F_fs_sus_06))
print("Single-Modality (SUS_06): p = %f" % (p_fs_sus_06))
print("Multi-Modality (SUS_06): F = %f" % (F_fm_sus_06))
print("Multi-Modality (SUS_06): p = %f" % (p_fm_sus_06))

# ============================================== #
# ============================================== #

# ============================================== #
#                    SUS: 7                      #
# ============================================== #

F_fs_sus_07, p_fs_sus_07 = stats.f_oneway(
  d_data_fs_sus_07['intern'],
  d_data_fs_sus_07['junior'],
  d_data_fs_sus_07['middle'],
  d_data_fs_sus_07['senior']
)

F_fm_sus_07, p_fm_sus_07 = stats.f_oneway(
  d_data_fm_sus_07['intern'],
  d_data_fm_sus_07['junior'],
  d_data_fm_sus_07['middle'],
  d_data_fm_sus_07['senior']
)

print("Single-Modality (SUS_07): F = %f" % (F_fs_sus_07))
print("Single-Modality (SUS_07): p = %f" % (p_fs_sus_07))
print("Multi-Modality (SUS_07): F = %f" % (F_fm_sus_07))
print("Multi-Modality (SUS_07): p = %f" % (p_fm_sus_07))

# ============================================== #
# ============================================== #

# ============================================== #
#                    SUS: 8                      #
# ============================================== #

F_fs_sus_08, p_fs_sus_08 = stats.f_oneway(
  d_data_fs_sus_08['intern'],
  d_data_fs_sus_08['junior'],
  d_data_fs_sus_08['middle'],
  d_data_fs_sus_08['senior']
)

F_fm_sus_08, p_fm_sus_08 = stats.f_oneway(
  d_data_fm_sus_08['intern'],
  d_data_fm_sus_08['junior'],
  d_data_fm_sus_08['middle'],
  d_data_fm_sus_08['senior']
)

print("Single-Modality (SUS_08): F = %f" % (F_fs_sus_08))
print("Single-Modality (SUS_08): p = %f" % (p_fs_sus_08))
print("Multi-Modality (SUS_08): F = %f" % (F_fm_sus_08))
print("Multi-Modality (SUS_08): p = %f" % (p_fm_sus_08))

# ============================================== #
# ============================================== #

# ============================================== #
#                    SUS: 9                      #
# ============================================== #

F_fs_sus_09, p_fs_sus_09 = stats.f_oneway(
  d_data_fs_sus_09['intern'],
  d_data_fs_sus_09['junior'],
  d_data_fs_sus_09['middle'],
  d_data_fs_sus_09['senior']
)

F_fm_sus_09, p_fm_sus_09 = stats.f_oneway(
  d_data_fm_sus_09['intern'],
  d_data_fm_sus_09['junior'],
  d_data_fm_sus_09['middle'],
  d_data_fm_sus_09['senior']
)

print("Single-Modality (SUS_09): F = %f" % (F_fs_sus_09))
print("Single-Modality (SUS_09): p = %f" % (p_fs_sus_09))
print("Multi-Modality (SUS_09): F = %f" % (F_fm_sus_09))
print("Multi-Modality (SUS_09): p = %f" % (p_fm_sus_09))

# ============================================== #
# ============================================== #

# ============================================== #
#                    SUS: 10                     #
# ============================================== #

F_fs_sus_10, p_fs_sus_10 = stats.f_oneway(
  d_data_fs_sus_10['intern'],
  d_data_fs_sus_10['junior'],
  d_data_fs_sus_10['middle'],
  d_data_fs_sus_10['senior']
)

F_fm_sus_10, p_fm_sus_10 = stats.f_oneway(
  d_data_fm_sus_10['intern'],
  d_data_fm_sus_10['junior'],
  d_data_fm_sus_10['middle'],
  d_data_fm_sus_10['senior']
)

print("Single-Modality (SUS_10): F = %f" % (F_fs_sus_10))
print("Single-Modality (SUS_10): p = %f" % (p_fs_sus_10))
print("Multi-Modality (SUS_10): F = %f" % (F_fm_sus_10))
print("Multi-Modality (SUS_10): p = %f" % (p_fm_sus_10))

# ============================================== #
# ============================================== #

# ============================================== #
#                   SUS: TOTAL                   #
# ============================================== #

F_fs_sus_total, p_fs_sus_total = stats.f_oneway(
  d_data_fs_sus_01['intern'],
  d_data_fs_sus_01['junior'],
  d_data_fs_sus_01['middle'],
  d_data_fs_sus_01['senior'],
  d_data_fs_sus_02['intern'],
  d_data_fs_sus_02['junior'],
  d_data_fs_sus_02['middle'],
  d_data_fs_sus_02['senior'],
  d_data_fs_sus_03['intern'],
  d_data_fs_sus_03['junior'],
  d_data_fs_sus_03['middle'],
  d_data_fs_sus_03['senior'],
  d_data_fs_sus_04['intern'],
  d_data_fs_sus_04['junior'],
  d_data_fs_sus_04['middle'],
  d_data_fs_sus_04['senior'],
  d_data_fs_sus_05['intern'],
  d_data_fs_sus_05['junior'],
  d_data_fs_sus_05['middle'],
  d_data_fs_sus_05['senior'],
  d_data_fs_sus_06['intern'],
  d_data_fs_sus_06['junior'],
  d_data_fs_sus_06['middle'],
  d_data_fs_sus_06['senior'],
  d_data_fs_sus_07['intern'],
  d_data_fs_sus_07['junior'],
  d_data_fs_sus_07['middle'],
  d_data_fs_sus_07['senior'],
  d_data_fs_sus_08['intern'],
  d_data_fs_sus_08['junior'],
  d_data_fs_sus_08['middle'],
  d_data_fs_sus_08['senior'],
  d_data_fs_sus_09['intern'],
  d_data_fs_sus_09['junior'],
  d_data_fs_sus_09['middle'],
  d_data_fs_sus_09['senior'],
  d_data_fs_sus_10['intern'],
  d_data_fs_sus_10['junior'],
  d_data_fs_sus_10['middle'],
  d_data_fs_sus_10['senior']
)

F_fm_sus_total, p_fm_sus_total = stats.f_oneway(
  d_data_fm_sus_01['intern'],
  d_data_fm_sus_01['junior'],
  d_data_fm_sus_01['middle'],
  d_data_fm_sus_01['senior'],
  d_data_fm_sus_02['intern'],
  d_data_fm_sus_02['junior'],
  d_data_fm_sus_02['middle'],
  d_data_fm_sus_02['senior'],
  d_data_fm_sus_03['intern'],
  d_data_fm_sus_03['junior'],
  d_data_fm_sus_03['middle'],
  d_data_fm_sus_03['senior'],
  d_data_fm_sus_04['intern'],
  d_data_fm_sus_04['junior'],
  d_data_fm_sus_04['middle'],
  d_data_fm_sus_04['senior'],
  d_data_fm_sus_05['intern'],
  d_data_fm_sus_05['junior'],
  d_data_fm_sus_05['middle'],
  d_data_fm_sus_05['senior'],
  d_data_fm_sus_06['intern'],
  d_data_fm_sus_06['junior'],
  d_data_fm_sus_06['middle'],
  d_data_fm_sus_06['senior'],
  d_data_fm_sus_07['intern'],
  d_data_fm_sus_07['junior'],
  d_data_fm_sus_07['middle'],
  d_data_fm_sus_07['senior'],
  d_data_fm_sus_08['intern'],
  d_data_fm_sus_08['junior'],
  d_data_fm_sus_08['middle'],
  d_data_fm_sus_08['senior'],
  d_data_fm_sus_09['intern'],
  d_data_fm_sus_09['junior'],
  d_data_fm_sus_09['middle'],
  d_data_fm_sus_09['senior'],
  d_data_fm_sus_10['intern'],
  d_data_fm_sus_10['junior'],
  d_data_fm_sus_10['middle'],
  d_data_fm_sus_10['senior']
)

print("Single-Modality (SUS_TOTAL): F = %f" % (F_fs_sus_total))
print("Single-Modality (SUS_TOTAL): p = %f" % (p_fs_sus_total))
print("Multi-Modality (SUS_TOTAL): F = %f" % (F_fm_sus_total))
print("Multi-Modality (SUS_TOTAL): p = %f" % (p_fm_sus_total))

# ============================================== #
# ============================================== #

# ============================================== #
#                  TIME: 94662                   #
# ============================================== #

F_fs_time_94662, p_fs_time_94662 = stats.f_oneway(
  d_data_fs_time_94662['intern'],
  d_data_fs_time_94662['junior'],
  d_data_fs_time_94662['middle'],
  d_data_fs_time_94662['senior']
)

F_fm_time_94662, p_fm_time_94662 = stats.f_oneway(
  d_data_fm_time_94662['intern'],
  d_data_fm_time_94662['junior'],
  d_data_fm_time_94662['middle'],
  d_data_fm_time_94662['senior']
)

print("Single-Modality (time_94662): F = %f" % (F_fs_time_94662))
print("Single-Modality (time_94662): p = %f" % (p_fs_time_94662))
print("Multi-Modality (time_94662): F = %f" % (F_fm_time_94662))
print("Multi-Modality (time_94662): p = %f" % (p_fm_time_94662))

# ============================================== #
# ============================================== #

# ============================================== #
#                 TIME: 607376                   #
# ============================================== #

F_fs_time_607376, p_fs_time_607376 = stats.f_oneway(
  d_data_fs_time_607376['intern'],
  d_data_fs_time_607376['junior'],
  d_data_fs_time_607376['middle'],
  d_data_fs_time_607376['senior']
)

F_fm_time_607376, p_fm_time_607376 = stats.f_oneway(
  d_data_fm_time_607376['intern'],
  d_data_fm_time_607376['junior'],
  d_data_fm_time_607376['middle'],
  d_data_fm_time_607376['senior']
)

print("Single-Modality (time_607376): F = %f" % (F_fs_time_607376))
print("Single-Modality (time_607376): p = %f" % (p_fs_time_607376))
print("Multi-Modality (time_607376): F = %f" % (F_fm_time_607376))
print("Multi-Modality (time_607376): p = %f" % (p_fm_time_607376))

# ============================================== #
# ============================================== #

# ============================================== #
#                 TIME: 737037                   #
# ============================================== #

F_fs_time_737037, p_fs_time_737037 = stats.f_oneway(
  d_data_fs_time_737037['intern'],
  d_data_fs_time_737037['junior'],
  d_data_fs_time_737037['middle'],
  d_data_fs_time_737037['senior']
)

F_fm_time_737037, p_fm_time_737037 = stats.f_oneway(
  d_data_fm_time_737037['intern'],
  d_data_fm_time_737037['junior'],
  d_data_fm_time_737037['middle'],
  d_data_fm_time_737037['senior']
)

print("Single-Modality (time_737037): F = %f" % (F_fs_time_737037))
print("Single-Modality (time_737037): p = %f" % (p_fs_time_737037))
print("Multi-Modality (time_737037): F = %f" % (F_fm_time_737037))
print("Multi-Modality (time_737037): p = %f" % (p_fm_time_737037))

# ============================================== #
# ============================================== #

# ============================================== #
#                  TIME: total                   #
# ============================================== #

F_fs_time_total, p_fs_time_total = stats.f_oneway(
  d_data_fs_time_total['intern'],
  d_data_fs_time_total['junior'],
  d_data_fs_time_total['middle'],
  d_data_fs_time_total['senior']
)

F_fm_time_total, p_fm_time_total = stats.f_oneway(
  d_data_fm_time_total['intern'],
  d_data_fm_time_total['junior'],
  d_data_fm_time_total['middle'],
  d_data_fm_time_total['senior']
)

print("Single-Modality (time_total): F = %f" % (F_fs_time_total))
print("Single-Modality (time_total): p = %f" % (p_fs_time_total))
print("Multi-Modality (time_total): F = %f" % (F_fm_time_total))
print("Multi-Modality (time_total): p = %f" % (p_fm_time_total))

# ============================================== #
# ============================================== #

# ============================================== #
#                CLICKS: 94662                   #
# ============================================== #

F_fs_clicks_94662, p_fs_clicks_94662 = stats.f_oneway(
  d_data_fs_clicks_94662['intern'],
  d_data_fs_clicks_94662['junior'],
  d_data_fs_clicks_94662['middle'],
  d_data_fs_clicks_94662['senior']
)

F_fm_clicks_94662, p_fm_clicks_94662 = stats.f_oneway(
  d_data_fm_clicks_94662['intern'],
  d_data_fm_clicks_94662['junior'],
  d_data_fm_clicks_94662['middle'],
  d_data_fm_clicks_94662['senior']
)

print("Single-Modality (clicks_94662): F = %f" % (F_fs_clicks_94662))
print("Single-Modality (clicks_94662): p = %f" % (p_fs_clicks_94662))
print("Multi-Modality (clicks_94662): F = %f" % (F_fm_clicks_94662))
print("Multi-Modality (clicks_94662): p = %f" % (p_fm_clicks_94662))

# ============================================== #
# ============================================== #

# ============================================== #
#               CLICKS: 607376                   #
# ============================================== #

F_fs_clicks_607376, p_fs_clicks_607376 = stats.f_oneway(
  d_data_fs_clicks_607376['intern'],
  d_data_fs_clicks_607376['junior'],
  d_data_fs_clicks_607376['middle'],
  d_data_fs_clicks_607376['senior']
)

F_fm_clicks_607376, p_fm_clicks_607376 = stats.f_oneway(
  d_data_fm_clicks_607376['intern'],
  d_data_fm_clicks_607376['junior'],
  d_data_fm_clicks_607376['middle'],
  d_data_fm_clicks_607376['senior']
)

print("Single-Modality (clicks_607376): F = %f" % (F_fs_clicks_607376))
print("Single-Modality (clicks_607376): p = %f" % (p_fs_clicks_607376))
print("Multi-Modality (clicks_607376): F = %f" % (F_fm_clicks_607376))
print("Multi-Modality (clicks_607376): p = %f" % (p_fm_clicks_607376))

# ============================================== #
# ============================================== #

# ============================================== #
#               CLICKS: 737037                   #
# ============================================== #

F_fs_clicks_737037, p_fs_clicks_737037 = stats.f_oneway(
  d_data_fs_clicks_737037['intern'],
  d_data_fs_clicks_737037['junior'],
  d_data_fs_clicks_737037['middle'],
  d_data_fs_clicks_737037['senior']
)

F_fm_clicks_737037, p_fm_clicks_737037 = stats.f_oneway(
  d_data_fm_clicks_737037['intern'],
  d_data_fm_clicks_737037['junior'],
  d_data_fm_clicks_737037['middle'],
  d_data_fm_clicks_737037['senior']
)

print("Single-Modality (clicks_737037): F = %f" % (F_fs_clicks_737037))
print("Single-Modality (clicks_737037): p = %f" % (p_fs_clicks_737037))
print("Multi-Modality (clicks_737037): F = %f" % (F_fm_clicks_737037))
print("Multi-Modality (clicks_737037): p = %f" % (p_fm_clicks_737037))

# ============================================== #
# ============================================== #

# ============================================== #
#                CLICKS: total                   #
# ============================================== #

F_fs_clicks_total, p_fs_clicks_total = stats.f_oneway(
  d_data_fs_clicks_total['intern'],
  d_data_fs_clicks_total['junior'],
  d_data_fs_clicks_total['middle'],
  d_data_fs_clicks_total['senior']
)

F_fm_clicks_total, p_fm_clicks_total = stats.f_oneway(
  d_data_fm_clicks_total['intern'],
  d_data_fm_clicks_total['junior'],
  d_data_fm_clicks_total['middle'],
  d_data_fm_clicks_total['senior']
)

print("Single-Modality (clicks_total): F = %f" % (F_fs_clicks_total))
print("Single-Modality (clicks_total): p = %f" % (p_fs_clicks_total))
print("Multi-Modality (clicks_total): F = %f" % (F_fm_clicks_total))
print("Multi-Modality (clicks_total): p = %f" % (p_fm_clicks_total))

# ============================================== #
# ============================================== #

# ============================================== #
#                ERRORS: 94662                   #
# ============================================== #

F_fs_errors_94662, p_fs_errors_94662 = stats.f_oneway(
  d_data_fs_errors_94662['intern'],
  d_data_fs_errors_94662['junior'],
  d_data_fs_errors_94662['middle'],
  d_data_fs_errors_94662['senior']
)

F_fm_errors_94662, p_fm_errors_94662 = stats.f_oneway(
  d_data_fm_errors_94662['intern'],
  d_data_fm_errors_94662['junior'],
  d_data_fm_errors_94662['middle'],
  d_data_fm_errors_94662['senior']
)

print("Single-Modality (errors_94662): F = %f" % (F_fs_errors_94662))
print("Single-Modality (errors_94662): p = %f" % (p_fs_errors_94662))
print("Multi-Modality (errors_94662): F = %f" % (F_fm_errors_94662))
print("Multi-Modality (errors_94662): p = %f" % (p_fm_errors_94662))

# ============================================== #
# ============================================== #

# ============================================== #
#               ERRORS: 607376                   #
# ============================================== #

F_fs_errors_607376, p_fs_errors_607376 = stats.f_oneway(
  d_data_fs_errors_607376['intern'],
  d_data_fs_errors_607376['junior'],
  d_data_fs_errors_607376['middle'],
  d_data_fs_errors_607376['senior']
)

F_fm_errors_607376, p_fm_errors_607376 = stats.f_oneway(
  d_data_fm_errors_607376['intern'],
  d_data_fm_errors_607376['junior'],
  d_data_fm_errors_607376['middle'],
  d_data_fm_errors_607376['senior']
)

print("Single-Modality (errors_607376): F = %f" % (F_fs_errors_607376))
print("Single-Modality (errors_607376): p = %f" % (p_fs_errors_607376))
print("Multi-Modality (errors_607376): F = %f" % (F_fm_errors_607376))
print("Multi-Modality (errors_607376): p = %f" % (p_fm_errors_607376))

# ============================================== #
# ============================================== #

# ============================================== #
#               ERRORS: 737037                   #
# ============================================== #

F_fs_errors_737037, p_fs_errors_737037 = stats.f_oneway(
  d_data_fs_errors_737037['intern'],
  d_data_fs_errors_737037['junior'],
  d_data_fs_errors_737037['middle'],
  d_data_fs_errors_737037['senior']
)

F_fm_errors_737037, p_fm_errors_737037 = stats.f_oneway(
  d_data_fm_errors_737037['intern'],
  d_data_fm_errors_737037['junior'],
  d_data_fm_errors_737037['middle'],
  d_data_fm_errors_737037['senior']
)

print("Single-Modality (errors_737037): F = %f" % (F_fs_errors_737037))
print("Single-Modality (errors_737037): p = %f" % (p_fs_errors_737037))
print("Multi-Modality (errors_737037): F = %f" % (F_fm_errors_737037))
print("Multi-Modality (errors_737037): p = %f" % (p_fm_errors_737037))

# ============================================== #
# ============================================== #

# ============================================== #
#                ERRORS: total                   #
# ============================================== #

F_fs_errors_total, p_fs_errors_total = stats.f_oneway(
  d_data_fs_errors_total['intern'],
  d_data_fs_errors_total['junior'],
  d_data_fs_errors_total['middle'],
  d_data_fs_errors_total['senior']
)

F_fm_errors_total, p_fm_errors_total = stats.f_oneway(
  d_data_fm_errors_total['intern'],
  d_data_fm_errors_total['junior'],
  d_data_fm_errors_total['middle'],
  d_data_fm_errors_total['senior']
)

print("Single-Modality (errors_total): F = %f" % (F_fs_errors_total))
print("Single-Modality (errors_total): p = %f" % (p_fs_errors_total))
print("Multi-Modality (errors_total): F = %f" % (F_fm_errors_total))
print("Multi-Modality (errors_total): p = %f" % (p_fm_errors_total))

# ============================================== #
# ============================================== #

# ============================================== #
#                  BIRADS: 94662                   #
# ============================================== #

F_fs_birads_94662, p_fs_birads_94662 = stats.f_oneway(
  d_data_fs_birads_94662['intern'],
  d_data_fs_birads_94662['junior'],
  d_data_fs_birads_94662['middle'],
  d_data_fs_birads_94662['senior']
)

F_fm_birads_94662, p_fm_birads_94662 = stats.f_oneway(
  d_data_fm_birads_94662['intern'],
  d_data_fm_birads_94662['junior'],
  d_data_fm_birads_94662['middle'],
  d_data_fm_birads_94662['senior']
)

print("Single-Modality (birads_94662): F = %f" % (F_fs_birads_94662))
print("Single-Modality (birads_94662): p = %f" % (p_fs_birads_94662))
print("Multi-Modality (birads_94662): F = %f" % (F_fm_birads_94662))
print("Multi-Modality (birads_94662): p = %f" % (p_fm_birads_94662))

# ============================================== #
# ============================================== #

# ============================================== #
#                 BIRADS: 607376                   #
# ============================================== #

F_fs_birads_607376, p_fs_birads_607376 = stats.f_oneway(
  d_data_fs_birads_607376['intern'],
  d_data_fs_birads_607376['junior'],
  d_data_fs_birads_607376['middle'],
  d_data_fs_birads_607376['senior']
)

F_fm_birads_607376, p_fm_birads_607376 = stats.f_oneway(
  d_data_fm_birads_607376['intern'],
  d_data_fm_birads_607376['junior'],
  d_data_fm_birads_607376['middle'],
  d_data_fm_birads_607376['senior']
)

print("Single-Modality (birads_607376): F = %f" % (F_fs_birads_607376))
print("Single-Modality (birads_607376): p = %f" % (p_fs_birads_607376))
print("Multi-Modality (birads_607376): F = %f" % (F_fm_birads_607376))
print("Multi-Modality (birads_607376): p = %f" % (p_fm_birads_607376))

# ============================================== #
# ============================================== #

# ============================================== #
#                 BIRADS: 737037                   #
# ============================================== #

F_fs_birads_737037, p_fs_birads_737037 = stats.f_oneway(
  d_data_fs_birads_737037['intern'],
  d_data_fs_birads_737037['junior'],
  d_data_fs_birads_737037['middle'],
  d_data_fs_birads_737037['senior']
)

F_fm_birads_737037, p_fm_birads_737037 = stats.f_oneway(
  d_data_fm_birads_737037['intern'],
  d_data_fm_birads_737037['junior'],
  d_data_fm_birads_737037['middle'],
  d_data_fm_birads_737037['senior']
)

print("Single-Modality (birads_737037): F = %f" % (F_fs_birads_737037))
print("Single-Modality (birads_737037): p = %f" % (p_fs_birads_737037))
print("Multi-Modality (birads_737037): F = %f" % (F_fm_birads_737037))
print("Multi-Modality (birads_737037): p = %f" % (p_fm_birads_737037))

# ============================================== #
# ============================================== #

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ==================== END File ==================== #
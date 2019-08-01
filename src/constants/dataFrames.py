#!/usr/bin/env python

"""summaries.py: This file aims at summarizing our DataFrames."""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "ACADEMIC & COMMERCIAL"
__version__     = "2.0.0"
__status__      = "Production"
__copyright__   = "Copyright 2019, Instituto Superior Técnico (IST)"
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

saJoinPath = os.path.join(pathAbsPath, 'statistical-analysis')
sys.path.append(saJoinPath)
saAbsPath = os.path.abspath(saJoinPath)

saSrcJoinPath = os.path.join(saAbsPath, 'src')
sys.path.append(saSrcJoinPath)
saSrcAbsPath = os.path.abspath(saSrcJoinPath)

saSrcConsJoinPath = os.path.join(saSrcAbsPath, 'constants')
sys.path.append(saSrcConsJoinPath)
saSrcConsAbsPath = os.path.abspath(saSrcConsJoinPath)

saSrcVarsJoinPath = os.path.join(saSrcAbsPath, 'variables')
sys.path.append(saSrcVarsJoinPath)
saSrcVarsAbsPath = os.path.abspath(saSrcVarsJoinPath)

import pandas as pd
import scipy.stats as stats
import researchpy as rp
import statsmodels.api as sm
from statsmodels.formula.api import ols
    
import matplotlib.pyplot as plt

from sheets import *
from baseStatisticalAnalysis import *
from pathsStatisticalAnalysis import *
from messagesStatisticalAnalysis import *

# ============================================== #
#                                                #
#                       UTA7                     #
#                                                #
# ============================================== #

# ============================================== #
#           UTA7: Current vs Assistant           #
# ============================================== #

# BIRADS

# ============================================== #
# ============================================== #

# DOTS

# ============================================== #
# ============================================== #

# NASA-TLX

df025 = df_birads_phy[fne103][df_birads_phy[fne012] == fne013]
df026 = df_birads_phy[fne103][df_birads_phy[fne012] == fne014]
df026 = df_birads_phy[fne103][df_birads_phy[fne012] == fne015]
df028 = df_birads_phy[fne103][df_birads_phy[fne012] == fne016]

# ============================================== #
# ============================================== #

# NOC

# ============================================== #
# ============================================== #

# NOE

# ============================================== #
# ============================================== #

# SUS

# ============================================== #
# ============================================== #

# Time

# ============================================== #

df001 = df_time_full_crrnt[fne105][df_time_full_crrnt[fne012] == fne013]
df002 = df_time_full_crrnt[fne105][df_time_full_crrnt[fne012] == fne014]
df003 = df_time_full_crrnt[fne105][df_time_full_crrnt[fne012] == fne015]
df004 = df_time_full_crrnt[fne105][df_time_full_crrnt[fne012] == fne016]

# ============================================== #

df013 = df_time_full_assis[fne105][df_time_full_assis[fne012] == fne013]
df014 = df_time_full_assis[fne105][df_time_full_assis[fne012] == fne014]
df015 = df_time_full_assis[fne105][df_time_full_assis[fne012] == fne015]
df016 = df_time_full_assis[fne105][df_time_full_assis[fne012] == fne016]

# ============================================== #

print(c010)

# ============================================== #

df005 = df_time_full_crrnt[fne104][df_time_full_crrnt[fne012] == fne013]
df006 = df_time_full_crrnt[fne104][df_time_full_crrnt[fne012] == fne014]
df007 = df_time_full_crrnt[fne104][df_time_full_crrnt[fne012] == fne015]
df008 = df_time_full_crrnt[fne104][df_time_full_crrnt[fne012] == fne016]

# ============================================== #

df017 = df_time_full_assis[fne104][df_time_full_assis[fne012] == fne013]
df018 = df_time_full_assis[fne104][df_time_full_assis[fne012] == fne014]
df019 = df_time_full_assis[fne104][df_time_full_assis[fne012] == fne015]
df020 = df_time_full_assis[fne104][df_time_full_assis[fne012] == fne016]

# ============================================== #

# ============================================== #

df009 = df_time_full_crrnt[fne103][df_time_full_crrnt[fne012] == fne013]
df010 = df_time_full_crrnt[fne103][df_time_full_crrnt[fne012] == fne014]
df011 = df_time_full_crrnt[fne103][df_time_full_crrnt[fne012] == fne015]
df012 = df_time_full_crrnt[fne103][df_time_full_crrnt[fne012] == fne016]

# ============================================== #

df021 = df_time_full_assis[fne103][df_time_full_assis[fne012] == fne013]
df022 = df_time_full_assis[fne103][df_time_full_assis[fne012] == fne014]
df023 = df_time_full_assis[fne103][df_time_full_assis[fne012] == fne015]
df024 = df_time_full_assis[fne103][df_time_full_assis[fne012] == fne016]

# ============================================== #

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ==================== END File ==================== #
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

saSrcMethJoinPath = os.path.join(saSrcAbsPath, 'methods')
sys.path.append(saSrcMethJoinPath)
saSrcMethAbsPath = os.path.abspath(saSrcMethJoinPath)

saSrcVarsJoinPath = os.path.join(saSrcAbsPath, 'variables')
sys.path.append(saSrcVarsJoinPath)
saSrcVarsAbsPath = os.path.abspath(saSrcVarsJoinPath)

import pandas as pd
import scipy.stats as stats
import researchpy as rp
import statsmodels.api as sm
from statsmodels.formula.api import ols
    
import matplotlib.pyplot as plt

from dataFrames import *
from sheets import *

from stats import *

from baseStatisticalAnalysis import *
from pathsStatisticalAnalysis import *
from messagesStatisticalAnalysis import *

# ============================================== #
#                                                #
#                       UTA7                     #
#                                                #
# ============================================== #

# birads_assis.csv
# birads_crrnt.csv
# birads_phy.csv
# birads_real.csv
# dots_assis.csv
# nasatlx_assis.csv
# nasatlx_crrnt.csv
# noc_assis.csv
# noc_crrnt.csv
# noe_ce_assis.csv
# noe_ce_crrnt.csv
# noe_nce_assis.csv
# noe_nce_crrnt.csv
# sus_assis.csv
# sus_crrnt.csv
# time_assis_avtr.csv
# time_assis_dgns.csv
# time_ext_all.csv
# time_ext_reg.csv
# time_full_assis.csv
# time_full_crrnt.csv

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

print(f_birads_phy_low_per_group)

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

orig_stdout = sys.stdout
f_a_time = open(fp107, 'w')
sys.stdout = f_a_time

# ============================================== #

print(c010)
print(t007, fne002, fne004, fne105)
print(f_time_full_crrnt_low_per_group)
print(c010)

# ============================================== #

print(c010)
print(t007, fne002, fne003, fne105)
print(f_time_full_assis_low_per_group)
print(c010)

# ============================================== #

print(c010)

# ============================================== #

print(c010)
print(t007, fne002, fne004, fne104)
print(f_time_full_crrnt_medium_per_group)
print(c010)

# ============================================== #

print(c010)
print(t007, fne002, fne003, fne104)
print(f_time_full_assis_medium_per_group)
print(c010)

# ============================================== #

print(c010)

# ============================================== #

print(c010)
print(t007, fne002, fne004, fne103)
print(f_time_full_crrnt_high_per_group)
print(c010)

# ============================================== #

print(c010)
print(t007, fne002, fne003, fne103)
print(f_time_full_assis_high_per_group)
print(c010)

# ============================================== #

sys.stdout = orig_stdout
f_a_time.close()

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ==================== END File ==================== #
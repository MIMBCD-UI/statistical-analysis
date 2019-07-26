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

import pandas as pd
import scipy.stats as stats
import researchpy as rp
import statsmodels.api as sm
from statsmodels.formula.api import ols
    
import matplotlib.pyplot as plt

from sheets import *

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

# NASA-TLX

# Time

df001 = df_time_full_crrnt['low'][df_time_full_crrnt['group'] == 'intern']
df002 = df_time_full_crrnt['low'][df_time_full_crrnt['group'] == 'junior']
df003 = df_time_full_crrnt['low'][df_time_full_crrnt['group'] == 'middle']
df004 = df_time_full_crrnt['low'][df_time_full_crrnt['group'] == 'senior']

f_time_full_crrnt_low_per_group = stats.f_oneway(df001,
	                                               df002,
	                                               df003,
	                                               df004)

print(f_time_full_crrnt_low_per_group)

df005 = df_time_full_crrnt['medium'][df_time_full_crrnt['group'] == 'intern']
df006 = df_time_full_crrnt['medium'][df_time_full_crrnt['group'] == 'junior']
df007 = df_time_full_crrnt['medium'][df_time_full_crrnt['group'] == 'middle']
df008 = df_time_full_crrnt['medium'][df_time_full_crrnt['group'] == 'senior']

f_time_full_crrnt_medium_per_group = stats.f_oneway(df005,
	                                                  df006,
	                                                  df007,
	                                                  df008)


print(f_time_full_crrnt_medium_per_group)

df009 = df_time_full_crrnt['high'][df_time_full_crrnt['group'] == 'intern']
df010 = df_time_full_crrnt['high'][df_time_full_crrnt['group'] == 'junior']
df011 = df_time_full_crrnt['high'][df_time_full_crrnt['group'] == 'middle']
df012 = df_time_full_crrnt['high'][df_time_full_crrnt['group'] == 'senior']

f_time_full_crrnt_high_per_group = stats.f_oneway(df009,
	                                                df010,
	                                                df011,
	                                                df012)


print(f_time_full_crrnt_high_per_group)

print("==============================")

df013 = df_time_full_assis['low'][df_time_full_assis['group'] == 'intern']
df014 = df_time_full_assis['low'][df_time_full_assis['group'] == 'junior']
df015 = df_time_full_assis['low'][df_time_full_assis['group'] == 'middle']
df016 = df_time_full_assis['low'][df_time_full_assis['group'] == 'senior']

f_time_full_assis_low_per_group = stats.f_oneway(df013,
	                                               df014,
	                                               df015,
	                                               df016)


print(f_time_full_assis_low_per_group)

df017 = df_time_full_assis['medium'][df_time_full_assis['group'] == 'intern']
df018 = df_time_full_assis['medium'][df_time_full_assis['group'] == 'junior']
df019 = df_time_full_assis['medium'][df_time_full_assis['group'] == 'middle']
df020 = df_time_full_assis['medium'][df_time_full_assis['group'] == 'senior']

f_time_full_assis_medium_per_group = stats.f_oneway(df017,
	                                                  df018,
	                                                  df019,
	                                                  df020)

print(f_time_full_assis_medium_per_group)

df021 = df_time_full_assis['high'][df_time_full_assis['group'] == 'intern']
df022 = df_time_full_assis['high'][df_time_full_assis['group'] == 'junior']
df023 = df_time_full_assis['high'][df_time_full_assis['group'] == 'middle']
df024 = df_time_full_assis['high'][df_time_full_assis['group'] == 'senior']

f_time_full_assis_high_per_group = stats.f_oneway(df021,
	                                                df022,
	                                                df023,
	                                                df024)


print(f_time_full_assis_high_per_group)

# BIRADS

df025 = df_birads_phy['high'][df_birads_phy['group'] == 'intern']
df026 = df_birads_phy['high'][df_birads_phy['group'] == 'junior']
df026 = df_birads_phy['high'][df_birads_phy['group'] == 'middle']
df028 = df_birads_phy['high'][df_birads_phy['group'] == 'senior']

f_birads_phy_low_per_group = stats.f_oneway(df025,
	                                          df026,
	                                          df026,
	                                          df028)


print(f_birads_phy_low_per_group)

# ============================================== #
# ============================================== #

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ==================== END File ==================== #
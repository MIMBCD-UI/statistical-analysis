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

f_time_full_crrnt_low_per_group = stats.f_oneway(df_time_full_crrnt['low'][df_time_full_crrnt['group'] == 'intern'],
	                                               df_time_full_crrnt['low'][df_time_full_crrnt['group'] == 'junior'],
	                                               df_time_full_crrnt['low'][df_time_full_crrnt['group'] == 'middle'],
	                                               df_time_full_crrnt['low'][df_time_full_crrnt['group'] == 'senior'])


print(f_time_full_crrnt_low_per_group)

f_time_full_crrnt_medium_per_group = stats.f_oneway(df_time_full_crrnt['medium'][df_time_full_crrnt['group'] == 'intern'],
	                                                  df_time_full_crrnt['medium'][df_time_full_crrnt['group'] == 'junior'],
	                                                  df_time_full_crrnt['medium'][df_time_full_crrnt['group'] == 'middle'],
	                                                  df_time_full_crrnt['medium'][df_time_full_crrnt['group'] == 'senior'])


print(f_time_full_crrnt_medium_per_group)

f_time_full_crrnt_high_per_group = stats.f_oneway(df_time_full_crrnt['high'][df_time_full_crrnt['group'] == 'intern'],
	                                                df_time_full_crrnt['high'][df_time_full_crrnt['group'] == 'junior'],
	                                                df_time_full_crrnt['high'][df_time_full_crrnt['group'] == 'middle'],
	                                                df_time_full_crrnt['high'][df_time_full_crrnt['group'] == 'senior'])


print(f_time_full_crrnt_high_per_group)

print("==============================")

f_time_full_assis_low_per_group = stats.f_oneway(df_time_full_assis['low'][df_time_full_assis['group'] == 'intern'],
	                                               df_time_full_assis['low'][df_time_full_assis['group'] == 'junior'],
	                                               df_time_full_assis['low'][df_time_full_assis['group'] == 'middle'],
	                                               df_time_full_assis['low'][df_time_full_assis['group'] == 'senior'])


print(f_time_full_assis_low_per_group)

f_time_full_assis_medium_per_group = stats.f_oneway(df_time_full_assis['medium'][df_time_full_assis['group'] == 'intern'],
	                                                  df_time_full_assis['medium'][df_time_full_assis['group'] == 'junior'],
	                                                  df_time_full_assis['medium'][df_time_full_assis['group'] == 'middle'],
	                                                  df_time_full_assis['medium'][df_time_full_assis['group'] == 'senior'])


print(f_time_full_assis_medium_per_group)

f_time_full_assis_high_per_group = stats.f_oneway(df_time_full_assis['high'][df_time_full_assis['group'] == 'intern'],
	                                                df_time_full_assis['high'][df_time_full_assis['group'] == 'junior'],
	                                                df_time_full_assis['high'][df_time_full_assis['group'] == 'middle'],
	                                                df_time_full_assis['high'][df_time_full_assis['group'] == 'senior'])


print(f_time_full_assis_high_per_group)

# BIRADS

# f_birads_phy_low_per_group = stats.f_oneway(df_birads_phy['high'][df_birads_phy['group'] == 'intern'],
# 	                                          df_birads_phy['high'][df_birads_phy['group'] == 'junior'],
# 	                                          df_birads_phy['high'][df_birads_phy['group'] == 'middle'],
# 	                                          df_birads_phy['high'][df_birads_phy['group'] == 'senior'])


# print(f_birads_phy_low_per_group)

# ============================================== #
# ============================================== #

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ==================== END File ==================== #
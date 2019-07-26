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

rp_nasatlx_crrnt_mendem = rp.summary_cont(df_nasatlx_crrnt['mental_demand'].groupby(df_nasatlx_crrnt['group']))
print (rp_nasatlx_crrnt_mendem)

rp_nasatlx_assis_mendem = rp.summary_cont(df_nasatlx_assis['mental_demand'].groupby(df_nasatlx_crrnt['group']))
print (rp_nasatlx_assis_mendem)

# BIRADS

rp_birads_assis_low = rp.summary_cont(df_birads_assis['low'].groupby(df_nasatlx_crrnt['group']))
print (rp_birads_assis_low)

rp_birads_phy_low = rp.summary_cont(df_birads_phy['low'].groupby(df_nasatlx_crrnt['group']))
print (rp_birads_phy_low)

rp_birads_assis_medium = rp.summary_cont(df_birads_assis['medium'].groupby(df_nasatlx_crrnt['group']))
print (rp_birads_assis_medium)

rp_birads_phy_medium = rp.summary_cont(df_birads_phy['medium'].groupby(df_nasatlx_crrnt['group']))
print (rp_birads_phy_medium)

rp_birads_assis_high = rp.summary_cont(df_birads_assis['high'].groupby(df_nasatlx_crrnt['group']))
print (rp_birads_assis_high)

rp_birads_phy_high = rp.summary_cont(df_birads_phy['high'].groupby(df_nasatlx_crrnt['group']))
print (rp_birads_phy_high)

# ============================================== #
# ============================================== #

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ==================== END File ==================== #
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
# ++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #
# ============================================== #
#                                                #
#                       UTA7                     #
#                                                #
# ============================================== #
# ++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #
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
#                                                #
#           UTA7: Current vs Assistant           #
#                                                #
# ============================================== #

# ============================================== #
#                    BIRADS                      #
# ============================================== #

orig_stdout = sys.stdout
f_birads = open(fp001, 'w')
sys.stdout = f_birads

# +++++++++++++++++++ LOW ++++++++++++++++++++++ #

print(c010)
print(tc001, fne003, fne105)
birads_assis_low_grp = df_birads_assis[fne105].groupby(df_nasatlx_crrnt[fne012])
rp_birads_assis_low = rp.summary_cont(birads_assis_low_grp)
print(rp_birads_assis_low)
print(c010)

print(c010)
print(tc001, fne004, fne105)
birads_phy_low_grp = df_birads_phy[fne105].groupby(df_nasatlx_crrnt[fne012])
rp_birads_phy_low = rp.summary_cont(birads_phy_low_grp)
print(rp_birads_phy_low)
print(c010)

# ============================================== #
# ============================================== #

print(c010)
print(c010)

# +++++++++++++++++ MEDIUM +++++++++++++++++++++ #

print(c010)
print(tc001, fne003, fne104)
birads_assis_md_grp = df_birads_assis[fne104].groupby(df_nasatlx_crrnt[fne012])
rp_birads_assis_medium = rp.summary_cont(birads_assis_md_grp)
print(rp_birads_assis_medium)
print(c010)

print(c010)
print(tc001, fne004, fne104)
birads_phy_med_grp = df_birads_phy[fne104].groupby(df_nasatlx_crrnt[fne012])
rp_birads_phy_medium = rp.summary_cont(birads_phy_med_grp)
print(rp_birads_phy_medium)
print(c010)

# ============================================== #
# ============================================== #

print(c010)
print(c010)

# ++++++++++++++++++ HIGH ++++++++++++++++++++++ #

print(c010)
print(tc001, fne003, fne103)
birads_assis_high_grp = df_birads_assis[fne103].groupby(df_nasatlx_crrnt[fne012])
rp_birads_assis_high = rp.summary_cont(birads_assis_high_grp)
print(rp_birads_assis_high)
print(c010)

print(c010)
print(tc001, fne004, fne103)
birads_phy_high_grp = df_birads_phy[fne103].groupby(df_nasatlx_crrnt[fne012])
rp_birads_phy_high = rp.summary_cont(birads_phy_high_grp)
print(rp_birads_phy_high)
print(c010)

# ============================================== #
# ============================================== #

sys.stdout = orig_stdout
f_birads.close()

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                     DOTS                       #
# ============================================== #

# TODO






# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                   NASA-TLX                     #
# ============================================== #

orig_stdout = sys.stdout
f_nasatlx = open(fp003, 'w')
sys.stdout = f_nasatlx

# +++++++++++++++++++ MD +++++++++++++++++++++++ #

print(c010)
nasatlx_crrnt_md_grp = df_nasatlx_crrnt[fne301].groupby(df_nasatlx_crrnt[fne012])
rp_nasatlx_crrnt_mendem = rp.summary_cont(nasatlx_crrnt_md_grp)
print(rp_nasatlx_crrnt_mendem)
print(c010)

print(c010)
nasatlx_assis_md_grp = df_nasatlx_assis[fne301].groupby(df_nasatlx_crrnt[fne012])
rp_nasatlx_assis_mendem = rp.summary_cont(nasatlx_assis_md_grp)
print(rp_nasatlx_assis_mendem)
print(c010)

# ============================================== #
# ============================================== #

sys.stdout = orig_stdout
f_nasatlx.close()

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                     NOC                        #
# ============================================== #

# TODO






# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                     NOE                        #
# ============================================== #

# TODO






# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                     SUS                        #
# ============================================== #

# TODO






# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                    TIME                        #
# ============================================== #

# TODO






# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
# ++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #
# ============================================== #

# ==================== END File ==================== #
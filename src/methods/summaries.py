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
birads_assis_low_grp = df_birads_assis[fne105].groupby(df_birads_assis[fne012])
rp_birads_assis_low = rp.summary_cont(birads_assis_low_grp)
print(rp_birads_assis_low)
print(c010)

print(c010)
print(tc001, fne004, fne105)
birads_phy_low_grp = df_birads_phy[fne105].groupby(df_birads_phy[fne012])
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
birads_assis_md_grp = df_birads_assis[fne104].groupby(df_birads_assis[fne012])
rp_birads_assis_medium = rp.summary_cont(birads_assis_md_grp)
print(rp_birads_assis_medium)
print(c010)

print(c010)
print(tc001, fne004, fne104)
birads_phy_med_grp = df_birads_phy[fne104].groupby(df_birads_phy[fne012])
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
birads_assis_high_grp = df_birads_assis[fne103].groupby(df_birads_assis[fne012])
rp_birads_assis_high = rp.summary_cont(birads_assis_high_grp)
print(rp_birads_assis_high)
print(c010)

print(c010)
print(tc001, fne004, fne103)
birads_phy_high_grp = df_birads_phy[fne103].groupby(df_birads_phy[fne012])
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
print(tc003, fne004, fne301)
nasatlx_crrnt_md_grp = df_nasatlx_crrnt[fne301].groupby(df_nasatlx_crrnt[fne012])
rp_nasatlx_crrnt_mendem = rp.summary_cont(nasatlx_crrnt_md_grp)
print(rp_nasatlx_crrnt_mendem)
print(c010)

print(c010)
print(tc003, fne003, fne301)
nasatlx_assis_md_grp = df_nasatlx_assis[fne301].groupby(df_nasatlx_assis[fne012])
rp_nasatlx_assis_mendem = rp.summary_cont(nasatlx_assis_md_grp)
print(rp_nasatlx_assis_mendem)
print(c010)

# ============================================== #
# ============================================== #

print(c010)
print(c010)

# +++++++++++++++++++ PD +++++++++++++++++++++++ #

print(c010)
print(tc003, fne004, fne302)
nasatlx_crrnt_pd_grp = df_nasatlx_crrnt[fne302].groupby(df_nasatlx_crrnt[fne012])
rp_nasatlx_crrnt_phydem = rp.summary_cont(nasatlx_crrnt_pd_grp)
print(rp_nasatlx_crrnt_phydem)
print(c010)

print(c010)
print(tc003, fne003, fne302)
nasatlx_assis_pd_grp = df_nasatlx_assis[fne302].groupby(df_nasatlx_assis[fne012])
rp_nasatlx_assis_phydem = rp.summary_cont(nasatlx_assis_pd_grp)
print(rp_nasatlx_assis_phydem)
print(c010)

# ============================================== #
# ============================================== #

print(c010)
print(c010)

# +++++++++++++++++++ TD +++++++++++++++++++++++ #

print(c010)
print(tc003, fne004, fne303)
nasatlx_crrnt_tm_grp = df_nasatlx_crrnt[fne303].groupby(df_nasatlx_crrnt[fne012])
rp_nasatlx_crrnt_tmpdem = rp.summary_cont(nasatlx_crrnt_tm_grp)
print(rp_nasatlx_crrnt_tmpdem)
print(c010)

print(c010)
print(tc003, fne003, fne303)
nasatlx_assis_tm_grp = df_nasatlx_assis[fne303].groupby(df_nasatlx_assis[fne012])
rp_nasatlx_assis_tmpdem = rp.summary_cont(nasatlx_assis_tm_grp)
print(rp_nasatlx_assis_tmpdem)
print(c010)

# ============================================== #
# ============================================== #

print(c010)
print(c010)

# ++++++++++++++ Performance +++++++++++++++++++ #

print(c010)
print(tc003, fne004, fne304)
nasatlx_crrnt_pr_grp = df_nasatlx_crrnt[fne304].groupby(df_nasatlx_crrnt[fne012])
rp_nasatlx_crrnt_prf = rp.summary_cont(nasatlx_crrnt_pr_grp)
print(rp_nasatlx_crrnt_prf)
print(c010)

print(c010)
print(tc003, fne003, fne304)
nasatlx_assis_pr_grp = df_nasatlx_assis[fne304].groupby(df_nasatlx_assis[fne012])
rp_nasatlx_assis_prf = rp.summary_cont(nasatlx_assis_pr_grp)
print(rp_nasatlx_assis_prf)
print(c010)

# ============================================== #
# ============================================== #

print(c010)
print(c010)

# ++++++++++++++++ Effort ++++++++++++++++++++++ #

print(c010)
print(tc003, fne004, fne305)
nasatlx_crrnt_ef_grp = df_nasatlx_crrnt[fne305].groupby(df_nasatlx_crrnt[fne012])
rp_nasatlx_crrnt_effrt = rp.summary_cont(nasatlx_crrnt_ef_grp)
print(rp_nasatlx_crrnt_effrt)
print(c010)

print(c010)
print(tc003, fne003, fne305)
nasatlx_assis_ef_grp = df_nasatlx_assis[fne305].groupby(df_nasatlx_assis[fne012])
rp_nasatlx_assis_effrt = rp.summary_cont(nasatlx_assis_ef_grp)
print(rp_nasatlx_assis_effrt)
print(c010)

# ============================================== #
# ============================================== #

print(c010)
print(c010)

# +++++++++++++++ Frustration ++++++++++++++++++ #

print(c010)
print(tc003, fne004, fne306)
nasatlx_crrnt_ft_grp = df_nasatlx_crrnt[fne306].groupby(df_nasatlx_crrnt[fne012])
rp_nasatlx_crrnt_frtr = rp.summary_cont(nasatlx_crrnt_ft_grp)
print(rp_nasatlx_crrnt_frtr)
print(c010)

print(c010)
print(tc003, fne003, fne306)
nasatlx_assis_ft_grp = df_nasatlx_assis[fne306].groupby(df_nasatlx_assis[fne012])
rp_nasatlx_assis_frtr = rp.summary_cont(nasatlx_assis_ft_grp)
print(rp_nasatlx_assis_frtr)
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

orig_stdout = sys.stdout
f_sus = open(fp006, 'w')
sys.stdout = f_sus

# ++++++++++++++++ SUS_01 ++++++++++++++++++++++ #

print(c010)
print(tc006, fne004, fne601)
sus_crrnt_sus_01_grp = df_sus_crrnt[fne601].groupby(df_sus_crrnt[fne012])
rp_sus_crrnt_sus_01 = rp.summary_cont(sus_crrnt_sus_01_grp)
print(rp_sus_crrnt_sus_01)
print(c010)

print(c010)
print(tc006, fne003, fne601)
sus_assis_sus_01_grp = df_sus_assis[fne601].groupby(df_sus_assis[fne012])
rp_sus_assis_sus_01 = rp.summary_cont(sus_assis_sus_01_grp)
print(rp_sus_assis_sus_01)
print(c010)

# ============================================== #
# ============================================== #

print(c010)
print(c010)

# ++++++++++++++++ SUS_02 ++++++++++++++++++++++ #

print(c010)
print(tc006, fne004, fne602)
sus_crrnt_sus_02_grp = df_sus_crrnt[fne602].groupby(df_sus_crrnt[fne012])
rp_sus_crrnt_sus_02 = rp.summary_cont(sus_crrnt_sus_02_grp)
print(rp_sus_crrnt_sus_02)
print(c010)

print(c010)
print(tc006, fne003, fne602)
sus_assis_sus_02_grp = df_sus_assis[fne602].groupby(df_sus_assis[fne012])
rp_sus_assis_sus_02 = rp.summary_cont(sus_assis_sus_02_grp)
print(rp_sus_assis_sus_02)
print(c010)

# ============================================== #
# ============================================== #

print(c010)
print(c010)

# ++++++++++++++++ SUS_03 ++++++++++++++++++++++ #

print(c010)
print(tc006, fne004, fne603)
sus_crrnt_sus_03_grp = df_sus_crrnt[fne603].groupby(df_sus_crrnt[fne012])
rp_sus_crrnt_sus_03 = rp.summary_cont(sus_crrnt_sus_03_grp)
print(rp_sus_crrnt_sus_03)
print(c010)

print(c010)
print(tc006, fne003, fne603)
sus_assis_sus_03_grp = df_sus_assis[fne603].groupby(df_sus_assis[fne012])
rp_sus_assis_sus_03 = rp.summary_cont(sus_assis_sus_03_grp)
print(rp_sus_assis_sus_03)
print(c010)

# ============================================== #
# ============================================== #

print(c010)
print(c010)

# ++++++++++++++++ SUS_04 ++++++++++++++++++++++ #

print(c010)
print(tc006, fne004, fne604)
sus_crrnt_sus_04_grp = df_sus_crrnt[fne604].groupby(df_sus_crrnt[fne012])
rp_sus_crrnt_sus_04 = rp.summary_cont(sus_crrnt_sus_04_grp)
print(rp_sus_crrnt_sus_04)
print(c010)

print(c010)
print(tc006, fne003, fne604)
sus_assis_sus_04_grp = df_sus_assis[fne604].groupby(df_sus_assis[fne012])
rp_sus_assis_sus_04 = rp.summary_cont(sus_assis_sus_04_grp)
print(rp_sus_assis_sus_04)
print(c010)

# ============================================== #
# ============================================== #

print(c010)
print(c010)

# ++++++++++++++++ SUS_05 ++++++++++++++++++++++ #

print(c010)
print(tc006, fne004, fne605)
sus_crrnt_sus_05_grp = df_sus_crrnt[fne605].groupby(df_sus_crrnt[fne012])
rp_sus_crrnt_sus_05 = rp.summary_cont(sus_crrnt_sus_05_grp)
print(rp_sus_crrnt_sus_05)
print(c010)

print(c010)
print(tc006, fne003, fne605)
sus_assis_sus_05_grp = df_sus_assis[fne605].groupby(df_sus_assis[fne012])
rp_sus_assis_sus_05 = rp.summary_cont(sus_assis_sus_05_grp)
print(rp_sus_assis_sus_05)
print(c010)

# ============================================== #
# ============================================== #

print(c010)
print(c010)

# ++++++++++++++++ SUS_06 ++++++++++++++++++++++ #

print(c010)
print(tc006, fne004, fne606)
sus_crrnt_sus_06_grp = df_sus_crrnt[fne606].groupby(df_sus_crrnt[fne012])
rp_sus_crrnt_sus_06 = rp.summary_cont(sus_crrnt_sus_06_grp)
print(rp_sus_crrnt_sus_06)
print(c010)

print(c010)
print(tc006, fne003, fne606)
sus_assis_sus_06_grp = df_sus_assis[fne606].groupby(df_sus_assis[fne012])
rp_sus_assis_sus_06 = rp.summary_cont(sus_assis_sus_06_grp)
print(rp_sus_assis_sus_06)
print(c010)

# ============================================== #
# ============================================== #

print(c010)
print(c010)

# ++++++++++++++++ SUS_07 ++++++++++++++++++++++ #

print(c010)
print(tc006, fne004, fne607)
sus_crrnt_sus_07_grp = df_sus_crrnt[fne607].groupby(df_sus_crrnt[fne012])
rp_sus_crrnt_sus_07 = rp.summary_cont(sus_crrnt_sus_07_grp)
print(rp_sus_crrnt_sus_07)
print(c010)

print(c010)
print(tc006, fne003, fne607)
sus_assis_sus_07_grp = df_sus_assis[fne607].groupby(df_sus_assis[fne012])
rp_sus_assis_sus_07 = rp.summary_cont(sus_assis_sus_07_grp)
print(rp_sus_assis_sus_07)
print(c010)

# ============================================== #
# ============================================== #

print(c010)
print(c010)

# ++++++++++++++++ SUS_08 ++++++++++++++++++++++ #

print(c010)
print(tc006, fne004, fne608)
sus_crrnt_sus_08_grp = df_sus_crrnt[fne608].groupby(df_sus_crrnt[fne012])
rp_sus_crrnt_sus_08 = rp.summary_cont(sus_crrnt_sus_08_grp)
print(rp_sus_crrnt_sus_08)
print(c010)

print(c010)
print(tc006, fne003, fne608)
sus_assis_sus_08_grp = df_sus_assis[fne608].groupby(df_sus_assis[fne012])
rp_sus_assis_sus_08 = rp.summary_cont(sus_assis_sus_08_grp)
print(rp_sus_assis_sus_08)
print(c010)

# ============================================== #
# ============================================== #

print(c010)
print(c010)

# ++++++++++++++++ SUS_09 ++++++++++++++++++++++ #

print(c010)
print(tc006, fne004, fne609)
sus_crrnt_sus_09_grp = df_sus_crrnt[fne609].groupby(df_sus_crrnt[fne012])
rp_sus_crrnt_sus_09 = rp.summary_cont(sus_crrnt_sus_09_grp)
print(rp_sus_crrnt_sus_09)
print(c010)

print(c010)
print(tc006, fne003, fne609)
sus_assis_sus_09_grp = df_sus_assis[fne609].groupby(df_sus_assis[fne012])
rp_sus_assis_sus_09 = rp.summary_cont(sus_assis_sus_09_grp)
print(rp_sus_assis_sus_09)
print(c010)

# ============================================== #
# ============================================== #

print(c010)
print(c010)

# ++++++++++++++++ SUS_10 ++++++++++++++++++++++ #

print(c010)
print(tc006, fne004, fne610)
sus_crrnt_sus_10_grp = df_sus_crrnt[fne610].groupby(df_sus_crrnt[fne012])
rp_sus_crrnt_sus_10 = rp.summary_cont(sus_crrnt_sus_10_grp)
print(rp_sus_crrnt_sus_10)
print(c010)

print(c010)
print(tc006, fne003, fne610)
sus_assis_sus_10_grp = df_sus_assis[fne610].groupby(df_sus_assis[fne012])
rp_sus_assis_sus_10 = rp.summary_cont(sus_assis_sus_10_grp)
print(rp_sus_assis_sus_10)
print(c010)

# ============================================== #
# ============================================== #

sys.stdout = orig_stdout
f_sus.close()

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                TIME - FULL                     #
# ============================================== #

orig_stdout = sys.stdout
f_time = open(fp007, 'w')
sys.stdout = f_time

# ++++++++++++++++++ LOW +++++++++++++++++++++++ #

print(c010)
print(tc007, fne004, fne105)
time_full_crrnt_low_grp = df_time_full_crrnt[fne105].groupby(df_time_full_crrnt[fne012])
rp_time_full_crrnt_low = rp.summary_cont(time_full_crrnt_low_grp)
print(rp_time_full_crrnt_low)
print(c010)

print(c010)
print(tc007, fne003, fne105)
time_full_assis_low_grp = df_time_full_assis[fne105].groupby(df_time_full_assis[fne012])
rp_time_full_assis_low = rp.summary_cont(time_full_assis_low_grp)
print(rp_time_full_assis_low)
print(c010)

# ============================================== #
# ============================================== #

# ++++++++++++++++ MEDIUM ++++++++++++++++++++++ #

print(c010)
print(tc007, fne004, fne104)
time_full_crrnt_low_grp = df_time_full_crrnt[fne104].groupby(df_time_full_crrnt[fne012])
rp_time_full_crrnt_low = rp.summary_cont(time_full_crrnt_low_grp)
print(rp_time_full_crrnt_low)
print(c010)

print(c010)
print(tc007, fne003, fne104)
time_full_assis_low_grp = df_time_full_assis[fne104].groupby(df_time_full_assis[fne012])
rp_time_full_assis_low = rp.summary_cont(time_full_assis_low_grp)
print(rp_time_full_assis_low)
print(c010)

# ============================================== #
# ============================================== #

# +++++++++++++++++ HIGH +++++++++++++++++++++++ #

print(c010)
print(tc007, fne004, fne103)
time_full_crrnt_low_grp = df_time_full_crrnt[fne103].groupby(df_time_full_crrnt[fne012])
rp_time_full_crrnt_low = rp.summary_cont(time_full_crrnt_low_grp)
print(rp_time_full_crrnt_low)
print(c010)

print(c010)
print(tc007, fne003, fne103)
time_full_assis_low_grp = df_time_full_assis[fne103].groupby(df_time_full_assis[fne012])
rp_time_full_assis_low = rp.summary_cont(time_full_assis_low_grp)
print(rp_time_full_assis_low)
print(c010)

# ============================================== #
# ============================================== #

# ============================================== #
# ============================================== #

print(c010)
print(c010)

# ++++++++++++++++ ASSIS +++++++++++++++++++++++ #

# TODO





# ============================================== #
# ============================================== #

print(c010)
print(c010)

# +++++++++++++++++ EXT ++++++++++++++++++++++++ #

# TODO






# ============================================== #
# ============================================== #

sys.stdout = orig_stdout
f_time.close()

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
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
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison
    
import matplotlib.pyplot as plt

from dataFrames import *
from sheets import *

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

f_birads_phy_low_per_group = stats.f_oneway(df025,
                                            df026,
                                            df026,
                                            df028)

l_birads_phy_low_per_group = stats.levene(df025,
                                          df026,
                                          df026,
                                          df028)

print(c010)
print(t001, fne002, fne004, fne105)
print(f_birads_phy_low_per_group)
print(l_birads_phy_low_per_group)
print(c010)

# ============================================== #
# ============================================== #

# DOTS

# ============================================== #

print(c001)
print(c001)
print(c001)
print(c001)

# ============================================== #

# NASA-TLX

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# +++++++++++++++ Current - MD +++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

f_nasatlx_crrnt_md_per_group = stats.f_oneway(df043,
                                              df044,
                                              df045,
                                              df046)

l_nasatlx_crrnt_md_per_group = stats.levene(df043,
                                            df044,
                                            df045,
                                            df046)

print(c010)
print(tc003, fne004, fne301)
print(f_nasatlx_crrnt_md_per_group)
print(l_nasatlx_crrnt_md_per_group)
print(c010)

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# +++++++++++++ END Current - MD +++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++ Assistant - MD ++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

f_nasatlx_assis_md_per_group = stats.f_oneway(df047,
                                              df048,
                                              df049,
                                              df050)

l_nasatlx_assis_md_per_group = stats.levene(df047,
                                            df048,
                                            df049,
                                            df050)

print(c010)
print(tc003, fne003, fne301)
print(f_nasatlx_assis_md_per_group)
print(l_nasatlx_assis_md_per_group)
print(c010)

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# +++++++++++++ END Assistant - MD +++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# +++++++++++++++ Current - PD +++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

f_nasatlx_crrnt_pd_per_group = stats.f_oneway(df051,
                                              df052,
                                              df053,
                                              df054)

l_nasatlx_crrnt_pd_per_group = stats.levene(df051,
                                            df052,
                                            df053,
                                            df054)

print(c010)
print(tc003, fne004, fne302)
print(f_nasatlx_crrnt_pd_per_group)
print(l_nasatlx_crrnt_pd_per_group)
print(c010)

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# +++++++++++++ END Current - PD +++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++ Assistant - PD ++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

f_nasatlx_assis_pd_per_group = stats.f_oneway(df055,
                                              df056,
                                              df057,
                                              df058)

l_nasatlx_assis_pd_per_group = stats.levene(df055,
                                            df056,
                                            df057,
                                            df058)

print(c010)
print(tc003, fne003, fne302)
print(f_nasatlx_assis_pd_per_group)
print(l_nasatlx_assis_pd_per_group)
print(c010)

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# +++++++++++++ END Assistant - PD +++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# +++++++++++++++ Current - TD +++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

f_nasatlx_crrnt_td_per_group = stats.f_oneway(df059,
                                              df060,
                                              df061,
                                              df062)

l_nasatlx_crrnt_td_per_group = stats.levene(df059,
                                            df060,
                                            df061,
                                            df062)

print(c010)
print(tc003, fne004, fne303)
print(f_nasatlx_crrnt_td_per_group)
print(l_nasatlx_crrnt_td_per_group)
print(c010)

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# +++++++++++++ END Current - TD +++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++ Assistant - TD ++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

f_nasatlx_assis_td_per_group = stats.f_oneway(df063,
                                              df064,
                                              df065,
                                              df066)

l_nasatlx_assis_td_per_group = stats.levene(df063,
                                            df064,
                                            df065,
                                            df066)

print(c010)
print(tc003, fne003, fne303)
print(f_nasatlx_assis_td_per_group)
print(l_nasatlx_assis_td_per_group)
print(c010)

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# +++++++++++++ END Assistant - TD +++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# +++++++++++++++ Current - PE +++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

f_nasatlx_crrnt_pe_per_group = stats.f_oneway(df067,
                                              df068,
                                              df069,
                                              df070)

l_nasatlx_crrnt_pe_per_group = stats.levene(df067,
                                            df068,
                                            df069,
                                            df070)

print(c010)
print(tc003, fne004, fne304)
print(f_nasatlx_crrnt_pe_per_group)
print(l_nasatlx_crrnt_pe_per_group)
print(c010)

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# +++++++++++++ END Current - PE +++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++ Assistant - PE ++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

f_nasatlx_assis_pe_per_group = stats.f_oneway(df071,
                                              df072,
                                              df073,
                                              df074)

l_nasatlx_assis_pe_per_group = stats.levene(df071,
                                            df072,
                                            df073,
                                            df074)

print(c010)
print(tc003, fne003, fne304)
print(f_nasatlx_assis_pe_per_group)
print(l_nasatlx_assis_pe_per_group)
print(c010)

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# +++++++++++++ END Assistant - PE +++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# +++++++++++++++ Current - EF +++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

f_nasatlx_crrnt_ef_per_group = stats.f_oneway(df075,
                                              df076,
                                              df077,
                                              df078)

l_nasatlx_crrnt_ef_per_group = stats.levene(df075,
                                            df076,
                                            df077,
                                            df078)

print(c010)
print(tc003, fne004, fne305)
print(f_nasatlx_crrnt_ef_per_group)
print(l_nasatlx_crrnt_ef_per_group)
print(c010)

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# +++++++++++++ END Current - EF +++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++ Assistant - EF ++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

f_nasatlx_assis_ef_per_group = stats.f_oneway(df079,
                                              df080,
                                              df081,
                                              df082)

l_nasatlx_assis_ef_per_group = stats.levene(df079,
                                            df080,
                                            df081,
                                            df082)

print(c010)
print(tc003, fne003, fne305)
print(f_nasatlx_assis_ef_per_group)
print(l_nasatlx_assis_ef_per_group)
print(c010)

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# +++++++++++++ END Assistant - EF +++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# +++++++++++++++ Current - FU +++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

f_nasatlx_crrnt_fu_per_group = stats.f_oneway(df083,
                                              df084,
                                              df085,
                                              df086)

l_nasatlx_crrnt_fu_per_group = stats.levene(df083,
                                            df084,
                                            df085,
                                            df086)

print(c010)
print(tc003, fne004, fne306)
print(f_nasatlx_crrnt_fu_per_group)
print(l_nasatlx_crrnt_fu_per_group)
print(c010)

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# +++++++++++++ END Current - FU +++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++ Assistant - FU ++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

f_nasatlx_assis_fu_per_group = stats.f_oneway(df087,
                                              df088,
                                              df089,
                                              df090)

l_nasatlx_assis_fu_per_group = stats.levene(df087,
                                            df088,
                                            df089,
                                            df090)

print(c010)
print(tc003, fne003, fne306)
print(f_nasatlx_assis_fu_per_group)
print(l_nasatlx_assis_fu_per_group)
print(c010)

# ++++++++++++++++++++++++++++++++++++++++++++++ #
# +++++++++++++ END Assistant - FU +++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

# ============================================== #

print(c001)
print(c001)
print(c001)
print(c001)

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

# ++++++++++++++++++++++++++++++++++++++++++++++ #
#                    Time                        #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

# ============================================== #

print(c001)
print(c001)

# ============================================== #

f_time_full_crrnt_low_per_group = stats.f_oneway(df001,
	                                               df002,
	                                               df003,
	                                               df004)

l_time_full_crrnt_low_per_group = stats.levene(df001,
                                               df002,
                                               df003,
                                               df004)

mc_time_full_crrnt_low_per_group = MultiComparison(df_time_full_crrnt[fne105],
	                                                 df_time_full_crrnt[fne012])
mc_res_time_full_crrnt_low_per_group = mc_time_full_crrnt_low_per_group.tukeyhsd()

print(c010)
print(t007, fne002, fne004, fne105)
print(f_time_full_crrnt_low_per_group)
print(l_time_full_crrnt_low_per_group)
print(mc_res_time_full_crrnt_low_per_group)
print(c010)

# ============================================== #

f_time_full_assis_low_per_group = stats.f_oneway(df013,
	                                               df014,
	                                               df015,
	                                               df016)

l_time_full_assis_low_per_group = stats.levene(df013,
                                               df014,
                                               df015,
                                               df016)

print(c010)
print(t007, fne002, fne003, fne105)
print(f_time_full_assis_low_per_group)
print(l_time_full_assis_low_per_group)
print(c010)

# ============================================== #

print(c001)
print(c010)
print(c001)

# ============================================== #

f_time_full_crrnt_medium_per_group = stats.f_oneway(df005,
	                                                  df006,
	                                                  df007,
	                                                  df008)

l_time_full_crrnt_medium_per_group = stats.levene(df005,
                                                  df006,
                                                  df007,
                                                  df008)

print(c010)
print(t007, fne002, fne004, fne104)
print(f_time_full_crrnt_medium_per_group)
print(l_time_full_crrnt_medium_per_group)
print(c010)

# ============================================== #

f_time_full_assis_medium_per_group = stats.f_oneway(df017,
	                                                  df018,
	                                                  df019,
	                                                  df020)

l_time_full_assis_medium_per_group = stats.levene(df017,
                                                  df018,
                                                  df019,
                                                  df020)

print(c010)
print(t007, fne002, fne003, fne104)
print(f_time_full_assis_medium_per_group)
print(l_time_full_assis_medium_per_group)
print(c010)

# ============================================== #

print(c001)
print(c010)
print(c001)

# ============================================== #

f_time_full_crrnt_high_per_group = stats.f_oneway(df009,
	                                                df010,
	                                                df011,
	                                                df012)

l_time_full_crrnt_high_per_group = stats.levene(df009,
                                                df010,
                                                df011,
                                                df012)

print(c010)
print(t007, fne002, fne004, fne103)
print(f_time_full_crrnt_high_per_group)
print(l_time_full_crrnt_high_per_group)
print(c010)

# ============================================== #

f_time_full_assis_high_per_group = stats.f_oneway(df021,
	                                                df022,
	                                                df023,
	                                                df024)

l_time_full_assis_high_per_group = stats.levene(df021,
                                                df022,
                                                df023,
                                                df024)

print(c010)
print(t007, fne002, fne003, fne103)
print(f_time_full_assis_high_per_group)
print(l_time_full_assis_high_per_group)
print(c010)

# ============================================== #

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ==================== END File ==================== #
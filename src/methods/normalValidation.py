#!/usr/bin/env python

""".py: """

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

saJoinPath = os.path.join(pathAbsPath, 'statistical-analysis', '')
saPathAbsPath = os.path.abspath(saJoinPath)
sys.path.append(saPathAbsPath)

saSrcJoinPath = os.path.join(saPathAbsPath, 'src', '')
saSrcPathAbsPath = os.path.abspath(saSrcJoinPath)
sys.path.append(saSrcPathAbsPath)

sa_constants_dir = os.path.join(saSrcPathAbsPath, 'constants')
sa_methods_dir = os.path.join(saSrcPathAbsPath, 'methods')

sys.path.append(sa_constants_dir)
sys.path.append(sa_methods_dir)

from special import *
from listGroups import *
from kDagostPear import *

from dataFrames import *
from sheets import *

from baseStatisticalAnalysis import *
from pathsStatisticalAnalysis import *
from messagesStatisticalAnalysis import *

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #
#                                                #
#              NORMAL VALIDATION                 #
#                                                #
# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

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

# ++++++++++++++++++++++++++++++++++++++++++++++ #
#                   BIRADS                       #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

print(c010)
print(tc001, fn008)

# ============================================== #
# ============================================== #

print(c001)
print(c001)
print(c001)
print(c001)

# ++++++++++++++++++++++++++++++++++++++++++++++ #
#                    DOTS                        #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

print(c010)
print(tc002, fn008)

# ============================================== #
# ============================================== #

print(c001)
print(c001)
print(c001)
print(c001)

# ++++++++++++++++++++++++++++++++++++++++++++++ #
#                  NASA-TLX                      #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

print(c010)
print(tc003, fn008)

# +++++++++++++++++ Current ++++++++++++++++++++ #

print(c010)

print(fne004)

dfnc_nasatlx_md = df_nasatlx_crrnt[fne301]
dfnc_nasatlx_pd = df_nasatlx_crrnt[fne302]
dfnc_nasatlx_td = df_nasatlx_crrnt[fne303]
dfnc_nasatlx_pe = df_nasatlx_crrnt[fne304]
dfnc_nasatlx_ef = df_nasatlx_crrnt[fne305]
dfnc_nasatlx_fr = df_nasatlx_crrnt[fne306]

n_nasatlx_crrnt_md = stats.normaltest(dfnc_nasatlx_md)
n_nasatlx_crrnt_pd = stats.normaltest(dfnc_nasatlx_pd)
n_nasatlx_crrnt_td = stats.normaltest(dfnc_nasatlx_td)
n_nasatlx_crrnt_pe = stats.normaltest(dfnc_nasatlx_pe)
n_nasatlx_crrnt_ef = stats.normaltest(dfnc_nasatlx_ef)
n_nasatlx_crrnt_fr = stats.normaltest(dfnc_nasatlx_fr)

nncmd_k2, nncmd_p = stats.normaltest(dfnc_nasatlx_md)
nncpd_k2, nncpd_p = stats.normaltest(dfnc_nasatlx_pd)
nnctd_k2, nnctd_p = stats.normaltest(dfnc_nasatlx_td)
nncpe_k2, nncpe_p = stats.normaltest(dfnc_nasatlx_pe)
nncef_k2, nncef_p = stats.normaltest(dfnc_nasatlx_ef)
nncfr_k2, nncfr_p = stats.normaltest(dfnc_nasatlx_fr)

print(n_nasatlx_crrnt_md)
print(n_nasatlx_crrnt_pd)
print(n_nasatlx_crrnt_td)
print(n_nasatlx_crrnt_pe)
print(n_nasatlx_crrnt_ef)
print(n_nasatlx_crrnt_fr)

print(c010)

# ++++++++++++++++++++++++++++++++++++++++++++++ #

# ++++++++++++++++ Assistant +++++++++++++++++++ #

print(c010)

print(fne003)

dfna_nasatlx_md = df_nasatlx_assis[fne301]
dfna_nasatlx_pd = df_nasatlx_assis[fne302]
dfna_nasatlx_td = df_nasatlx_assis[fne303]
dfna_nasatlx_pe = df_nasatlx_assis[fne304]
dfna_nasatlx_ef = df_nasatlx_assis[fne305]
dfna_nasatlx_fr = df_nasatlx_assis[fne306]

n_nasatlx_assis_md = stats.normaltest(dfna_nasatlx_md)
n_nasatlx_assis_pd = stats.normaltest(dfna_nasatlx_pd)
n_nasatlx_assis_td = stats.normaltest(dfna_nasatlx_td)
n_nasatlx_assis_pe = stats.normaltest(dfna_nasatlx_pe)
n_nasatlx_assis_ef = stats.normaltest(dfna_nasatlx_ef)
n_nasatlx_assis_fr = stats.normaltest(dfna_nasatlx_fr)

nnamd_k2, nnamd_p = stats.normaltest(dfna_nasatlx_md)
nnapd_k2, nnapd_p = stats.normaltest(dfna_nasatlx_pd)
nnatd_k2, nnatd_p = stats.normaltest(dfna_nasatlx_td)
nnape_k2, nnape_p = stats.normaltest(dfna_nasatlx_pe)
nnaef_k2, nnaef_p = stats.normaltest(dfna_nasatlx_ef)
nnafr_k2, nnafr_p = stats.normaltest(dfna_nasatlx_fr)

print(n_nasatlx_assis_md)
print(n_nasatlx_assis_pd)
print(n_nasatlx_assis_td)
print(n_nasatlx_assis_pe)
print(n_nasatlx_assis_ef)
print(n_nasatlx_assis_fr)

print(c010)

# ++++++++++++++++++++++++++++++++++++++++++++++ #

# ============================================== #
# ============================================== #

print(c001)
print(c001)
print(c001)
print(c001)

# ++++++++++++++++++++++++++++++++++++++++++++++ #
#                    NOC                         #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

print(c010)
print(tc004, fn008)

# ============================================== #
# ============================================== #

print(c001)
print(c001)
print(c001)
print(c001)

# ++++++++++++++++++++++++++++++++++++++++++++++ #
#                    NOE                         #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

print(c010)
print(tc005, fn008)

# ============================================== #
# ============================================== #

print(c001)
print(c001)
print(c001)
print(c001)

# ++++++++++++++++++++++++++++++++++++++++++++++ #
#                    SUS                         #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

print(c010)
print(tc006, fn008)

# ++++++++++++++++ Current +++++++++++++++++++++ #

print(c010)

print(fne004)

dfsc_sus_01 = df_sus_crrnt[fne601]
dfsc_sus_02 = df_sus_crrnt[fne602]
dfsc_sus_03 = df_sus_crrnt[fne603]
dfsc_sus_04 = df_sus_crrnt[fne604]
dfsc_sus_05 = df_sus_crrnt[fne605]
dfsc_sus_06 = df_sus_crrnt[fne606]
dfsc_sus_07 = df_sus_crrnt[fne607]
dfsc_sus_08 = df_sus_crrnt[fne608]
dfsc_sus_09 = df_sus_crrnt[fne609]
dfsc_sus_10 = df_sus_crrnt[fne610]

n_sus_crrnt_sus_01 = stats.normaltest(dfsc_sus_01)
n_sus_crrnt_sus_02 = stats.normaltest(dfsc_sus_02)
n_sus_crrnt_sus_03 = stats.normaltest(dfsc_sus_03)
n_sus_crrnt_sus_04 = stats.normaltest(dfsc_sus_04)
n_sus_crrnt_sus_05 = stats.normaltest(dfsc_sus_05)
n_sus_crrnt_sus_06 = stats.normaltest(dfsc_sus_06)
n_sus_crrnt_sus_07 = stats.normaltest(dfsc_sus_07)
n_sus_crrnt_sus_08 = stats.normaltest(dfsc_sus_08)
n_sus_crrnt_sus_09 = stats.normaltest(dfsc_sus_09)
n_sus_crrnt_sus_10 = stats.normaltest(dfsc_sus_10)

nscs_01_k2, nscs_01_p = stats.normaltest(dfsc_sus_01)
nscs_02_k2, nscs_02_p = stats.normaltest(dfsc_sus_02)
nscs_03_k2, nscs_03_p = stats.normaltest(dfsc_sus_03)
nscs_04_k2, nscs_04_p = stats.normaltest(dfsc_sus_04)
nscs_05_k2, nscs_05_p = stats.normaltest(dfsc_sus_05)
nscs_06_k2, nscs_06_p = stats.normaltest(dfsc_sus_06)
nscs_07_k2, nscs_07_p = stats.normaltest(dfsc_sus_07)
nscs_08_k2, nscs_08_p = stats.normaltest(dfsc_sus_08)
nscs_09_k2, nscs_09_p = stats.normaltest(dfsc_sus_09)
nscs_10_k2, nscs_10_p = stats.normaltest(dfsc_sus_10)

print(n_sus_crrnt_sus_01)
print(n_sus_crrnt_sus_02)
print(n_sus_crrnt_sus_03)
print(n_sus_crrnt_sus_04)
print(n_sus_crrnt_sus_05)
print(n_sus_crrnt_sus_06)
print(n_sus_crrnt_sus_07)
print(n_sus_crrnt_sus_08)
print(n_sus_crrnt_sus_09)
print(n_sus_crrnt_sus_10)

print(c010)

# ++++++++++++++++++++++++++++++++++++++++++++++ #

print(c001)

# +++++++++++++++ Assistant ++++++++++++++++++++ #

print(c010)

print(fne003)

dfsa_sus_01 = df_sus_assis[fne601]
dfsa_sus_02 = df_sus_assis[fne602]
dfsa_sus_03 = df_sus_assis[fne603]
dfsa_sus_04 = df_sus_assis[fne604]
dfsa_sus_05 = df_sus_assis[fne605]
dfsa_sus_06 = df_sus_assis[fne606]
dfsa_sus_07 = df_sus_assis[fne607]
dfsa_sus_08 = df_sus_assis[fne608]
dfsa_sus_09 = df_sus_assis[fne609]
dfsa_sus_10 = df_sus_assis[fne610]

n_sus_assis_sus_01 = stats.normaltest(dfsa_sus_01)
n_sus_assis_sus_02 = stats.normaltest(dfsa_sus_02)
n_sus_assis_sus_03 = stats.normaltest(dfsa_sus_03)
n_sus_assis_sus_04 = stats.normaltest(dfsa_sus_04)
n_sus_assis_sus_05 = stats.normaltest(dfsa_sus_05)
n_sus_assis_sus_06 = stats.normaltest(dfsa_sus_06)
n_sus_assis_sus_07 = stats.normaltest(dfsa_sus_07)
n_sus_assis_sus_08 = stats.normaltest(dfsa_sus_08)
n_sus_assis_sus_09 = stats.normaltest(dfsa_sus_09)
n_sus_assis_sus_10 = stats.normaltest(dfsa_sus_10)

nsas_01_k2, nsas_01_p = stats.normaltest(dfsa_sus_01)
nsas_02_k2, nsas_02_p = stats.normaltest(dfsa_sus_02)
nsas_03_k2, nsas_03_p = stats.normaltest(dfsa_sus_03)
nsas_04_k2, nsas_04_p = stats.normaltest(dfsa_sus_04)
nsas_05_k2, nsas_05_p = stats.normaltest(dfsa_sus_05)
nsas_06_k2, nsas_06_p = stats.normaltest(dfsa_sus_06)
nsas_07_k2, nsas_07_p = stats.normaltest(dfsa_sus_07)
nsas_08_k2, nsas_08_p = stats.normaltest(dfsa_sus_08)
nsas_09_k2, nsas_09_p = stats.normaltest(dfsa_sus_09)
nsas_10_k2, nsas_10_p = stats.normaltest(dfsa_sus_10)

print(n_sus_assis_sus_01)
print(n_sus_assis_sus_02)
print(n_sus_assis_sus_03)
print(n_sus_assis_sus_04)
print(n_sus_assis_sus_05)
print(n_sus_assis_sus_06)
print(n_sus_assis_sus_07)
print(n_sus_assis_sus_08)
print(n_sus_assis_sus_09)
print(n_sus_assis_sus_10)

print(c010)

# ++++++++++++++++++++++++++++++++++++++++++++++ #

# ============================================== #
# ============================================== #

print(c001)
print(c001)
print(c001)
print(c001)

# ++++++++++++++++++++++++++++++++++++++++++++++ #
#                 Time - Full                    #
# ++++++++++++++++++++++++++++++++++++++++++++++ #

# +++++++++++++++++ Current ++++++++++++++++++++ #

dftfc_low = df_time_full_crrnt[fne105]
dftfc_med = df_time_full_crrnt[fne104]
dftfc_hgh = df_time_full_crrnt[fne103]

n_time_full_crrnt_low = stats.normaltest(dftfc_low)
n_time_full_crrnt_med = stats.normaltest(dftfc_med)
n_time_full_crrnt_hgh = stats.normaltest(dftfc_hgh)

ntfcl_k2, ntfcl_p = stats.normaltest(dftfc_low)
ntfcm_k2, ntfcm_p = stats.normaltest(dftfc_med)
ntfch_k2, ntfch_p = stats.normaltest(dftfc_hgh)

print(c010)
print(tc007, fn008)

print(c023)
print(fn007, fne004, fne105)
print(n_time_full_crrnt_low)
print(c023)
print(fn007, fne004, fne104)
print(n_time_full_crrnt_med)
print(c023)
print(fn007, fne004, fne103)
print(n_time_full_crrnt_hgh)
print(c023)

print(c010)

# ++++++++++++++++++++++++++++++++++++++++++++++ #

print(c001)

# ++++++++++++++++ Assistant +++++++++++++++++++ #

dftfa_low = df_time_full_assis[fne105]
dftfa_med = df_time_full_assis[fne104]
dftfa_hgh = df_time_full_assis[fne103]

n_time_full_assis_low = stats.normaltest(dftfa_low)
n_time_full_assis_med = stats.normaltest(dftfa_med)
n_time_full_assis_hgh = stats.normaltest(dftfa_hgh)

ntfal_k2, ntfal_p = stats.normaltest(dftfa_low)
ntfam_k2, ntfam_p = stats.normaltest(dftfa_med)
ntfah_k2, ntfah_p = stats.normaltest(dftfa_hgh)

print(c010)
print(tc007, fn008)

print(c023)
print(fn007, fne003, fne105)
print(n_time_full_assis_low)
print(c023)
print(fn007, fne003, fne104)
print(n_time_full_assis_med)
print(c023)
print(fn007, fne003, fne103)
print(n_time_full_assis_hgh)
print(c023)

print(c010)

# ++++++++++++++++++++++++++++++++++++++++++++++ #

# ============================================== #

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

print(c001)
print(c001)
print(c001)
print(c001)

# ============================================== #
#                                                #
#                       UTA4                     #
#                                                #
# ============================================== #

# ============================================== #
#          NASA-TLX: Single-Modality             #
# ============================================== #

normalValidation_s_001 = stats.normaltest(s_001)
normalValidation_s_002 = stats.normaltest(s_002)
normalValidation_s_003 = stats.normaltest(s_003)
normalValidation_s_004 = stats.normaltest(s_004)
normalValidation_s_005 = stats.normaltest(s_005)
normalValidation_s_006 = stats.normaltest(s_006)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_001)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_002)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_003)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_004)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_005)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_006)

# ============================================== #
# ============================================== #

# ============================================== #
#          NASA-TLX: Multi-Modality              #
# ============================================== #

normalValidation_s_007 = stats.normaltest(s_007)
normalValidation_s_008 = stats.normaltest(s_008)
normalValidation_s_009 = stats.normaltest(s_009)
normalValidation_s_010 = stats.normaltest(s_010)
normalValidation_s_011 = stats.normaltest(s_011)
normalValidation_s_012 = stats.normaltest(s_012)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_007)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_008)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_009)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_010)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_011)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_012)

# ============================================== #
# ============================================== #

# ============================================== #
#            SUS: Single-Modality                #
# ============================================== #

normalValidation_s_013 = stats.normaltest(s_013)
normalValidation_s_014 = stats.normaltest(s_014)
normalValidation_s_015 = stats.normaltest(s_015)
normalValidation_s_016 = stats.normaltest(s_016)
normalValidation_s_017 = stats.normaltest(s_017)
normalValidation_s_018 = stats.normaltest(s_018)
normalValidation_s_019 = stats.normaltest(s_019)
normalValidation_s_020 = stats.normaltest(s_020)
normalValidation_s_021 = stats.normaltest(s_021)
normalValidation_s_022 = stats.normaltest(s_022)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_013)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_014)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_015)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_016)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_017)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_018)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_019)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_020)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_021)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_022)

# ============================================== #
# ============================================== #

# ============================================== #
#            SUS: Multi-Modality                 #
# ============================================== #

normalValidation_s_023 = stats.normaltest(s_023)
normalValidation_s_024 = stats.normaltest(s_024)
normalValidation_s_025 = stats.normaltest(s_025)
normalValidation_s_026 = stats.normaltest(s_026)
normalValidation_s_027 = stats.normaltest(s_027)
normalValidation_s_028 = stats.normaltest(s_028)
normalValidation_s_029 = stats.normaltest(s_029)
normalValidation_s_030 = stats.normaltest(s_030)
normalValidation_s_031 = stats.normaltest(s_031)
normalValidation_s_032 = stats.normaltest(s_032)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_023)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_024)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_025)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_026)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_027)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_028)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_029)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_030)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_031)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_032)

# ============================================== #
# ============================================== #

# ============================================== #
#            TIME: Single-Modality               #
# ============================================== #

normalValidation_s_033 = stats.normaltest(s_033)
normalValidation_s_034 = stats.normaltest(s_034)
normalValidation_s_035 = stats.normaltest(s_035)
normalValidation_s_036 = stats.normaltest(s_036)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_033)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_034)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_035)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_036)

# ============================================== #
# ============================================== #

# ============================================== #
#            TIME: Multi-Modality                #
# ============================================== #

normalValidation_s_037 = stats.normaltest(s_037)
normalValidation_s_038 = stats.normaltest(s_038)
normalValidation_s_039 = stats.normaltest(s_039)
normalValidation_s_040 = stats.normaltest(s_040)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_037)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_038)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_039)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_040)

# ============================================== #
# ============================================== #

# ============================================== #
#            CLICKS: Single-Modality             #
# ============================================== #

normalValidation_s_041 = stats.normaltest(s_041)
normalValidation_s_042 = stats.normaltest(s_042)
normalValidation_s_043 = stats.normaltest(s_043)
normalValidation_s_044 = stats.normaltest(s_044)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_041)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_042)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_043)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_044)

# ============================================== #
# ============================================== #

# ============================================== #
#            CLICKS: Multi-Modality              #
# ============================================== #

normalValidation_s_045 = stats.normaltest(s_045)
normalValidation_s_046 = stats.normaltest(s_046)
normalValidation_s_047 = stats.normaltest(s_047)
normalValidation_s_048 = stats.normaltest(s_048)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_045)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_046)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_047)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_048)

# ============================================== #
# ============================================== #

# ============================================== #
#            ERRORS: Single-Modality             #
# ============================================== #

normalValidation_s_049 = stats.normaltest(s_049)
normalValidation_s_050 = stats.normaltest(s_050)
normalValidation_s_051 = stats.normaltest(s_051)
normalValidation_s_052 = stats.normaltest(s_052)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_049)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_050)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_051)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_052)

# ============================================== #
# ============================================== #

# ============================================== #
#            ERRORS: Multi-Modality              #
# ============================================== #

normalValidation_s_053 = stats.normaltest(s_053)
normalValidation_s_054 = stats.normaltest(s_054)
normalValidation_s_055 = stats.normaltest(s_055)
normalValidation_s_056 = stats.normaltest(s_056)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_053)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_054)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_055)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_056)

# ============================================== #
# ============================================== #

# ============================================== #
#            BIRADS: Single-Modality             #
# ============================================== #

normalValidation_s_057 = stats.normaltest(s_057)
normalValidation_s_058 = stats.normaltest(s_058)
normalValidation_s_059 = stats.normaltest(s_059)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_057)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_058)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_059)

# ============================================== #
# ============================================== #

# ============================================== #
#            BIRADS: MULTI-Modality              #
# ============================================== #

normalValidation_s_060 = stats.normaltest(s_060)
normalValidation_s_061 = stats.normaltest(s_061)
normalValidation_s_062 = stats.normaltest(s_062)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_060)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_061)
print("[D'Agostino and Pearson: Normal Distribution]" + "\n", normalValidation_s_062)

# ============================================== #
# ============================================== #

# ============================================== #
#       D'Agostino and Pearson: Kurtosis         #
# ============================================== #

kDagostPear(s_min, s_max)

# ============================================== #
# ============================================== #

# ==================== END File ==================== #
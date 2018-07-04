#!/usr/bin/env python

"""anova.py: A python version of ANOVA."""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "ACADEMIC & COMMERCIAL"
__version__     = "1.1.0"
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
#pathDirname = '/Users/Francisco/Git/statistical-analysis/methods/anova.py'
joinPath = os.path.join(pathDirname, '..', '..')
pathAbsPath = os.path.abspath(joinPath)
#pathAbsPath = '/Users/Francisco/Git/statistical-analysis/methods/anova.py'

print(pathDirname)

sa_scripts_dir = (pathAbsPath + '/statistical-analysis/scripts/')
sys.path.append(sa_scripts_dir)

from nasa import nasaColMean

src_dir = (pathAbsPath + '/sheet-reader/src/')
sys.path.append(src_dir)

constants_dir = (pathAbsPath + '/sheet-reader/constants/')
sys.path.append(constants_dir)
import main_variables

MV_N = main_variables.N

scripts_dir = (pathAbsPath + '/sheet-reader/scripts/')
sys.path.append(scripts_dir)
import sheetReaders

main_sheet_dir = pathAbsPath + '/sheet-reader/temp/main_sheet.csv'
fs_sheet_dir = pathAbsPath + '/sheet-reader/temp/fs_sheet.csv'
fm_sheet_dir = pathAbsPath + '/sheet-reader/temp/fm_sheet.csv'

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np

datafile_fs = pd.read_csv(fs_sheet_dir)
datafile_fm = pd.read_csv(fm_sheet_dir)

# ============================================== #
#                                                #
#                 CREATE BOXPLOT                 #
#                                                #
# ============================================== #

nasatlx_columns = [
  'mental_demand',
  'physical_demand',
  'temporal_demand',
  'performance',
  'effort',
  'frustration'
]

filterByColumn = 'group'
figSizeX = 12
figSizeY = 8

# ============================================== #
#                SINGLE-MODALITY                 #
# ============================================== #

def createBoxplotFS(filterBy, array):
  i = 0
  for i in range(len(array)):
    datafile_fs.boxplot(array[i], by=filterByColumn, figsize=(figSizeX, figSizeY))

createBoxplotFS(filterByColumn, nasatlx_columns)

# ============================================== #
#                 MULTI-MODALITY                 #
# ============================================== #

def createBoxplotFM(filterBy, array):
  i = 0
  for i in range(len(array)):
    datafile_fm.boxplot(array[i], by=filterByColumn, figsize=(figSizeX, figSizeY))

createBoxplotFM(filterByColumn, nasatlx_columns)

# ============================================== #
# ============================================== #

# ============================================== #
#                 INITIALIZATION                 #
# ============================================== #

# intern_1 = datafile_fs['mental_demand'][datafile_fs.group == 'intern_1']
# intern_2 = datafile_fs['mental_demand'][datafile_fs.group == 'intern_2']
# junior_1 = datafile_fs['mental_demand'][datafile_fs.group == 'junior_1']
# junior_2 = datafile_fs['mental_demand'][datafile_fs.group == 'junior_2']
# middle_1 = datafile_fs['mental_demand'][datafile_fs.group == 'middle_1']
# middle_2 = datafile_fs['mental_demand'][datafile_fs.group == 'middle_2']
# senior_1 = datafile_fs['mental_demand'][datafile_fs.group == 'senior_1']
# senior_2 = datafile_fs['mental_demand'][datafile_fs.group == 'senior_2']

grps_fs = pd.unique(datafile_fs.group.values)
grps_fm = pd.unique(datafile_fm.group.values)

# ============================================== #
# ============================================== #

# ============================================== #
#                SINGLE-MODALITY                 #
# ============================================== #

d_data_fs_md = {
  grp:datafile_fs['mental_demand'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_pd = {
  grp:datafile_fs['physical_demand'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_td = {
  grp:datafile_fs['temporal_demand'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_p = {
  grp:datafile_fs['performance'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_e = {
  grp:datafile_fs['effort'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_f = {
  grp:datafile_fs['frustration'][datafile_fs.group == grp]
  for grp in grps_fs
}

# ============================================== #
#                 MULTI-MODALITY                 #
# ============================================== #

d_data_fm_md = {
  grp:datafile_fm['mental_demand'][datafile_fs.group == grp]
  for grp in grps_fm
}

d_data_fm_pd = {
  grp:datafile_fm['physical_demand'][datafile_fs.group == grp]
  for grp in grps_fm
}

d_data_fm_td = {
  grp:datafile_fm['temporal_demand'][datafile_fs.group == grp]
  for grp in grps_fm
}

d_data_fm_p = {
  grp:datafile_fm['performance'][datafile_fs.group == grp]
  for grp in grps_fm
}

d_data_fm_e = {
  grp:datafile_fm['effort'][datafile_fs.group == grp]
  for grp in grps_fm
}

d_data_fm_f = {
  grp:datafile_fm['frustration'][datafile_fs.group == grp]
  for grp in grps_fm
}

# ============================================== #
# ============================================== #

k = len(pd.unique(datafile_fs.group))  # number of conditions
N = len(datafile_fs.values)  # conditions times participants
n = datafile_fs.groupby('group').size()[0] #Participants in each condition

# ============================================== #
#                                                #
#      IS IT NORMAL (GAUSSIAN) DISTRIBUTION?     #
#                                                #
# ============================================== #

s_001 = datafile_fs.mental_demand[:MV_N].tolist()
s_002 = datafile_fs.physical_demand[:MV_N].tolist()
s_003 = datafile_fs.temporal_demand[:MV_N].tolist()
s_004 = datafile_fs.performance[:MV_N].tolist()
s_005 = datafile_fs.effort[:MV_N].tolist()
s_006 = datafile_fs.frustration[:MV_N].tolist()

s_007 = datafile_fm.mental_demand[:MV_N].tolist()
s_008 = datafile_fm.physical_demand[:MV_N].tolist()
s_009 = datafile_fm.temporal_demand[:MV_N].tolist()
s_010 = datafile_fm.performance[:MV_N].tolist()
s_011 = datafile_fm.effort[:MV_N].tolist()
s_012 = datafile_fm.frustration[:MV_N].tolist()

print(s_001)
print(s_002)
print(s_003)
print(s_004)
print(s_005)
print(s_006)

print(s_007)
print(s_008)
print(s_009)
print(s_010)
print(s_011)
print(s_012)

# ============================================== #
# Mean:
mu_s_001 = np.mean(s_001, axis=0)
mu_s_002 = np.mean(s_002, axis=0)
mu_s_003 = np.mean(s_003, axis=0)
mu_s_004 = np.mean(s_004, axis=0)
mu_s_005 = np.mean(s_005, axis=0)
mu_s_006 = np.mean(s_006, axis=0)

mu_s_007 = np.mean(s_007, axis=0)
mu_s_008 = np.mean(s_008, axis=0)
mu_s_009 = np.mean(s_009, axis=0)
mu_s_010 = np.mean(s_010, axis=0)
mu_s_011 = np.mean(s_011, axis=0)
mu_s_012 = np.mean(s_012, axis=0)
# ============================================== #

# ============================================== #
# Standard Deviation:
sigma = 0.1
stdToCompare = 0.01
# ============================================== #

# ============================================== #
# Compute Standard Deviation:
stdComp_s_001 = np.mean(s_001)
stdComp_s_002 = np.mean(s_002)
stdComp_s_003 = np.mean(s_003)
stdComp_s_004 = np.mean(s_004)
stdComp_s_005 = np.mean(s_005)
stdComp_s_006 = np.mean(s_006)
print("Compute Standard Deviation for stdComp_s_001: %d" % stdComp_s_001)
print("Compute Standard Deviation for stdComp_s_002: %d" % stdComp_s_002)
print("Compute Standard Deviation for stdComp_s_003: %d" % stdComp_s_003)
print("Compute Standard Deviation for stdComp_s_004: %d" % stdComp_s_004)
print("Compute Standard Deviation for stdComp_s_005: %d" % stdComp_s_005)
print("Compute Standard Deviation for stdComp_s_006: %d" % stdComp_s_006)

stdComp_s_007 = np.mean(s_007)
stdComp_s_008 = np.mean(s_008)
stdComp_s_009 = np.mean(s_009)
stdComp_s_010 = np.mean(s_010)
stdComp_s_011 = np.mean(s_011)
stdComp_s_012 = np.mean(s_012)
print("Compute Standard Deviation for stdComp_s_007: %d" % stdComp_s_007)
print("Compute Standard Deviation for stdComp_s_008: %d" % stdComp_s_008)
print("Compute Standard Deviation for stdComp_s_009: %d" % stdComp_s_009)
print("Compute Standard Deviation for stdComp_s_010: %d" % stdComp_s_010)
print("Compute Standard Deviation for stdComp_s_011: %d" % stdComp_s_011)
print("Compute Standard Deviation for stdComp_s_012: %d" % stdComp_s_012)
# ============================================== #

# ============================================== #
# Verification of the Mean:
mean_ver_s_001 = abs(mu_s_001 - stdComp_s_001) < stdToCompare
mean_ver_s_002 = abs(mu_s_002 - stdComp_s_002) < stdToCompare
mean_ver_s_003 = abs(mu_s_003 - stdComp_s_003) < stdToCompare
mean_ver_s_004 = abs(mu_s_004 - stdComp_s_004) < stdToCompare
mean_ver_s_005 = abs(mu_s_005 - stdComp_s_005) < stdToCompare
mean_ver_s_006 = abs(mu_s_006 - stdComp_s_006) < stdToCompare
print("Verification of the Mean for mean_ver_s_001: %r" % mean_ver_s_001)
print("Verification of the Mean for mean_ver_s_002: %r" % mean_ver_s_002)
print("Verification of the Mean for mean_ver_s_003: %r" % mean_ver_s_003)
print("Verification of the Mean for mean_ver_s_004: %r" % mean_ver_s_004)
print("Verification of the Mean for mean_ver_s_005: %r" % mean_ver_s_005)
print("Verification of the Mean for mean_ver_s_006: %r" % mean_ver_s_006)

mean_ver_s_007 = abs(mu_s_007 - stdComp_s_007) < stdToCompare
mean_ver_s_008 = abs(mu_s_008 - stdComp_s_008) < stdToCompare
mean_ver_s_009 = abs(mu_s_009 - stdComp_s_009) < stdToCompare
mean_ver_s_010 = abs(mu_s_010 - stdComp_s_010) < stdToCompare
mean_ver_s_011 = abs(mu_s_011 - stdComp_s_011) < stdToCompare
mean_ver_s_012 = abs(mu_s_012 - stdComp_s_012) < stdToCompare
print("Verification of the Mean for mean_ver_s_007: %r" % mean_ver_s_007)
print("Verification of the Mean for mean_ver_s_008: %r" % mean_ver_s_008)
print("Verification of the Mean for mean_ver_s_009: %r" % mean_ver_s_009)
print("Verification of the Mean for mean_ver_s_010: %r" % mean_ver_s_010)
print("Verification of the Mean for mean_ver_s_011: %r" % mean_ver_s_011)
print("Verification of the Mean for mean_ver_s_012: %r" % mean_ver_s_012)
# ============================================== #

# ============================================== #
# Compute Variance:
stdS_001 = np.std(s_001, ddof=1)
stdS_002 = np.std(s_002, ddof=1)
stdS_003 = np.std(s_003, ddof=1)
stdS_004 = np.std(s_004, ddof=1)
stdS_005 = np.std(s_005, ddof=1)
stdS_006 = np.std(s_006, ddof=1)
print("Compute Variance for stdS_001: %f" % stdS_001)
print("Compute Variance for stdS_002: %f" % stdS_002)
print("Compute Variance for stdS_003: %f" % stdS_003)
print("Compute Variance for stdS_004: %f" % stdS_004)
print("Compute Variance for stdS_005: %f" % stdS_005)
print("Compute Variance for stdS_006: %f" % stdS_006)

stdS_007 = np.std(s_007, ddof=1)
stdS_008 = np.std(s_008, ddof=1)
stdS_009 = np.std(s_009, ddof=1)
stdS_010 = np.std(s_010, ddof=1)
stdS_011 = np.std(s_011, ddof=1)
stdS_012 = np.std(s_012, ddof=1)
print("Compute Variance for stdS_007: %f" % stdS_007)
print("Compute Variance for stdS_008: %f" % stdS_008)
print("Compute Variance for stdS_009: %f" % stdS_009)
print("Compute Variance for stdS_010: %f" % stdS_010)
print("Compute Variance for stdS_011: %f" % stdS_011)
print("Compute Variance for stdS_012: %f" % stdS_012)
# ============================================== #

# ============================================== #
# Verification of the Variance:
variance_ver_s_001 = abs(sigma - stdS_001) < stdToCompare
variance_ver_s_002 = abs(sigma - stdS_002) < stdToCompare
variance_ver_s_003 = abs(sigma - stdS_003) < stdToCompare
variance_ver_s_004 = abs(sigma - stdS_004) < stdToCompare
variance_ver_s_005 = abs(sigma - stdS_005) < stdToCompare
variance_ver_s_006 = abs(sigma - stdS_006) < stdToCompare
print("Verification of the Variance for variance_ver_s_001: %r" % variance_ver_s_001)
print("Verification of the Variance for variance_ver_s_002: %r" % variance_ver_s_002)
print("Verification of the Variance for variance_ver_s_003: %r" % variance_ver_s_003)
print("Verification of the Variance for variance_ver_s_004: %r" % variance_ver_s_004)
print("Verification of the Variance for variance_ver_s_005: %r" % variance_ver_s_005)
print("Verification of the Variance for variance_ver_s_006: %r" % variance_ver_s_006)

variance_ver_s_007 = abs(sigma - stdS_007) < stdToCompare
variance_ver_s_008 = abs(sigma - stdS_008) < stdToCompare
variance_ver_s_009 = abs(sigma - stdS_009) < stdToCompare
variance_ver_s_010 = abs(sigma - stdS_010) < stdToCompare
variance_ver_s_011 = abs(sigma - stdS_011) < stdToCompare
variance_ver_s_012 = abs(sigma - stdS_012) < stdToCompare
print("Verification of the Variance for variance_ver_s_007: %r" % variance_ver_s_007)
print("Verification of the Variance for variance_ver_s_008: %r" % variance_ver_s_008)
print("Verification of the Variance for variance_ver_s_009: %r" % variance_ver_s_009)
print("Verification of the Variance for variance_ver_s_010: %r" % variance_ver_s_010)
print("Verification of the Variance for variance_ver_s_011: %r" % variance_ver_s_011)
print("Verification of the Variance for variance_ver_s_012: %r" % variance_ver_s_012)
# ============================================== #

# ============================================== #
# Normal Validation:
normalValidation_s_001 = stats.normaltest(s_001)
normalValidation_s_002 = stats.normaltest(s_002)
normalValidation_s_003 = stats.normaltest(s_003)
normalValidation_s_004 = stats.normaltest(s_004)
normalValidation_s_005 = stats.normaltest(s_005)
normalValidation_s_006 = stats.normaltest(s_006)
print(normalValidation_s_001)
print(normalValidation_s_002)
print(normalValidation_s_003)
print(normalValidation_s_004)
print(normalValidation_s_005)
print(normalValidation_s_006)

normalValidation_s_001 = stats.normaltest(s_007)
normalValidation_s_001 = stats.normaltest(s_008)
normalValidation_s_001 = stats.normaltest(s_009)
normalValidation_s_001 = stats.normaltest(s_010)
normalValidation_s_001 = stats.normaltest(s_011)
normalValidation_s_001 = stats.normaltest(s_012)
print(normalValidation_s_007)
print(normalValidation_s_008)
print(normalValidation_s_009)
print(normalValidation_s_010)
print(normalValidation_s_011)
print(normalValidation_s_012)
# ============================================== #

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                                                #
#                     ANOVA                      #
#                                                #
# ============================================== #

# ============================================== #
#            NASA-TLX: Mental Demand             #
# ============================================== #

F_fs_md, p_fs_md = stats.f_oneway(
  d_data_fs_md['intern_1'],
  d_data_fs_md['intern_2'],
  d_data_fs_md['junior_1'],
  d_data_fs_md['junior_2'],
  #d_data_fs_md['middle_1'],
  #d_data_fs_md['middle_2'],
  d_data_fs_md['senior_1']
  #d_data_fs_md['senior_2']
)

F_fm_md, p_fm_md = stats.f_oneway(
  d_data_fm_md['intern_1'],
  d_data_fm_md['intern_2'],
  d_data_fm_md['junior_1'],
  d_data_fm_md['junior_2'],
  #d_data_fs_md['middle_1'],
  #d_data_fs_md['middle_2'],
  d_data_fm_md['senior_1']
  #d_data_fs_md['senior_2']
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
  d_data_fs_pd['intern_1'],
  d_data_fs_pd['intern_2'],
  d_data_fs_pd['junior_1'],
  d_data_fs_pd['junior_2'],
  #d_data_fs_pd['middle_1'],
  #d_data_fs_pd['middle_2'],
  d_data_fs_pd['senior_1']
  #d_data_fs_pd['senior_2']
)

F_fm_pd, p_fm_pd = stats.f_oneway(
  d_data_fm_pd['intern_1'],
  d_data_fm_pd['intern_2'],
  d_data_fm_pd['junior_1'],
  d_data_fm_pd['junior_2'],
  #d_data_fs_pd['middle_1'],
  #d_data_fs_pd['middle_2'],
  d_data_fm_pd['senior_1']
  #d_data_fs_pd['senior_2']
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
  d_data_fs_td['intern_1'],
  d_data_fs_td['intern_2'],
  d_data_fs_td['junior_1'],
  d_data_fs_td['junior_2'],
  #d_data_fs_td['middle_1'],
  #d_data_fs_td['middle_2'],
  d_data_fs_td['senior_1']
  #d_data_fs_td['senior_2']
)

F_fm_td, p_fm_td = stats.f_oneway(
  d_data_fm_td['intern_1'],
  d_data_fm_td['intern_2'],
  d_data_fm_td['junior_1'],
  d_data_fm_td['junior_2'],
  #d_data_fs_td['middle_1'],
  #d_data_fs_td['middle_2'],
  d_data_fm_td['senior_1']
  #d_data_fs_td['senior_2']
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
  d_data_fs_p['intern_1'],
  d_data_fs_p['intern_2'],
  d_data_fs_p['junior_1'],
  d_data_fs_p['junior_2'],
  #d_data_fs_p['middle_1'],
  #d_data_fs_p['middle_2'],
  d_data_fs_p['senior_1']
  #d_data_fs_p['senior_2']
)

F_fm_p, p_fm_p = stats.f_oneway(
  d_data_fm_p['intern_1'],
  d_data_fm_p['intern_2'],
  d_data_fm_p['junior_1'],
  d_data_fm_p['junior_2'],
  #d_data_fs_p['middle_1'],
  #d_data_fs_p['middle_2'],
  d_data_fm_p['senior_1']
  #d_data_fs_p['senior_2']
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
  d_data_fs_e['intern_1'],
  d_data_fs_e['intern_2'],
  d_data_fs_e['junior_1'],
  d_data_fs_e['junior_2'],
  #d_data_fs_e['middle_1'],
  #d_data_fs_e['middle_2'],
  d_data_fs_e['senior_1']
  #d_data_fs_e['senior_2']
)

F_fm_e, p_fm_e = stats.f_oneway(
  d_data_fm_e['intern_1'],
  d_data_fm_e['intern_2'],
  d_data_fm_e['junior_1'],
  d_data_fm_e['junior_2'],
  #d_data_fs_e['middle_1'],
  #d_data_fs_e['middle_2'],
  d_data_fm_e['senior_1']
  #d_data_fs_e['senior_2']
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
  d_data_fs_f['intern_1'],
  d_data_fs_f['intern_2'],
  d_data_fs_f['junior_1'],
  d_data_fs_f['junior_2'],
  #d_data_fs_f['middle_1'],
  #d_data_fs_f['middle_2'],
  d_data_fs_f['senior_1']
  #d_data_fs_f['senior_2']
)

F_fm_f, p_fm_f = stats.f_oneway(
  d_data_fm_f['intern_1'],
  d_data_fm_f['intern_2'],
  d_data_fm_f['junior_1'],
  d_data_fm_f['junior_2'],
  #d_data_fs_f['middle_1'],
  #d_data_fs_f['middle_2'],
  d_data_fm_f['senior_1']
  #d_data_fs_f['senior_2']
)

print("Single-Modality (Frustration): F = %f" % (F_fs_f))
print("Single-Modality (Frustration): p = %f" % (p_fs_f))
print("Multi-Modality (Frustration): F = %f" % (F_fm_f))
print("Multi-Modality (Frustration): p = %f" % (p_fm_f))

# ============================================== #
# ============================================== #

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

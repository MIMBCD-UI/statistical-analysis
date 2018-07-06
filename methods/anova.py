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

sus_columns = [
  'sus_01',
  'sus_02',
  'sus_03',
  'sus_04',
  'sus_05',
  'sus_06',
  'sus_07',
  'sus_08',
  'sus_09',
  'sus_10',
]

measures_columns = [
  'time_94662',
  'time_607376',
  'time_737037',
  'time_total',
  'clicks_94662',
  'clicks_607376',
  'clicks_737037',
  'clicks_total',
  'errors_94662',
  'errors_607376',
  'errors_737037',
  'errors_total'
]

birads_columns = [
  'birads_94662',
  'birads_607376',
  'birads_737037'
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
createBoxplotFS(filterByColumn, sus_columns)
createBoxplotFS(filterByColumn, measures_columns)
createBoxplotFS(filterByColumn, birads_columns)

# ============================================== #
#                 MULTI-MODALITY                 #
# ============================================== #

def createBoxplotFM(filterBy, array):
  i = 0
  for i in range(len(array)):
    datafile_fm.boxplot(array[i], by=filterByColumn, figsize=(figSizeX, figSizeY))

createBoxplotFM(filterByColumn, nasatlx_columns)
createBoxplotFM(filterByColumn, sus_columns)
createBoxplotFM(filterByColumn, measures_columns)
createBoxplotFM(filterByColumn, birads_columns)

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

d_data_fs_sus_01 = {
  grp:datafile_fs['sus_01'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_sus_02 = {
  grp:datafile_fs['sus_02'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_sus_03 = {
  grp:datafile_fs['sus_03'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_sus_04 = {
  grp:datafile_fs['sus_04'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_sus_05 = {
  grp:datafile_fs['sus_05'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_sus_06 = {
  grp:datafile_fs['sus_06'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_sus_07 = {
  grp:datafile_fs['sus_07'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_sus_08 = {
  grp:datafile_fs['sus_08'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_sus_09 = {
  grp:datafile_fs['sus_09'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_sus_10 = {
  grp:datafile_fs['sus_10'][datafile_fs.group == grp]
  for grp in grps_fs
}






measures_columns = [
  'time_94662',
  'time_607376',
  'time_737037',
  'time_total',
  'clicks_94662',
  'clicks_607376',
  'clicks_737037',
  'clicks_total',
  'errors_94662',
  'errors_607376',
  'errors_737037',
  'errors_total'
]

birads_columns = [
  'birads_94662',
  'birads_607376',
  'birads_737037'
]

d_data_fs_time_94662 = {
  grp:datafile_fs['time_94662'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_time_607376 = {
  grp:datafile_fs['time_607376'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_time_737037 = {
  grp:datafile_fs['time_737037'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_time_total = {
  grp:datafile_fs['time_total'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_clicks_94662 = {
  grp:datafile_fs['clicks_94662'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_clicks_607376 = {
  grp:datafile_fs['clicks_607376'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_clicks_737037 = {
  grp:datafile_fs['clicks_737037'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_clicks_total = {
  grp:datafile_fs['clicks_total'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_errors_94662 = {
  grp:datafile_fs['errors_94662'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_errors_607376 = {
  grp:datafile_fs['errors_607376'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_errors_737037 = {
  grp:datafile_fs['errors_737037'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_errors_total = {
  grp:datafile_fs['errors_total'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_birads_94662 = {
  grp:datafile_fs['birads_94662'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_birads_607376 = {
  grp:datafile_fs['birads_607376'][datafile_fs.group == grp]
  for grp in grps_fs
}

d_data_fs_birads_737037 = {
  grp:datafile_fs['birads_737037'][datafile_fs.group == grp]
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

d_data_fm_sus_01 = {
  grp:datafile_fm['sus_01'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_sus_02 = {
  grp:datafile_fm['sus_02'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_sus_03 = {
  grp:datafile_fm['sus_03'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_sus_04 = {
  grp:datafile_fm['sus_04'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_sus_05 = {
  grp:datafile_fm['sus_05'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_sus_06 = {
  grp:datafile_fm['sus_06'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_sus_07 = {
  grp:datafile_fm['sus_07'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_sus_08 = {
  grp:datafile_fm['sus_08'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_sus_09 = {
  grp:datafile_fm['sus_09'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_sus_10 = {
  grp:datafile_fm['sus_10'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_time_94662 = {
  grp:datafile_fm['time_94662'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_time_607376 = {
  grp:datafile_fm['time_607376'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_time_737037 = {
  grp:datafile_fm['time_737037'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_time_total = {
  grp:datafile_fm['time_total'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_clicks_94662 = {
  grp:datafile_fm['clicks_94662'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_clicks_607376 = {
  grp:datafile_fm['clicks_607376'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_clicks_737037 = {
  grp:datafile_fm['clicks_737037'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_clicks_total = {
  grp:datafile_fm['clicks_total'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_errors_94662 = {
  grp:datafile_fm['errors_94662'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_errors_607376 = {
  grp:datafile_fm['errors_607376'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_errors_737037 = {
  grp:datafile_fm['errors_737037'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_errors_total = {
  grp:datafile_fm['errors_total'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_birads_94662 = {
  grp:datafile_fm['birads_94662'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_birads_607376 = {
  grp:datafile_fm['birads_607376'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_birads_737037 = {
  grp:datafile_fm['birads_737037'][datafile_fm.group == grp]
  for grp in grps_fm
}

# ============================================== #
# ============================================== #

k_fs = len(pd.unique(datafile_fs.group))  # number of conditions
N_fs = len(datafile_fs.values)  # conditions times participants
n_fs = datafile_fs.groupby('group').size()[0] #Participants in each condition

k_fm = len(pd.unique(datafile_fm.group))  # number of conditions
N_fm = len(datafile_fm.values)  # conditions times participants
n_fm = datafile_fm.groupby('group').size()[0] #Participants in each condition

# ============================================== #
#                                                #
#      IS IT NORMAL (GAUSSIAN) DISTRIBUTION?     #
#                                                #
# ============================================== #

s_Number = 62

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

# ============================================== #

s_013 = datafile_fs.sus_01[:MV_N].tolist()
s_014 = datafile_fs.sus_02[:MV_N].tolist()
s_015 = datafile_fs.sus_03[:MV_N].tolist()
s_016 = datafile_fs.sus_04[:MV_N].tolist()
s_017 = datafile_fs.sus_05[:MV_N].tolist()
s_018 = datafile_fs.sus_06[:MV_N].tolist()
s_019 = datafile_fs.sus_07[:MV_N].tolist()
s_020 = datafile_fs.sus_08[:MV_N].tolist()
s_021 = datafile_fs.sus_09[:MV_N].tolist()
s_022 = datafile_fs.sus_10[:MV_N].tolist()

s_023 = datafile_fm.sus_01[:MV_N].tolist()
s_024 = datafile_fm.sus_02[:MV_N].tolist()
s_025 = datafile_fm.sus_03[:MV_N].tolist()
s_026 = datafile_fm.sus_04[:MV_N].tolist()
s_027 = datafile_fm.sus_05[:MV_N].tolist()
s_028 = datafile_fm.sus_06[:MV_N].tolist()
s_029 = datafile_fm.sus_07[:MV_N].tolist()
s_030 = datafile_fm.sus_08[:MV_N].tolist()
s_031 = datafile_fm.sus_09[:MV_N].tolist()
s_032 = datafile_fm.sus_10[:MV_N].tolist()

# ============================================== #

s_033 = datafile_fs.time_94662[:MV_N].tolist()
s_034 = datafile_fs.time_607376[:MV_N].tolist()
s_035 = datafile_fs.time_737037[:MV_N].tolist()
s_036 = datafile_fs.time_total[:MV_N].tolist()

s_037 = datafile_fs.clicks_94662[:MV_N].tolist()
s_038 = datafile_fs.clicks_607376[:MV_N].tolist()
s_039 = datafile_fs.clicks_737037[:MV_N].tolist()
s_040 = datafile_fs.clicks_total[:MV_N].tolist()

s_041 = datafile_fs.errors_94662[:MV_N].tolist()
s_042 = datafile_fs.errors_607376[:MV_N].tolist()
s_043 = datafile_fs.errors_737037[:MV_N].tolist()
s_044 = datafile_fs.errors_total[:MV_N].tolist()

s_045 = datafile_fs.birads_94662[:MV_N].tolist()
s_046 = datafile_fs.birads_607376[:MV_N].tolist()
s_047 = datafile_fs.birads_737037[:MV_N].tolist()

# ============================================== #

s_048 = datafile_fm.time_94662[:MV_N].tolist()
s_049 = datafile_fm.time_607376[:MV_N].tolist()
s_050 = datafile_fm.time_737037[:MV_N].tolist()
s_051 = datafile_fm.time_total[:MV_N].tolist()

s_052 = datafile_fm.clicks_94662[:MV_N].tolist()
s_053 = datafile_fm.clicks_607376[:MV_N].tolist()
s_054 = datafile_fm.clicks_737037[:MV_N].tolist()
s_055 = datafile_fm.clicks_total[:MV_N].tolist()

s_056 = datafile_fm.errors_94662[:MV_N].tolist()
s_057 = datafile_fm.errors_607376[:MV_N].tolist()
s_058 = datafile_fm.errors_737037[:MV_N].tolist()
s_059 = datafile_fm.errors_total[:MV_N].tolist()

s_060 = datafile_fm.birads_94662[:MV_N].tolist()
s_061 = datafile_fm.birads_607376[:MV_N].tolist()
s_062 = datafile_fm.birads_737037[:MV_N].tolist()

# ============================================== #

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

mu_s_013 = np.mean(s_013, axis=0)
mu_s_014 = np.mean(s_014, axis=0)
mu_s_015 = np.mean(s_015, axis=0)
mu_s_016 = np.mean(s_016, axis=0)
mu_s_017 = np.mean(s_017, axis=0)
mu_s_018 = np.mean(s_018, axis=0)
mu_s_019 = np.mean(s_019, axis=0)
mu_s_020 = np.mean(s_020, axis=0)
mu_s_021 = np.mean(s_021, axis=0)
mu_s_022 = np.mean(s_022, axis=0)

mu_s_023 = np.mean(s_023, axis=0)
mu_s_024 = np.mean(s_024, axis=0)
mu_s_025 = np.mean(s_025, axis=0)
mu_s_026 = np.mean(s_026, axis=0)
mu_s_027 = np.mean(s_027, axis=0)
mu_s_028 = np.mean(s_028, axis=0)
mu_s_029 = np.mean(s_029, axis=0)
mu_s_030 = np.mean(s_030, axis=0)
mu_s_031 = np.mean(s_031, axis=0)
mu_s_032 = np.mean(s_032, axis=0)

mu_s_033 = np.mean(s_033, axis=0)
mu_s_034 = np.mean(s_034, axis=0)
mu_s_035 = np.mean(s_035, axis=0)
mu_s_036 = np.mean(s_036, axis=0)

mu_s_037 = np.mean(s_037, axis=0)
mu_s_038 = np.mean(s_038, axis=0)
mu_s_039 = np.mean(s_039, axis=0)
mu_s_040 = np.mean(s_040, axis=0)

mu_s_041 = np.mean(s_041, axis=0)
mu_s_042 = np.mean(s_042, axis=0)
mu_s_043 = np.mean(s_043, axis=0)
mu_s_044 = np.mean(s_044, axis=0)

mu_s_045 = np.mean(s_045, axis=0)
mu_s_046 = np.mean(s_046, axis=0)
mu_s_047 = np.mean(s_047, axis=0)
mu_s_048 = np.mean(s_048, axis=0)

mu_s_049 = np.mean(s_049, axis=0)
mu_s_050 = np.mean(s_050, axis=0)
mu_s_051 = np.mean(s_051, axis=0)
mu_s_052 = np.mean(s_052, axis=0)

mu_s_053 = np.mean(s_053, axis=0)
mu_s_054 = np.mean(s_054, axis=0)
mu_s_055 = np.mean(s_055, axis=0)
mu_s_056 = np.mean(s_056, axis=0)

mu_s_057 = np.mean(s_057, axis=0)
mu_s_058 = np.mean(s_058, axis=0)
mu_s_059 = np.mean(s_059, axis=0)

mu_s_060 = np.mean(s_060, axis=0)
mu_s_061 = np.mean(s_061, axis=0)
mu_s_062 = np.mean(s_062, axis=0)
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

stdComp_s_013 = np.mean(s_013)
stdComp_s_014 = np.mean(s_014)
stdComp_s_015 = np.mean(s_015)
stdComp_s_016 = np.mean(s_016)
stdComp_s_017 = np.mean(s_017)
stdComp_s_018 = np.mean(s_018)
stdComp_s_019 = np.mean(s_019)
stdComp_s_020 = np.mean(s_020)
stdComp_s_021 = np.mean(s_021)
stdComp_s_022 = np.mean(s_022)
print("Compute Standard Deviation for stdComp_s_013: %d" % stdComp_s_013)
print("Compute Standard Deviation for stdComp_s_014: %d" % stdComp_s_014)
print("Compute Standard Deviation for stdComp_s_015: %d" % stdComp_s_015)
print("Compute Standard Deviation for stdComp_s_016: %d" % stdComp_s_016)
print("Compute Standard Deviation for stdComp_s_017: %d" % stdComp_s_017)
print("Compute Standard Deviation for stdComp_s_018: %d" % stdComp_s_018)
print("Compute Standard Deviation for stdComp_s_019: %d" % stdComp_s_019)
print("Compute Standard Deviation for stdComp_s_020: %d" % stdComp_s_020)
print("Compute Standard Deviation for stdComp_s_021: %d" % stdComp_s_021)
print("Compute Standard Deviation for stdComp_s_022: %d" % stdComp_s_022)

stdComp_s_023 = np.mean(s_023)
stdComp_s_024 = np.mean(s_024)
stdComp_s_025 = np.mean(s_025)
stdComp_s_026 = np.mean(s_026)
stdComp_s_027 = np.mean(s_027)
stdComp_s_028 = np.mean(s_028)
stdComp_s_029 = np.mean(s_029)
stdComp_s_030 = np.mean(s_030)
stdComp_s_031 = np.mean(s_031)
stdComp_s_032 = np.mean(s_032)
print("Compute Standard Deviation for stdComp_s_023: %d" % stdComp_s_023)
print("Compute Standard Deviation for stdComp_s_024: %d" % stdComp_s_024)
print("Compute Standard Deviation for stdComp_s_025: %d" % stdComp_s_025)
print("Compute Standard Deviation for stdComp_s_026: %d" % stdComp_s_026)
print("Compute Standard Deviation for stdComp_s_027: %d" % stdComp_s_027)
print("Compute Standard Deviation for stdComp_s_028: %d" % stdComp_s_028)
print("Compute Standard Deviation for stdComp_s_029: %d" % stdComp_s_029)
print("Compute Standard Deviation for stdComp_s_030: %d" % stdComp_s_030)
print("Compute Standard Deviation for stdComp_s_031: %d" % stdComp_s_031)
print("Compute Standard Deviation for stdComp_s_032: %d" % stdComp_s_032)

stdComp_s_033 = np.mean(s_033)
stdComp_s_034 = np.mean(s_034)
stdComp_s_035 = np.mean(s_035)
stdComp_s_036 = np.mean(s_036)
print("Compute Standard Deviation for stdComp_s_033: %d" % stdComp_s_033)
print("Compute Standard Deviation for stdComp_s_034: %d" % stdComp_s_034)
print("Compute Standard Deviation for stdComp_s_035: %d" % stdComp_s_035)
print("Compute Standard Deviation for stdComp_s_036: %d" % stdComp_s_036)

stdComp_s_037 = np.mean(s_037)
stdComp_s_038 = np.mean(s_038)
stdComp_s_039 = np.mean(s_039)
stdComp_s_040 = np.mean(s_040)
print("Compute Standard Deviation for stdComp_s_037: %d" % stdComp_s_037)
print("Compute Standard Deviation for stdComp_s_038: %d" % stdComp_s_038)
print("Compute Standard Deviation for stdComp_s_039: %d" % stdComp_s_039)
print("Compute Standard Deviation for stdComp_s_040: %d" % stdComp_s_040)

stdComp_s_041 = np.mean(s_041)
stdComp_s_042 = np.mean(s_042)
stdComp_s_043 = np.mean(s_043)
stdComp_s_044 = np.mean(s_044)
print("Compute Standard Deviation for stdComp_s_041: %d" % stdComp_s_041)
print("Compute Standard Deviation for stdComp_s_042: %d" % stdComp_s_042)
print("Compute Standard Deviation for stdComp_s_043: %d" % stdComp_s_043)
print("Compute Standard Deviation for stdComp_s_044: %d" % stdComp_s_044)

stdComp_s_045 = np.mean(s_045)
stdComp_s_046 = np.mean(s_046)
stdComp_s_047 = np.mean(s_047)
stdComp_s_048 = np.mean(s_048)
print("Compute Standard Deviation for stdComp_s_045: %d" % stdComp_s_045)
print("Compute Standard Deviation for stdComp_s_046: %d" % stdComp_s_046)
print("Compute Standard Deviation for stdComp_s_047: %d" % stdComp_s_047)
print("Compute Standard Deviation for stdComp_s_048: %d" % stdComp_s_048)

stdComp_s_049 = np.mean(s_049)
stdComp_s_050 = np.mean(s_050)
stdComp_s_051 = np.mean(s_051)
stdComp_s_052 = np.mean(s_052)
print("Compute Standard Deviation for stdComp_s_049: %d" % stdComp_s_049)
print("Compute Standard Deviation for stdComp_s_050: %d" % stdComp_s_050)
print("Compute Standard Deviation for stdComp_s_051: %d" % stdComp_s_051)
print("Compute Standard Deviation for stdComp_s_052: %d" % stdComp_s_052)

stdComp_s_053 = np.mean(s_053)
stdComp_s_054 = np.mean(s_054)
stdComp_s_055 = np.mean(s_055)
stdComp_s_056 = np.mean(s_056)
print("Compute Standard Deviation for stdComp_s_053: %d" % stdComp_s_053)
print("Compute Standard Deviation for stdComp_s_054: %d" % stdComp_s_054)
print("Compute Standard Deviation for stdComp_s_055: %d" % stdComp_s_055)
print("Compute Standard Deviation for stdComp_s_056: %d" % stdComp_s_056)

stdComp_s_057 = np.mean(s_057)
stdComp_s_058 = np.mean(s_058)
stdComp_s_059 = np.mean(s_059)
print("Compute Standard Deviation for stdComp_s_057: %d" % stdComp_s_057)
print("Compute Standard Deviation for stdComp_s_058: %d" % stdComp_s_058)
print("Compute Standard Deviation for stdComp_s_059: %d" % stdComp_s_059)

stdComp_s_060 = np.mean(s_060)
stdComp_s_061 = np.mean(s_061)
stdComp_s_062 = np.mean(s_062)
print("Compute Standard Deviation for stdComp_s_060: %d" % stdComp_s_060)
print("Compute Standard Deviation for stdComp_s_061: %d" % stdComp_s_061)
print("Compute Standard Deviation for stdComp_s_062: %d" % stdComp_s_062)
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
#                                                #
#              NORMAL VALIDATION                 #
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
print(normalValidation_s_001)
print(normalValidation_s_002)
print(normalValidation_s_003)
print(normalValidation_s_004)
print(normalValidation_s_005)
print(normalValidation_s_006)

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
print(normalValidation_s_007)
print(normalValidation_s_008)
print(normalValidation_s_009)
print(normalValidation_s_010)
print(normalValidation_s_011)
print(normalValidation_s_012)

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
print(normalValidation_s_013)
print(normalValidation_s_014)
print(normalValidation_s_015)
print(normalValidation_s_016)
print(normalValidation_s_017)
print(normalValidation_s_018)
print(normalValidation_s_019)
print(normalValidation_s_020)
print(normalValidation_s_021)
print(normalValidation_s_022)

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
print(normalValidation_s_023)
print(normalValidation_s_024)
print(normalValidation_s_025)
print(normalValidation_s_026)
print(normalValidation_s_027)
print(normalValidation_s_028)
print(normalValidation_s_029)
print(normalValidation_s_030)
print(normalValidation_s_031)
print(normalValidation_s_032)

# ============================================== #
# ============================================== #

# ============================================== #
#            TIME: Single-Modality               #
# ============================================== #

normalValidation_s_033 = stats.normaltest(s_033)
normalValidation_s_034 = stats.normaltest(s_034)
normalValidation_s_035 = stats.normaltest(s_035)
normalValidation_s_036 = stats.normaltest(s_036)
print(normalValidation_s_033)
print(normalValidation_s_034)
print(normalValidation_s_035)
print(normalValidation_s_036)

# ============================================== #
# ============================================== #

# ============================================== #
#            TIME: Multi-Modality                #
# ============================================== #

normalValidation_s_037 = stats.normaltest(s_037)
normalValidation_s_038 = stats.normaltest(s_038)
normalValidation_s_039 = stats.normaltest(s_039)
normalValidation_s_040 = stats.normaltest(s_040)
print(normalValidation_s_037)
print(normalValidation_s_038)
print(normalValidation_s_039)
print(normalValidation_s_040)

# ============================================== #
# ============================================== #

# ============================================== #
#            CLICKS: Single-Modality             #
# ============================================== #

normalValidation_s_041 = stats.normaltest(s_041)
normalValidation_s_042 = stats.normaltest(s_042)
normalValidation_s_043 = stats.normaltest(s_043)
normalValidation_s_044 = stats.normaltest(s_044)
print(normalValidation_s_041)
print(normalValidation_s_042)
print(normalValidation_s_043)
print(normalValidation_s_044)

# ============================================== #
# ============================================== #

# ============================================== #
#            CLICKS: Multi-Modality              #
# ============================================== #

normalValidation_s_045 = stats.normaltest(s_045)
normalValidation_s_046 = stats.normaltest(s_046)
normalValidation_s_047 = stats.normaltest(s_047)
normalValidation_s_048 = stats.normaltest(s_048)
print(normalValidation_s_045)
print(normalValidation_s_046)
print(normalValidation_s_047)
print(normalValidation_s_048)

# ============================================== #
# ============================================== #

# ============================================== #
#            ERRORS: Single-Modality             #
# ============================================== #

normalValidation_s_049 = stats.normaltest(s_049)
normalValidation_s_050 = stats.normaltest(s_050)
normalValidation_s_051 = stats.normaltest(s_051)
normalValidation_s_052 = stats.normaltest(s_052)
print(normalValidation_s_049)
print(normalValidation_s_050)
print(normalValidation_s_051)
print(normalValidation_s_052)

# ============================================== #
# ============================================== #

# ============================================== #
#            ERRORS: Multi-Modality              #
# ============================================== #

normalValidation_s_053 = stats.normaltest(s_053)
normalValidation_s_054 = stats.normaltest(s_054)
normalValidation_s_055 = stats.normaltest(s_055)
normalValidation_s_056 = stats.normaltest(s_056)
print(normalValidation_s_053)
print(normalValidation_s_054)
print(normalValidation_s_055)
print(normalValidation_s_056)

# ============================================== #
# ============================================== #

# ============================================== #
#            BIRADS: Single-Modality             #
# ============================================== #

normalValidation_s_057 = stats.normaltest(s_057)
normalValidation_s_058 = stats.normaltest(s_058)
normalValidation_s_059 = stats.normaltest(s_059)
print(normalValidation_s_057)
print(normalValidation_s_058)
print(normalValidation_s_059)

# ============================================== #
# ============================================== #

# ============================================== #
#            BIRADS: MULTI-Modality              #
# ============================================== #

normalValidation_s_060 = stats.normaltest(s_060)
normalValidation_s_061 = stats.normaltest(s_061)
normalValidation_s_062 = stats.normaltest(s_062)
print(normalValidation_s_060)
print(normalValidation_s_061)
print(normalValidation_s_062)

# ============================================== #
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

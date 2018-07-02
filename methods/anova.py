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

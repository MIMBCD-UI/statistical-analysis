#!/usr/bin/env python

"""dataFileGroups.py: Set of Data Files grouping it by Groups
                      of selecting data."""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "ACADEMIC & COMMERCIAL"
__version__     = "1.0.0"
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
joinPath = os.path.join(pathDirname, '..', '..', '..')
pathAbsPath = os.path.abspath(joinPath)

sa_techniques_dir = (pathAbsPath + '/statistical-analysis/src/techniques/')
sa_constants_dir = (pathAbsPath + '/statistical-analysis/src/constants/')
sa_methods_dir = (pathAbsPath + '/statistical-analysis/src/methods/')
src_dir = (pathAbsPath + '/sheet-reader/src/core')
constants_dir = (pathAbsPath + '/sheet-reader/src/constants/')
techniques_dir = (pathAbsPath + '/sheet-reader/src/techniques/')

sys.path.append(sa_techniques_dir)
sys.path.append(sa_constants_dir)
sys.path.append(sa_methods_dir)
sys.path.append(src_dir)
sys.path.append(constants_dir)
sys.path.append(techniques_dir)

import sheets
import iterators

datafileIteratorPerGroup = iterators.datafileIteratorPerGroup

main_sheet_dir = pathAbsPath + '/sheet-reader/data/temp/main_sheet.csv'
fs_sheet_dir = pathAbsPath + '/sheet-reader/data/temp/fs_sheet.csv'
fm_sheet_dir = pathAbsPath + '/sheet-reader/data/temp/fm_sheet.csv'

import pandas as pd
import scipy
from scipy import stats

# ============================================== #
#                                                #
#                    CREATORS                    #
#                                                #
# ============================================== #

datafile_fs = sheets.datafile_fs
datafile_fm = sheets.datafile_fm

# ============================================== #
#               DATAFILE ITERATORS               #
# ============================================== #

datafile_fs_list = datafileIteratorPerGroup(datafile_fs)
datafile_fm_list = datafileIteratorPerGroup(datafile_fm)

# ============================================== #
# ============================================== #

# ============================================== #
#                 INITIALIZATION                 #
# ============================================== #

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
  grp:datafile_fm['mental_demand'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_pd = {
  grp:datafile_fm['physical_demand'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_td = {
  grp:datafile_fm['temporal_demand'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_p = {
  grp:datafile_fm['performance'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_e = {
  grp:datafile_fm['effort'][datafile_fm.group == grp]
  for grp in grps_fm
}

d_data_fm_f = {
  grp:datafile_fm['frustration'][datafile_fm.group == grp]
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

# ============================================== #
#             DATA FRAMES: Grouping              #
# ============================================== #

# ==================== SUS ===================== #

d_data_fs_sus_intern_arr = d_data_fs_sus_01['intern'] + d_data_fs_sus_02['intern'] + d_data_fs_sus_03['intern'] + d_data_fs_sus_04['intern'] + d_data_fs_sus_05['intern'] + d_data_fs_sus_06['intern'] + d_data_fs_sus_07['intern'] + d_data_fs_sus_08['intern'] + d_data_fs_sus_09['intern'] + d_data_fs_sus_10['intern']

d_data_fs_sus_junior_arr = d_data_fs_sus_01['junior'] + d_data_fs_sus_02['junior'] + d_data_fs_sus_03['junior'] + d_data_fs_sus_04['junior'] + d_data_fs_sus_05['junior'] + d_data_fs_sus_06['junior'] + d_data_fs_sus_07['junior'] + d_data_fs_sus_08['junior'] + d_data_fs_sus_09['junior'] + d_data_fs_sus_10['junior']

d_data_fs_sus_middle_arr = d_data_fs_sus_01['middle'] + d_data_fs_sus_02['middle'] + d_data_fs_sus_03['middle'] + d_data_fs_sus_04['middle'] + d_data_fs_sus_05['middle'] + d_data_fs_sus_06['middle'] + d_data_fs_sus_07['middle'] + d_data_fs_sus_08['middle'] + d_data_fs_sus_09['middle'] + d_data_fs_sus_10['middle']

d_data_fs_sus_senior_arr = d_data_fs_sus_01['senior'] + d_data_fs_sus_02['senior'] + d_data_fs_sus_03['senior'] + d_data_fs_sus_04['senior'] + d_data_fs_sus_05['senior'] + d_data_fs_sus_06['senior'] + d_data_fs_sus_07['senior'] + d_data_fs_sus_08['senior'] + d_data_fs_sus_09['senior'] + d_data_fs_sus_10['senior']

d_data_fs_sus_intern_list = list(d_data_fs_sus_intern_arr)
d_data_fs_sus_junior_list = list(d_data_fs_sus_junior_arr)
d_data_fs_sus_middle_list = list(d_data_fs_sus_middle_arr)
d_data_fs_sus_senior_list = list(d_data_fs_sus_senior_arr)

df_fs_sus_groups = {
  'intern': d_data_fs_sus_intern_arr,
  'junior': d_data_fs_sus_junior_arr,
  'middle': d_data_fs_sus_middle_arr,
  'senior': d_data_fs_sus_senior_arr
}

d_data_fm_sus_intern_arr = d_data_fm_sus_01['intern'] + d_data_fm_sus_02['intern'] + d_data_fm_sus_03['intern'] + d_data_fm_sus_04['intern'] + d_data_fm_sus_05['intern'] + d_data_fm_sus_06['intern'] + d_data_fm_sus_07['intern'] + d_data_fm_sus_08['intern'] + d_data_fm_sus_09['intern'] + d_data_fm_sus_10['intern']

d_data_fm_sus_junior_arr = d_data_fm_sus_01['junior'] + d_data_fm_sus_02['junior'] + d_data_fm_sus_03['junior'] + d_data_fm_sus_04['junior'] + d_data_fm_sus_05['junior'] + d_data_fm_sus_06['junior'] + d_data_fm_sus_07['junior'] + d_data_fm_sus_08['junior'] + d_data_fm_sus_09['junior'] + d_data_fm_sus_10['junior']

d_data_fm_sus_middle_arr = d_data_fm_sus_01['middle'] + d_data_fm_sus_02['middle'] + d_data_fm_sus_03['middle'] + d_data_fm_sus_04['middle'] + d_data_fm_sus_05['middle'] + d_data_fm_sus_06['middle'] + d_data_fm_sus_07['middle'] + d_data_fm_sus_08['middle'] + d_data_fm_sus_09['middle'] + d_data_fm_sus_10['middle']

d_data_fm_sus_senior_arr = d_data_fm_sus_01['senior'] + d_data_fm_sus_02['senior'] + d_data_fm_sus_03['senior'] + d_data_fm_sus_04['senior'] + d_data_fm_sus_05['senior'] + d_data_fm_sus_06['senior'] + d_data_fm_sus_07['senior'] + d_data_fm_sus_08['senior'] + d_data_fm_sus_09['senior'] + d_data_fm_sus_10['senior']

d_data_fm_sus_intern_list = list(d_data_fm_sus_intern_arr)
d_data_fm_sus_junior_list = list(d_data_fm_sus_junior_arr)
d_data_fm_sus_middle_list = list(d_data_fm_sus_middle_arr)
d_data_fm_sus_senior_list = list(d_data_fm_sus_senior_arr)

df_fm_sus_groups = {
  'intern': d_data_fm_sus_intern_arr,
  'junior': d_data_fm_sus_junior_arr,
  'middle': d_data_fm_sus_middle_arr,
  'senior': d_data_fm_sus_senior_arr
}

pd_df_fs = pd.DataFrame(df_fs_sus_groups)
pd_df_fm = pd.DataFrame(df_fm_sus_groups)

# ============================================== #

# ================= NASA-TLX =================== #

d_data_fs_nasatlx_intern_arr = d_data_fs_md['intern'] + d_data_fs_pd['intern'] + d_data_fs_td['intern'] + d_data_fs_p['intern'] + d_data_fs_e['intern'] + d_data_fs_f['intern']

d_data_fs_nasatlx_junior_arr = d_data_fs_md['junior'] + d_data_fs_pd['junior'] + d_data_fs_td['junior'] + d_data_fs_p['junior'] + d_data_fs_e['junior'] + d_data_fs_f['junior']

d_data_fs_nasatlx_middle_arr = d_data_fs_md['middle'] + d_data_fs_pd['middle'] + d_data_fs_td['middle'] + d_data_fs_p['middle'] + d_data_fs_e['middle'] + d_data_fs_f['middle']

d_data_fs_nasatlx_senior_arr = d_data_fs_md['senior'] + d_data_fs_pd['senior'] + d_data_fs_td['senior'] + d_data_fs_p['senior'] + d_data_fs_e['senior'] + d_data_fs_f['senior']

d_data_fs_nasatlx_intern_list = list(d_data_fs_nasatlx_intern_arr)
d_data_fs_nasatlx_junior_list = list(d_data_fs_nasatlx_junior_arr)
d_data_fs_nasatlx_middle_list = list(d_data_fs_nasatlx_middle_arr)
d_data_fs_nasatlx_senior_list = list(d_data_fs_nasatlx_senior_arr)

df_fs_nasatlx_groups = {
  'intern': d_data_fs_nasatlx_intern_arr,
  'junior': d_data_fs_nasatlx_junior_arr,
  'middle': d_data_fs_nasatlx_middle_arr,
  'senior': d_data_fs_nasatlx_senior_arr
}

d_data_fm_nasatlx_intern_arr = d_data_fm_md['intern'] + d_data_fm_pd['intern'] + d_data_fm_td['intern'] + d_data_fm_p['intern'] + d_data_fm_e['intern'] + d_data_fm_f['intern']

d_data_fm_nasatlx_junior_arr = d_data_fm_md['junior'] + d_data_fm_pd['junior'] + d_data_fm_td['junior'] + d_data_fm_p['junior'] + d_data_fm_e['junior'] + d_data_fm_f['junior']

d_data_fm_nasatlx_middle_arr = d_data_fm_md['middle'] + d_data_fm_pd['middle'] + d_data_fm_td['middle'] + d_data_fm_p['middle'] + d_data_fm_e['middle'] + d_data_fm_f['middle']

d_data_fm_nasatlx_senior_arr = d_data_fm_md['senior'] + d_data_fm_pd['senior'] + d_data_fm_td['senior'] + d_data_fm_p['senior'] + d_data_fm_e['senior'] + d_data_fm_f['senior']

d_data_fm_nasatlx_intern_list = list(d_data_fm_nasatlx_intern_arr)
d_data_fm_nasatlx_junior_list = list(d_data_fm_nasatlx_junior_arr)
d_data_fm_nasatlx_middle_list = list(d_data_fm_nasatlx_middle_arr)
d_data_fm_nasatlx_senior_list = list(d_data_fm_nasatlx_senior_arr)

df_fm_nasatlx_groups = {
  'intern': d_data_fm_nasatlx_intern_arr,
  'junior': d_data_fm_nasatlx_junior_arr,
  'middle': d_data_fm_nasatlx_middle_arr,
  'senior': d_data_fm_nasatlx_senior_arr
}

# ============================================== #

# =================== TIME ===================== #

d_data_fs_time_intern_arr = d_data_fs_time_94662['intern'] + d_data_fs_time_607376['intern'] + d_data_fs_time_737037['intern']

d_data_fs_time_junior_arr = d_data_fs_time_94662['junior'] + d_data_fs_time_607376['junior'] + d_data_fs_time_737037['junior']

d_data_fs_time_middle_arr = d_data_fs_time_94662['middle'] + d_data_fs_time_607376['middle'] + d_data_fs_time_737037['middle']

d_data_fs_time_senior_arr = d_data_fs_time_94662['senior'] + d_data_fs_time_607376['senior'] + d_data_fs_time_737037['senior']

d_data_fs_time_intern_list = list(d_data_fs_time_intern_arr)
d_data_fs_time_junior_list = list(d_data_fs_time_junior_arr)
d_data_fs_time_middle_list = list(d_data_fs_time_middle_arr)
d_data_fs_time_senior_list = list(d_data_fs_time_senior_arr)

df_fs_time_groups = {
  'intern': d_data_fs_time_intern_arr,
  'junior': d_data_fs_time_junior_arr,
  'middle': d_data_fs_time_middle_arr,
  'senior': d_data_fs_time_senior_arr
}

d_data_fm_time_intern_arr = d_data_fm_time_94662['intern'] + d_data_fm_time_607376['intern'] + d_data_fm_time_737037['intern']

d_data_fm_time_junior_arr = d_data_fm_time_94662['junior'] + d_data_fm_time_607376['junior'] + d_data_fm_time_737037['junior']

d_data_fm_time_middle_arr = d_data_fm_time_94662['middle'] + d_data_fm_time_607376['middle'] + d_data_fm_time_737037['middle']

d_data_fm_time_senior_arr = d_data_fm_time_94662['senior'] + d_data_fm_time_607376['senior'] + d_data_fm_time_737037['senior']

d_data_fm_time_intern_list = list(d_data_fm_time_intern_arr)
d_data_fm_time_junior_list = list(d_data_fm_time_junior_arr)
d_data_fm_time_middle_list = list(d_data_fm_time_middle_arr)
d_data_fm_time_senior_list = list(d_data_fm_time_senior_arr)

df_fm_time_groups = {
  'intern': d_data_fm_time_intern_arr,
  'junior': d_data_fm_time_junior_arr,
  'middle': d_data_fm_time_middle_arr,
  'senior': d_data_fm_time_senior_arr
}

# ============================================== #

# ================== CLICKS ==================== #

d_data_fs_clicks_intern_arr = d_data_fs_clicks_94662['intern'] + d_data_fs_clicks_607376['intern'] + d_data_fs_clicks_737037['intern']

d_data_fs_clicks_junior_arr = d_data_fs_clicks_94662['junior'] + d_data_fs_clicks_607376['junior'] + d_data_fs_clicks_737037['junior']

d_data_fs_clicks_middle_arr = d_data_fs_clicks_94662['middle'] + d_data_fs_clicks_607376['middle'] + d_data_fs_clicks_737037['middle']

d_data_fs_clicks_senior_arr = d_data_fs_clicks_94662['senior'] + d_data_fs_clicks_607376['senior'] + d_data_fs_clicks_737037['senior']

d_data_fs_clicks_intern_list = list(d_data_fs_clicks_intern_arr)
d_data_fs_clicks_junior_list = list(d_data_fs_clicks_junior_arr)
d_data_fs_clicks_middle_list = list(d_data_fs_clicks_middle_arr)
d_data_fs_clicks_senior_list = list(d_data_fs_clicks_senior_arr)

df_fs_clicks_groups = {
  'intern': d_data_fs_clicks_intern_arr,
  'junior': d_data_fs_clicks_junior_arr,
  'middle': d_data_fs_clicks_middle_arr,
  'senior': d_data_fs_clicks_senior_arr
}

d_data_fm_clicks_intern_arr = d_data_fm_clicks_94662['intern'] + d_data_fm_clicks_607376['intern'] + d_data_fm_clicks_737037['intern']

d_data_fm_clicks_junior_arr = d_data_fm_clicks_94662['junior'] + d_data_fm_clicks_607376['junior'] + d_data_fm_clicks_737037['junior']

d_data_fm_clicks_middle_arr = d_data_fm_clicks_94662['middle'] + d_data_fm_clicks_607376['middle'] + d_data_fm_clicks_737037['middle']

d_data_fm_clicks_senior_arr = d_data_fm_clicks_94662['senior'] + d_data_fm_clicks_607376['senior'] + d_data_fm_clicks_737037['senior']

d_data_fm_clicks_intern_list = list(d_data_fm_clicks_intern_arr)
d_data_fm_clicks_junior_list = list(d_data_fm_clicks_junior_arr)
d_data_fm_clicks_middle_list = list(d_data_fm_clicks_middle_arr)
d_data_fm_clicks_senior_list = list(d_data_fm_clicks_senior_arr)

df_fm_clicks_groups = {
  'intern': d_data_fm_clicks_intern_arr,
  'junior': d_data_fm_clicks_junior_arr,
  'middle': d_data_fm_clicks_middle_arr,
  'senior': d_data_fm_clicks_senior_arr
}

# ============================================== #

# ================== ERRORS ==================== #

d_data_fs_errors_intern_arr = d_data_fs_errors_94662['intern'] + d_data_fs_errors_607376['intern'] + d_data_fs_errors_737037['intern']

d_data_fs_errors_junior_arr = d_data_fs_errors_94662['junior'] + d_data_fs_errors_607376['junior'] + d_data_fs_errors_737037['junior']

d_data_fs_errors_middle_arr = d_data_fs_errors_94662['middle'] + d_data_fs_errors_607376['middle'] + d_data_fs_errors_737037['middle']

d_data_fs_errors_senior_arr = d_data_fs_errors_94662['senior'] + d_data_fs_errors_607376['senior'] + d_data_fs_errors_737037['senior']

d_data_fs_errors_intern_list = list(d_data_fs_errors_intern_arr)
d_data_fs_errors_junior_list = list(d_data_fs_errors_junior_arr)
d_data_fs_errors_middle_list = list(d_data_fs_errors_middle_arr)
d_data_fs_errors_senior_list = list(d_data_fs_errors_senior_arr)

df_fs_errors_groups = {
  'intern': d_data_fs_errors_intern_arr,
  'junior': d_data_fs_errors_junior_arr,
  'middle': d_data_fs_errors_middle_arr,
  'senior': d_data_fs_errors_senior_arr
}

d_data_fm_errors_intern_arr = d_data_fm_errors_94662['intern'] + d_data_fm_errors_607376['intern'] + d_data_fm_errors_737037['intern']

d_data_fm_errors_junior_arr = d_data_fm_errors_94662['junior'] + d_data_fm_errors_607376['junior'] + d_data_fm_errors_737037['junior']

d_data_fm_errors_middle_arr = d_data_fm_errors_94662['middle'] + d_data_fm_errors_607376['middle'] + d_data_fm_errors_737037['middle']

d_data_fm_errors_senior_arr = d_data_fm_errors_94662['senior'] + d_data_fm_errors_607376['senior'] + d_data_fm_errors_737037['senior']

d_data_fm_errors_intern_list = list(d_data_fm_errors_intern_arr)
d_data_fm_errors_junior_list = list(d_data_fm_errors_junior_arr)
d_data_fm_errors_middle_list = list(d_data_fm_errors_middle_arr)
d_data_fm_errors_senior_list = list(d_data_fm_errors_senior_arr)

df_fm_errors_groups = {
  'intern': d_data_fm_errors_intern_arr,
  'junior': d_data_fm_errors_junior_arr,
  'middle': d_data_fm_errors_middle_arr,
  'senior': d_data_fm_errors_senior_arr
}

# ============================================== #

# ================== BIRADS ==================== #

d_data_fs_birads_intern_arr = d_data_fs_birads_94662['intern'] + d_data_fs_birads_607376['intern'] + d_data_fs_birads_737037['intern']

d_data_fs_birads_junior_arr = d_data_fs_birads_94662['junior'] + d_data_fs_birads_607376['junior'] + d_data_fs_birads_737037['junior']

d_data_fs_birads_middle_arr = d_data_fs_birads_94662['middle'] + d_data_fs_birads_607376['middle'] + d_data_fs_birads_737037['middle']

d_data_fs_birads_senior_arr = d_data_fs_birads_94662['senior'] + d_data_fs_birads_607376['senior'] + d_data_fs_birads_737037['senior']

d_data_fs_birads_intern_list = list(d_data_fs_birads_intern_arr)
d_data_fs_birads_junior_list = list(d_data_fs_birads_junior_arr)
d_data_fs_birads_middle_list = list(d_data_fs_birads_middle_arr)
d_data_fs_birads_senior_list = list(d_data_fs_birads_senior_arr)

df_fs_birads_groups = {
  'intern': d_data_fs_birads_intern_arr,
  'junior': d_data_fs_birads_junior_arr,
  'middle': d_data_fs_birads_middle_arr,
  'senior': d_data_fs_birads_senior_arr
}

d_data_fm_birads_intern_arr = d_data_fm_birads_94662['intern'] + d_data_fm_birads_607376['intern'] + d_data_fm_birads_737037['intern']

d_data_fm_birads_junior_arr = d_data_fm_birads_94662['junior'] + d_data_fm_birads_607376['junior'] + d_data_fm_birads_737037['junior']

d_data_fm_birads_middle_arr = d_data_fm_birads_94662['middle'] + d_data_fm_birads_607376['middle'] + d_data_fm_birads_737037['middle']

d_data_fm_birads_senior_arr = d_data_fm_birads_94662['senior'] + d_data_fm_birads_607376['senior'] + d_data_fm_birads_737037['senior']

d_data_fm_birads_intern_list = list(d_data_fm_birads_intern_arr)
d_data_fm_birads_junior_list = list(d_data_fm_birads_junior_arr)
d_data_fm_birads_middle_list = list(d_data_fm_birads_middle_arr)
d_data_fm_birads_senior_list = list(d_data_fm_birads_senior_arr)

df_fm_birads_groups = {
  'intern': d_data_fm_birads_intern_arr,
  'junior': d_data_fm_birads_junior_arr,
  'middle': d_data_fm_birads_middle_arr,
  'senior': d_data_fm_birads_senior_arr
}

# ============================================== #

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

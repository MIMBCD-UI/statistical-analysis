#!/usr/bin/env python

""".py: """

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
joinPath = os.path.join(pathDirname, '..', '..')
pathAbsPath = os.path.abspath(joinPath)

sa_constants_dir = (pathAbsPath + '/statistical-analysis/constants/')

sys.path.append(sa_constants_dir)

from dataFileGroups import *

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
#         SUS List/Group: Single-Modality        #
# ============================================== #

lg_fs_sus_01_intern = d_data_fs_sus_01['intern'].tolist()
lg_fs_sus_01_junior = d_data_fs_sus_01['junior'].tolist()
lg_fs_sus_01_middle = d_data_fs_sus_01['middle'].tolist()
lg_fs_sus_01_senior = d_data_fs_sus_01['senior'].tolist()

lg_fs_sus_02_intern = d_data_fs_sus_02['intern'].tolist()
lg_fs_sus_02_junior = d_data_fs_sus_02['junior'].tolist()
lg_fs_sus_02_middle = d_data_fs_sus_02['middle'].tolist()
lg_fs_sus_02_senior = d_data_fs_sus_02['senior'].tolist()

lg_fs_sus_03_intern = d_data_fs_sus_03['intern'].tolist()
lg_fs_sus_03_junior = d_data_fs_sus_03['junior'].tolist()
lg_fs_sus_03_middle = d_data_fs_sus_03['middle'].tolist()
lg_fs_sus_03_senior = d_data_fs_sus_03['senior'].tolist()

lg_fs_sus_04_intern = d_data_fs_sus_04['intern'].tolist()
lg_fs_sus_04_junior = d_data_fs_sus_04['junior'].tolist()
lg_fs_sus_04_middle = d_data_fs_sus_04['middle'].tolist()
lg_fs_sus_04_senior = d_data_fs_sus_04['senior'].tolist()

lg_fs_sus_05_intern = d_data_fs_sus_05['intern'].tolist()
lg_fs_sus_05_junior = d_data_fs_sus_05['junior'].tolist()
lg_fs_sus_05_middle = d_data_fs_sus_05['middle'].tolist()
lg_fs_sus_05_senior = d_data_fs_sus_05['senior'].tolist()

lg_fs_sus_06_intern = d_data_fs_sus_06['intern'].tolist()
lg_fs_sus_06_junior = d_data_fs_sus_06['junior'].tolist()
lg_fs_sus_06_middle = d_data_fs_sus_06['middle'].tolist()
lg_fs_sus_06_senior = d_data_fs_sus_06['senior'].tolist()

lg_fs_sus_07_intern = d_data_fs_sus_07['intern'].tolist()
lg_fs_sus_07_junior = d_data_fs_sus_07['junior'].tolist()
lg_fs_sus_07_middle = d_data_fs_sus_07['middle'].tolist()
lg_fs_sus_07_senior = d_data_fs_sus_07['senior'].tolist()

lg_fs_sus_08_intern = d_data_fs_sus_08['intern'].tolist()
lg_fs_sus_08_junior = d_data_fs_sus_08['junior'].tolist()
lg_fs_sus_08_middle = d_data_fs_sus_08['middle'].tolist()
lg_fs_sus_08_senior = d_data_fs_sus_08['senior'].tolist()

lg_fs_sus_09_intern = d_data_fs_sus_09['intern'].tolist()
lg_fs_sus_09_junior = d_data_fs_sus_09['junior'].tolist()
lg_fs_sus_09_middle = d_data_fs_sus_09['middle'].tolist()
lg_fs_sus_09_senior = d_data_fs_sus_09['senior'].tolist()

lg_fs_sus_10_intern = d_data_fs_sus_10['intern'].tolist()
lg_fs_sus_10_junior = d_data_fs_sus_10['junior'].tolist()
lg_fs_sus_10_middle = d_data_fs_sus_10['middle'].tolist()
lg_fs_sus_10_senior = d_data_fs_sus_10['senior'].tolist()

# ============================================== #

# ============================================== #
#         SUS List/Group: Multi-Modality         #
# ============================================== #

lg_fm_sus_01_intern = d_data_fm_sus_01['intern'].tolist()
lg_fm_sus_01_junior = d_data_fm_sus_01['junior'].tolist()
lg_fm_sus_01_middle = d_data_fm_sus_01['middle'].tolist()
lg_fm_sus_01_senior = d_data_fm_sus_01['senior'].tolist()

lg_fm_sus_02_intern = d_data_fm_sus_02['intern'].tolist()
lg_fm_sus_02_junior = d_data_fm_sus_02['junior'].tolist()
lg_fm_sus_02_middle = d_data_fm_sus_02['middle'].tolist()
lg_fm_sus_02_senior = d_data_fm_sus_02['senior'].tolist()

lg_fm_sus_03_intern = d_data_fm_sus_03['intern'].tolist()
lg_fm_sus_03_junior = d_data_fm_sus_03['junior'].tolist()
lg_fm_sus_03_middle = d_data_fm_sus_03['middle'].tolist()
lg_fm_sus_03_senior = d_data_fm_sus_03['senior'].tolist()

lg_fm_sus_04_intern = d_data_fm_sus_04['intern'].tolist()
lg_fm_sus_04_junior = d_data_fm_sus_04['junior'].tolist()
lg_fm_sus_04_middle = d_data_fm_sus_04['middle'].tolist()
lg_fm_sus_04_senior = d_data_fm_sus_04['senior'].tolist()

lg_fm_sus_05_intern = d_data_fm_sus_05['intern'].tolist()
lg_fm_sus_05_junior = d_data_fm_sus_05['junior'].tolist()
lg_fm_sus_05_middle = d_data_fm_sus_05['middle'].tolist()
lg_fm_sus_05_senior = d_data_fm_sus_05['senior'].tolist()

lg_fm_sus_06_intern = d_data_fm_sus_06['intern'].tolist()
lg_fm_sus_06_junior = d_data_fm_sus_06['junior'].tolist()
lg_fm_sus_06_middle = d_data_fm_sus_06['middle'].tolist()
lg_fm_sus_06_senior = d_data_fm_sus_06['senior'].tolist()

lg_fm_sus_07_intern = d_data_fm_sus_07['intern'].tolist()
lg_fm_sus_07_junior = d_data_fm_sus_07['junior'].tolist()
lg_fm_sus_07_middle = d_data_fm_sus_07['middle'].tolist()
lg_fm_sus_07_senior = d_data_fm_sus_07['senior'].tolist()

lg_fm_sus_08_intern = d_data_fm_sus_08['intern'].tolist()
lg_fm_sus_08_junior = d_data_fm_sus_08['junior'].tolist()
lg_fm_sus_08_middle = d_data_fm_sus_08['middle'].tolist()
lg_fm_sus_08_senior = d_data_fm_sus_08['senior'].tolist()

lg_fm_sus_09_intern = d_data_fm_sus_09['intern'].tolist()
lg_fm_sus_09_junior = d_data_fm_sus_09['junior'].tolist()
lg_fm_sus_09_middle = d_data_fm_sus_09['middle'].tolist()
lg_fm_sus_09_senior = d_data_fm_sus_09['senior'].tolist()

lg_fm_sus_10_intern = d_data_fm_sus_10['intern'].tolist()
lg_fm_sus_10_junior = d_data_fm_sus_10['junior'].tolist()
lg_fm_sus_10_middle = d_data_fm_sus_10['middle'].tolist()
lg_fm_sus_10_senior = d_data_fm_sus_10['senior'].tolist()

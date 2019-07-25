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
joinPath = os.path.join(pathDirname, '..', '..', '..')
pathAbsPath = os.path.abspath(joinPath)

sa_constants_dir = (pathAbsPath + '/statistical-analysis/src/constants/')

sys.path.append(sa_constants_dir)

from listGroups import *

# ============================================== #
#         SUS List/Group: Single-Modality        #
# ============================================== #

lg_fs_sus_intern = lg_fs_sus_01_intern + lg_fs_sus_02_intern + lg_fs_sus_03_intern + lg_fs_sus_04_intern + lg_fs_sus_05_intern + lg_fs_sus_06_intern + lg_fs_sus_07_intern + lg_fs_sus_08_intern + lg_fs_sus_09_intern + lg_fs_sus_10_intern

lg_fs_sus_intern_arr = [
  lg_fs_sus_01_intern,
  lg_fs_sus_02_intern,
  lg_fs_sus_03_intern,
  lg_fs_sus_04_intern,
  lg_fs_sus_05_intern,
  lg_fs_sus_06_intern,
  lg_fs_sus_07_intern,
  lg_fs_sus_08_intern,
  lg_fs_sus_09_intern,
  lg_fs_sus_10_intern
]

lg_fs_sus_junior = lg_fs_sus_01_junior + lg_fs_sus_02_junior + lg_fs_sus_03_junior + lg_fs_sus_04_junior + lg_fs_sus_05_junior + lg_fs_sus_06_junior + lg_fs_sus_07_junior + lg_fs_sus_08_junior + lg_fs_sus_09_junior + lg_fs_sus_10_junior

lg_fs_sus_junior_arr = [
  lg_fs_sus_01_junior,
  lg_fs_sus_02_junior,
  lg_fs_sus_03_junior,
  lg_fs_sus_04_junior,
  lg_fs_sus_05_junior,
  lg_fs_sus_06_junior,
  lg_fs_sus_07_junior,
  lg_fs_sus_08_junior,
  lg_fs_sus_09_junior,
  lg_fs_sus_10_junior
]

lg_fs_sus_middle = lg_fs_sus_01_middle + lg_fs_sus_02_middle + lg_fs_sus_03_middle + lg_fs_sus_04_middle + lg_fs_sus_05_middle + lg_fs_sus_06_middle + lg_fs_sus_07_middle + lg_fs_sus_08_middle + lg_fs_sus_09_middle + lg_fs_sus_10_middle

lg_fs_sus_middle_arr = [
  lg_fs_sus_01_middle,
  lg_fs_sus_02_middle,
  lg_fs_sus_03_middle,
  lg_fs_sus_04_middle,
  lg_fs_sus_05_middle,
  lg_fs_sus_06_middle,
  lg_fs_sus_07_middle,
  lg_fs_sus_08_middle,
  lg_fs_sus_09_middle,
  lg_fs_sus_10_middle
]

lg_fs_sus_senior = lg_fs_sus_01_senior + lg_fs_sus_02_senior + lg_fs_sus_03_senior + lg_fs_sus_04_senior + lg_fs_sus_05_senior + lg_fs_sus_06_senior + lg_fs_sus_07_senior + lg_fs_sus_08_senior + lg_fs_sus_09_senior + lg_fs_sus_10_senior

lg_fs_sus_senior_arr = [
  lg_fs_sus_01_senior,
  lg_fs_sus_02_senior,
  lg_fs_sus_03_senior,
  lg_fs_sus_04_senior,
  lg_fs_sus_05_senior,
  lg_fs_sus_06_senior,
  lg_fs_sus_07_senior,
  lg_fs_sus_08_senior,
  lg_fs_sus_09_senior,
  lg_fs_sus_10_senior
]

# ============================================== #

# ============================================== #
#         SUS List/Group: Multi-Modality         #
# ============================================== #

lg_fm_sus_intern = lg_fm_sus_01_intern + lg_fm_sus_02_intern + lg_fm_sus_03_intern + lg_fm_sus_04_intern + lg_fm_sus_05_intern + lg_fm_sus_06_intern + lg_fm_sus_07_intern + lg_fm_sus_08_intern + lg_fm_sus_09_intern + lg_fm_sus_10_intern

lg_fm_sus_intern_arr = [
  lg_fm_sus_01_intern,
  lg_fm_sus_02_intern,
  lg_fm_sus_03_intern,
  lg_fm_sus_04_intern,
  lg_fm_sus_05_intern,
  lg_fm_sus_06_intern,
  lg_fm_sus_07_intern,
  lg_fm_sus_08_intern,
  lg_fm_sus_09_intern,
  lg_fm_sus_10_intern
]

lg_fm_sus_junior = lg_fm_sus_01_junior + lg_fm_sus_02_junior + lg_fm_sus_03_junior + lg_fm_sus_04_junior + lg_fm_sus_05_junior + lg_fm_sus_06_junior + lg_fm_sus_07_junior + lg_fm_sus_08_junior + lg_fm_sus_09_junior + lg_fm_sus_10_junior

lg_fm_sus_junior_arr = [
  lg_fm_sus_01_junior,
  lg_fm_sus_02_junior,
  lg_fm_sus_03_junior,
  lg_fm_sus_04_junior,
  lg_fm_sus_05_junior,
  lg_fm_sus_06_junior,
  lg_fm_sus_07_junior,
  lg_fm_sus_08_junior,
  lg_fm_sus_09_junior,
  lg_fm_sus_10_junior
]

lg_fm_sus_middle = lg_fm_sus_01_middle + lg_fm_sus_02_middle + lg_fm_sus_03_middle + lg_fm_sus_04_middle + lg_fm_sus_05_middle + lg_fm_sus_06_middle + lg_fm_sus_07_middle + lg_fm_sus_08_middle + lg_fm_sus_09_middle + lg_fm_sus_10_middle

lg_fm_sus_middle_arr = [
  lg_fm_sus_01_middle,
  lg_fm_sus_02_middle,
  lg_fm_sus_03_middle,
  lg_fm_sus_04_middle,
  lg_fm_sus_05_middle,
  lg_fm_sus_06_middle,
  lg_fm_sus_07_middle,
  lg_fm_sus_08_middle,
  lg_fm_sus_09_middle,
  lg_fm_sus_10_middle
]

lg_fm_sus_senior = lg_fm_sus_01_senior + lg_fm_sus_02_senior + lg_fm_sus_03_senior + lg_fm_sus_04_senior + lg_fm_sus_05_senior + lg_fm_sus_06_senior + lg_fm_sus_07_senior + lg_fm_sus_08_senior + lg_fm_sus_09_senior + lg_fm_sus_10_senior

lg_fm_sus_senior_arr = [
  lg_fm_sus_01_senior,
  lg_fm_sus_02_senior,
  lg_fm_sus_03_senior,
  lg_fm_sus_04_senior,
  lg_fm_sus_05_senior,
  lg_fm_sus_06_senior,
  lg_fm_sus_07_senior,
  lg_fm_sus_08_senior,
  lg_fm_sus_09_senior,
  lg_fm_sus_10_senior
]

# ============================================== #

# ============================================== #
# ============================================== #
# ============================================== #

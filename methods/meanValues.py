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

from listGroups import *

import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np

# ============================================== #
#                                                #
#      IS IT NORMAL (GAUSSIAN) DISTRIBUTION?     #
#                                                #
# ============================================== #

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
# SUS MEANS

sus_sm_val = mu_s_013 + mu_s_014 + mu_s_015 + mu_s_016 + mu_s_017 + mu_s_018 + mu_s_019 + mu_s_020 + mu_s_021 + mu_s_022
sus_mm_val = mu_s_023 + mu_s_024 + mu_s_025 + mu_s_026 + mu_s_027 + mu_s_028 + mu_s_029 + mu_s_030 + mu_s_031 + mu_s_032

sus_sm_mean = sus_sm_val / 10
sus_mm_mean = sus_mm_val / 10

print("Compute Mean Value for sus_sm_mean: %d" % sus_sm_val)
print("Compute Mean Value for sus_mm_mean: %d" % sus_mm_val)

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

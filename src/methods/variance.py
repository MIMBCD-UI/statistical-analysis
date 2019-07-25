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
sa_methods_dir = (pathAbsPath + '/statistical-analysis/src/methods/')

sys.path.append(sa_constants_dir)
sys.path.append(sa_methods_dir)

from listGroups import *
from messageVars import *
from meanValues import *

import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np

# ============================================== #
# Verification of the Mean:
mean_ver_s_001 = abs(mu_s_001 - meanComp_s_001) < stdToCompare
mean_ver_s_002 = abs(mu_s_002 - meanComp_s_002) < stdToCompare
mean_ver_s_003 = abs(mu_s_003 - meanComp_s_003) < stdToCompare
mean_ver_s_004 = abs(mu_s_004 - meanComp_s_004) < stdToCompare
mean_ver_s_005 = abs(mu_s_005 - meanComp_s_005) < stdToCompare
mean_ver_s_006 = abs(mu_s_006 - meanComp_s_006) < stdToCompare
print(message_mean_ver_s_001, mean_ver_s_001)
print(message_mean_ver_s_002, mean_ver_s_002)
print(message_mean_ver_s_003, mean_ver_s_003)
print(message_mean_ver_s_004, mean_ver_s_004)
print(message_mean_ver_s_005, mean_ver_s_005)
print(message_mean_ver_s_006, mean_ver_s_006)

mean_ver_s_007 = abs(mu_s_007 - meanComp_s_007) < stdToCompare
mean_ver_s_008 = abs(mu_s_008 - meanComp_s_008) < stdToCompare
mean_ver_s_009 = abs(mu_s_009 - meanComp_s_009) < stdToCompare
mean_ver_s_010 = abs(mu_s_010 - meanComp_s_010) < stdToCompare
mean_ver_s_011 = abs(mu_s_011 - meanComp_s_011) < stdToCompare
mean_ver_s_012 = abs(mu_s_012 - meanComp_s_012) < stdToCompare
print(message_mean_ver_s_007, mean_ver_s_007)
print(message_mean_ver_s_008, mean_ver_s_008)
print(message_mean_ver_s_009, mean_ver_s_009)
print(message_mean_ver_s_010, mean_ver_s_010)
print(message_mean_ver_s_011, mean_ver_s_011)
print(message_mean_ver_s_012, mean_ver_s_012)
# ============================================== #

# ============================================== #
# Compute Variance:
stdS_001 = np.std(s_001, ddof=1)
stdS_002 = np.std(s_002, ddof=1)
stdS_003 = np.std(s_003, ddof=1)
stdS_004 = np.std(s_004, ddof=1)
stdS_005 = np.std(s_005, ddof=1)
stdS_006 = np.std(s_006, ddof=1)
print(message_stdS_001, stdS_001)
print(message_stdS_002, stdS_002)
print(message_stdS_003, stdS_003)
print(message_stdS_004, stdS_004)
print(message_stdS_005, stdS_005)
print(message_stdS_006, stdS_006)

stdS_007 = np.std(s_007, ddof=1)
stdS_008 = np.std(s_008, ddof=1)
stdS_009 = np.std(s_009, ddof=1)
stdS_010 = np.std(s_010, ddof=1)
stdS_011 = np.std(s_011, ddof=1)
stdS_012 = np.std(s_012, ddof=1)
print(message_stdS_007, stdS_007)
print(message_stdS_008, stdS_008)
print(message_stdS_009, stdS_009)
print(message_stdS_010, stdS_010)
print(message_stdS_011, stdS_011)
print(message_stdS_012, stdS_012)

stdS_013 = np.std(s_013, ddof=1)
stdS_014 = np.std(s_014, ddof=1)
stdS_015 = np.std(s_015, ddof=1)
stdS_016 = np.std(s_016, ddof=1)
stdS_017 = np.std(s_017, ddof=1)
stdS_018 = np.std(s_018, ddof=1)
stdS_019 = np.std(s_019, ddof=1)
stdS_020 = np.std(s_020, ddof=1)
stdS_021 = np.std(s_021, ddof=1)
stdS_022 = np.std(s_022, ddof=1)
print(message_stdS_013, stdS_013)
print(message_stdS_014, stdS_014)
print(message_stdS_015, stdS_015)
print(message_stdS_016, stdS_016)
print(message_stdS_017, stdS_017)
print(message_stdS_018, stdS_018)
print(message_stdS_019, stdS_019)
print(message_stdS_020, stdS_020)
print(message_stdS_021, stdS_021)
print(message_stdS_022, stdS_022)

stdS_023 = np.std(s_023, ddof=1)
stdS_024 = np.std(s_024, ddof=1)
stdS_025 = np.std(s_025, ddof=1)
stdS_026 = np.std(s_026, ddof=1)
stdS_027 = np.std(s_027, ddof=1)
stdS_028 = np.std(s_028, ddof=1)
stdS_029 = np.std(s_029, ddof=1)
stdS_030 = np.std(s_030, ddof=1)
stdS_031 = np.std(s_031, ddof=1)
stdS_032 = np.std(s_032, ddof=1)
print(message_stdS_023, stdS_023)
print(message_stdS_024, stdS_024)
print(message_stdS_025, stdS_025)
print(message_stdS_026, stdS_026)
print(message_stdS_027, stdS_027)
print(message_stdS_028, stdS_028)
print(message_stdS_029, stdS_029)
print(message_stdS_030, stdS_030)
print(message_stdS_031, stdS_031)
print(message_stdS_032, stdS_032)

stdS_033 = np.std(s_033, ddof=1)
stdS_034 = np.std(s_034, ddof=1)
stdS_035 = np.std(s_035, ddof=1)
stdS_036 = np.std(s_036, ddof=1)
print(message_stdS_033, stdS_033)
print(message_stdS_034, stdS_034)
print(message_stdS_035, stdS_035)
print(message_stdS_036, stdS_036)

stdS_037 = np.std(s_037, ddof=1)
stdS_038 = np.std(s_038, ddof=1)
stdS_039 = np.std(s_039, ddof=1)
stdS_040 = np.std(s_040, ddof=1)
print(message_stdS_037, stdS_037)
print(message_stdS_038, stdS_038)
print(message_stdS_039, stdS_039)
print(message_stdS_040, stdS_040)

stdS_041 = np.std(s_041, ddof=1)
stdS_042 = np.std(s_042, ddof=1)
stdS_043 = np.std(s_043, ddof=1)
stdS_044 = np.std(s_044, ddof=1)
print(message_stdS_041, stdS_041)
print(message_stdS_042, stdS_042)
print(message_stdS_043, stdS_043)
print(message_stdS_044, stdS_044)

stdS_045 = np.std(s_045, ddof=1)
stdS_046 = np.std(s_046, ddof=1)
stdS_047 = np.std(s_047, ddof=1)
print(message_stdS_045, stdS_045)
print(message_stdS_046, stdS_046)
print(message_stdS_047, stdS_047)

stdS_048 = np.std(s_048, ddof=1)
stdS_049 = np.std(s_049, ddof=1)
stdS_050 = np.std(s_050, ddof=1)
stdS_051 = np.std(s_051, ddof=1)
print(message_stdS_048, stdS_048)
print(message_stdS_049, stdS_049)
print(message_stdS_050, stdS_050)
print(message_stdS_051, stdS_051)

stdS_052 = np.std(s_052, ddof=1)
stdS_053 = np.std(s_053, ddof=1)
stdS_054 = np.std(s_054, ddof=1)
stdS_055 = np.std(s_055, ddof=1)
print(message_stdS_052, stdS_052)
print(message_stdS_053, stdS_053)
print(message_stdS_054, stdS_054)
print(message_stdS_055, stdS_055)

stdS_056 = np.std(s_056, ddof=1)
stdS_057 = np.std(s_057, ddof=1)
stdS_058 = np.std(s_058, ddof=1)
stdS_059 = np.std(s_059, ddof=1)
print(message_stdS_056, stdS_056)
print(message_stdS_057, stdS_057)
print(message_stdS_058, stdS_058)
print(message_stdS_059, stdS_059)

stdS_060 = np.std(s_060, ddof=1)
stdS_061 = np.std(s_061, ddof=1)
stdS_062 = np.std(s_062, ddof=1)
print(message_stdS_060, stdS_060)
print(message_stdS_061, stdS_061)
print(message_stdS_062, stdS_062)

stdS_sm_sus = stdS_013 + stdS_014 + stdS_015 + stdS_016 + stdS_017 + stdS_018 + stdS_019 + stdS_020 + stdS_021 + stdS_022
stdS_mm_sus = stdS_023 + stdS_024 + stdS_025 + stdS_026 + stdS_027 + stdS_028 + stdS_029 + stdS_030 + stdS_031 + stdS_032
stdS_sm_sus_mean = stdS_sm_sus / 10
stdS_mm_sus_mean = stdS_mm_sus / 10
print("Compute Variance for stdS_sm: %f" % stdS_sm_sus_mean)
print("Compute Variance for stdS_mm: %f" % stdS_mm_sus_mean)
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
# ============================================== #
# ============================================== #
# ============================================== #

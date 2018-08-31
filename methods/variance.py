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
sa_methods_dir = (pathAbsPath + '/statistical-analysis/methods/')

sys.path.append(sa_constants_dir)
sys.path.append(sa_methods_dir)

from listGroups import *
from meanValues import *

import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np

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

stdS_sm = stdS_013 + stdS_014 + stdS_015 + stdS_016 + stdS_017 + stdS_018 + stdS_019 + stdS_020 + stdS_021 + stdS_022
stdS_mm = stdS_023 + stdS_024 + stdS_025 + stdS_026 + stdS_027 + stdS_028 + stdS_029 + stdS_030 + stdS_031 + stdS_032
stdS_sm_mean = stdS_sm / 10
stdS_mm_mean = stdS_mm / 10
print("Compute Variance for stdS_sm: %f" % stdS_sm_mean)
print("Compute Variance for stdS_mm: %f" % stdS_mm_mean)
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

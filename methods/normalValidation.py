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

from special import *
from listGroups import *
from kDagostPear import *

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

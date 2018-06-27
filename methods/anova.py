#!/usr/bin/env python

"""anova.py: A python version of ANOVA."""

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

joinPath = os.path.join(os.path.dirname(__file__), '..', '..')
pathAbsPath = os.path.abspath(joinPath)

sa_scripts_dir = (pathAbsPath + '/statistical-analysis/scripts/')
sys.path.append(sa_scripts_dir)

from nasa import nasaColMean

sheetReader_dir = (pathAbsPath + '/sheet-reader/src/')
sys.path.append(sheetReader_dir)

import pandas as pd
datafile = (pathAbsPath + '/sheet-reader/temp/sheet.csv')

#data = pd.read_csv(datafile, error_bad_lines=False)

from main import sheetReader
from main import sheetReaderSum
from main import sheetReaderMean

constants_dir = (pathAbsPath + '/sheet-reader/constants/')
sys.path.append(constants_dir)
import main_variables

# ============================================== #
#                IMPORT VARIABLES                #
# ============================================== #

MIN_VAL = main_variables.MIN_VAL
MAX_VAL = main_variables.MAX_VAL
N       = main_variables.N

GROUP_INTERN_1 = main_variables.GROUP_INTERN_1
GROUP_INTERN_2 = main_variables.GROUP_INTERN_2
GROUP_JUNIOR_1 = main_variables.GROUP_JUNIOR_1
GROUP_JUNIOR_2 = main_variables.GROUP_JUNIOR_2
GROUP_MIDDLE_1 = main_variables.GROUP_MIDDLE_1
GROUP_MIDDLE_2 = main_variables.GROUP_MIDDLE_2
GROUP_SENIOR_1 = main_variables.GROUP_SENIOR_1
GROUP_SENIOR_2 = main_variables.GROUP_SENIOR_2

GROUPS_LIST = main_variables.GROUPS_LIST

NASATLX_SINGLE_MENTAL_DEMAND = main_variables.NASATLX_SINGLE_MENTAL_DEMAND
NASATLX_SINGLE_PHYSICAL_DEMAND = main_variables.NASATLX_SINGLE_PHYSICAL_DEMAND
NASATLX_SINGLE_TEMPORAL_DEMAND = main_variables.NASATLX_SINGLE_TEMPORAL_DEMAND
NASATLX_SINGLE_PERFORMANCE = main_variables.NASATLX_SINGLE_PERFORMANCE
NASATLX_SINGLE_EFFORT = main_variables.NASATLX_SINGLE_EFFORT
NASATLX_SINGLE_FRUSTRATION = main_variables.NASATLX_SINGLE_FRUSTRATION

NASATLX_SINGLE_LIST = main_variables.NASATLX_SINGLE_LIST

NASATLX_MULTI_MENTAL_DEMAND = main_variables.NASATLX_MULTI_MENTAL_DEMAND
NASATLX_MULTI_PHYSICAL_DEMAND = main_variables.NASATLX_MULTI_PHYSICAL_DEMAND
NASATLX_MULTI_TEMPORAL_DEMAND = main_variables.NASATLX_MULTI_TEMPORAL_DEMAND
NASATLX_MULTI_PERFORMANCE = main_variables.NASATLX_MULTI_PERFORMANCE
NASATLX_MULTI_EFFORT = main_variables.NASATLX_MULTI_EFFORT
NASATLX_MULTI_FRUSTRATION = main_variables.NASATLX_MULTI_FRUSTRATION

NASATLX_MULTI_LIST = main_variables.NASATLX_MULTI_LIST

# ============================================== #
#                                                #
#                 READING GROUPS                 #
#                                                #
# ============================================== #

# ============================================== #
#                 GROUP_INTERN_1                 #
# ============================================== #

NSMD_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_SINGLE_PERFORMANCE)
NSE_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_SINGLE_EFFORT)
NSF_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_SINGLE_FRUSTRATION)

NMMD_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_MULTI_PERFORMANCE)
NME_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_MULTI_EFFORT)
NMF_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_MULTI_FRUSTRATION)

NSMD_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_SINGLE_PERFORMANCE)
NSE_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_SINGLE_EFFORT)
NSF_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_SINGLE_FRUSTRATION)

NMMD_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_MULTI_PERFORMANCE)
NME_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_MULTI_EFFORT)
NMF_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_MULTI_FRUSTRATION)

# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                 GROUP_INTERN_2                 #
# ============================================== #

NSMD_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_SINGLE_PERFORMANCE)
NSE_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_SINGLE_EFFORT)
NSF_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_SINGLE_FRUSTRATION)

NMMD_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_MULTI_PERFORMANCE)
NME_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_MULTI_EFFORT)
NMF_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_MULTI_FRUSTRATION)

NSMD_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_SINGLE_PERFORMANCE)
NSE_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_SINGLE_EFFORT)
NSF_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_SINGLE_FRUSTRATION)

NMMD_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_MULTI_PERFORMANCE)
NME_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_MULTI_EFFORT)
NMF_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_MULTI_FRUSTRATION)

# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                 GROUP_JUNIOR_1                 #
# ============================================== #

NSMD_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_SINGLE_PERFORMANCE)
NSE_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_SINGLE_EFFORT)
NSF_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_SINGLE_FRUSTRATION)

NMMD_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_MULTI_PERFORMANCE)
NME_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_MULTI_EFFORT)
NMF_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_MULTI_FRUSTRATION)

NSMD_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_SINGLE_PERFORMANCE)
NSE_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_SINGLE_EFFORT)
NSF_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_SINGLE_FRUSTRATION)

NMMD_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_MULTI_PERFORMANCE)
NME_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_MULTI_EFFORT)
NMF_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_MULTI_FRUSTRATION)

# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                 GROUP_JUNIOR_2                 #
# ============================================== #

NSMD_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_SINGLE_PERFORMANCE)
NSE_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_SINGLE_EFFORT)
NSF_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_SINGLE_FRUSTRATION)

NMMD_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_MULTI_PERFORMANCE)
NME_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_MULTI_EFFORT)
NMF_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_MULTI_FRUSTRATION)

NSMD_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_SINGLE_PERFORMANCE)
NSE_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_SINGLE_EFFORT)
NSF_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_SINGLE_FRUSTRATION)

NMMD_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_MULTI_PERFORMANCE)
NME_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_MULTI_EFFORT)
NMF_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_MULTI_FRUSTRATION)

# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                 GROUP_MIDDLE_1                 #
# ============================================== #

NSMD_SUM_GM1 = sheetReaderSum(GROUP_MIDDLE_1, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_SUM_GM1 = sheetReaderSum(GROUP_MIDDLE_1, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_SUM_GM1 = sheetReaderSum(GROUP_MIDDLE_1, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_SUM_GM1 = sheetReaderSum(GROUP_MIDDLE_1, NASATLX_SINGLE_PERFORMANCE)
NSE_SUM_GM1 = sheetReaderSum(GROUP_MIDDLE_1, NASATLX_SINGLE_EFFORT)
NSF_SUM_GM1 = sheetReaderSum(GROUP_MIDDLE_1, NASATLX_SINGLE_FRUSTRATION)

NMMD_SUM_GM1 = sheetReaderSum(GROUP_MIDDLE_1, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_SUM_GM1 = sheetReaderSum(GROUP_MIDDLE_1, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_SUM_GM1 = sheetReaderSum(GROUP_MIDDLE_1, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_SUM_GM1 = sheetReaderSum(GROUP_MIDDLE_1, NASATLX_MULTI_PERFORMANCE)
NME_SUM_GM1 = sheetReaderSum(GROUP_MIDDLE_1, NASATLX_MULTI_EFFORT)
NMF_SUM_GM1 = sheetReaderSum(GROUP_MIDDLE_1, NASATLX_MULTI_FRUSTRATION)

NSMD_MEAN_GM1 = sheetReaderMean(GROUP_MIDDLE_1, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_MEAN_GM1 = sheetReaderMean(GROUP_MIDDLE_1, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_MEAN_GM1 = sheetReaderMean(GROUP_MIDDLE_1, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_MEAN_GM1 = sheetReaderMean(GROUP_MIDDLE_1, NASATLX_SINGLE_PERFORMANCE)
NSE_MEAN_GM1 = sheetReaderMean(GROUP_MIDDLE_1, NASATLX_SINGLE_EFFORT)
NSF_MEAN_GM1 = sheetReaderMean(GROUP_MIDDLE_1, NASATLX_SINGLE_FRUSTRATION)

NMMD_MEAN_GM1 = sheetReaderMean(GROUP_MIDDLE_1, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_MEAN_GM1 = sheetReaderMean(GROUP_MIDDLE_1, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_MEAN_GM1 = sheetReaderMean(GROUP_MIDDLE_1, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_MEAN_GM1 = sheetReaderMean(GROUP_MIDDLE_1, NASATLX_MULTI_PERFORMANCE)
NME_MEAN_GM1 = sheetReaderMean(GROUP_MIDDLE_1, NASATLX_MULTI_EFFORT)
NMF_MEAN_GM1 = sheetReaderMean(GROUP_MIDDLE_1, NASATLX_MULTI_FRUSTRATION)

# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                 GROUP_MIDDLE_2                 #
# ============================================== #

NSMD_SUM_GM2 = sheetReaderSum(GROUP_MIDDLE_2, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_SUM_GM2 = sheetReaderSum(GROUP_MIDDLE_2, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_SUM_GM2 = sheetReaderSum(GROUP_MIDDLE_2, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_SUM_GM2 = sheetReaderSum(GROUP_MIDDLE_2, NASATLX_SINGLE_PERFORMANCE)
NSE_SUM_GM2 = sheetReaderSum(GROUP_MIDDLE_2, NASATLX_SINGLE_EFFORT)
NSF_SUM_GM2 = sheetReaderSum(GROUP_MIDDLE_2, NASATLX_SINGLE_FRUSTRATION)

NMMD_SUM_GM2 = sheetReaderSum(GROUP_MIDDLE_2, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_SUM_GM2 = sheetReaderSum(GROUP_MIDDLE_2, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_SUM_GM2 = sheetReaderSum(GROUP_MIDDLE_2, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_SUM_GM2 = sheetReaderSum(GROUP_MIDDLE_2, NASATLX_MULTI_PERFORMANCE)
NME_SUM_GM2 = sheetReaderSum(GROUP_MIDDLE_2, NASATLX_MULTI_EFFORT)
NMF_SUM_GM2 = sheetReaderSum(GROUP_MIDDLE_2, NASATLX_MULTI_FRUSTRATION)

NSMD_MEAN_GM2 = sheetReaderMean(GROUP_MIDDLE_2, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_MEAN_GM2 = sheetReaderMean(GROUP_MIDDLE_2, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_MEAN_GM2 = sheetReaderMean(GROUP_MIDDLE_2, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_MEAN_GM2 = sheetReaderMean(GROUP_MIDDLE_2, NASATLX_SINGLE_PERFORMANCE)
NSE_MEAN_GM2 = sheetReaderMean(GROUP_MIDDLE_2, NASATLX_SINGLE_EFFORT)
NSF_MEAN_GM2 = sheetReaderMean(GROUP_MIDDLE_2, NASATLX_SINGLE_FRUSTRATION)

NMMD_MEAN_GM2 = sheetReaderMean(GROUP_MIDDLE_2, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_MEAN_GM2 = sheetReaderMean(GROUP_MIDDLE_2, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_MEAN_GM2 = sheetReaderMean(GROUP_MIDDLE_2, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_MEAN_GM2 = sheetReaderMean(GROUP_MIDDLE_2, NASATLX_MULTI_PERFORMANCE)
NME_MEAN_GM2 = sheetReaderMean(GROUP_MIDDLE_2, NASATLX_MULTI_EFFORT)
NMF_MEAN_GM2 = sheetReaderMean(GROUP_MIDDLE_2, NASATLX_MULTI_FRUSTRATION)

# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                 GROUP_SENIOR_1                 #
# ============================================== #

NSMD_SUM_GS1 = sheetReaderSum(GROUP_SENIOR_1, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_SUM_GS1 = sheetReaderSum(GROUP_SENIOR_1, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_SUM_GS1 = sheetReaderSum(GROUP_SENIOR_1, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_SUM_GS1 = sheetReaderSum(GROUP_SENIOR_1, NASATLX_SINGLE_PERFORMANCE)
NSE_SUM_GS1 = sheetReaderSum(GROUP_SENIOR_1, NASATLX_SINGLE_EFFORT)
NSF_SUM_GS1 = sheetReaderSum(GROUP_SENIOR_1, NASATLX_SINGLE_FRUSTRATION)

NMMD_SUM_GS1 = sheetReaderSum(GROUP_SENIOR_1, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_SUM_GS1 = sheetReaderSum(GROUP_SENIOR_1, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_SUM_GS1 = sheetReaderSum(GROUP_SENIOR_1, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_SUM_GS1 = sheetReaderSum(GROUP_SENIOR_1, NASATLX_MULTI_PERFORMANCE)
NME_SUM_GS1 = sheetReaderSum(GROUP_SENIOR_1, NASATLX_MULTI_EFFORT)
NMF_SUM_GS1 = sheetReaderSum(GROUP_SENIOR_1, NASATLX_MULTI_FRUSTRATION)

NSMD_MEAN_GS1 = sheetReaderMean(GROUP_SENIOR_1, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_MEAN_GS1 = sheetReaderMean(GROUP_SENIOR_1, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_MEAN_GS1 = sheetReaderMean(GROUP_SENIOR_1, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_MEAN_GS1 = sheetReaderMean(GROUP_SENIOR_1, NASATLX_SINGLE_PERFORMANCE)
NSE_MEAN_GS1 = sheetReaderMean(GROUP_SENIOR_1, NASATLX_SINGLE_EFFORT)
NSF_MEAN_GS1 = sheetReaderMean(GROUP_SENIOR_1, NASATLX_SINGLE_FRUSTRATION)

NMMD_MEAN_GS1 = sheetReaderMean(GROUP_SENIOR_1, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_MEAN_GS1 = sheetReaderMean(GROUP_SENIOR_1, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_MEAN_GS1 = sheetReaderMean(GROUP_SENIOR_1, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_MEAN_GS1 = sheetReaderMean(GROUP_SENIOR_1, NASATLX_MULTI_PERFORMANCE)
NME_MEAN_GS1 = sheetReaderMean(GROUP_SENIOR_1, NASATLX_MULTI_EFFORT)
NMF_MEAN_GS1 = sheetReaderMean(GROUP_SENIOR_1, NASATLX_MULTI_FRUSTRATION)

# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                 GROUP_SENIOR_2                 #
# ============================================== #

NSMD_SUM_GS2 = sheetReaderSum(GROUP_SENIOR_2, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_SUM_GS2 = sheetReaderSum(GROUP_SENIOR_2, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_SUM_GS2 = sheetReaderSum(GROUP_SENIOR_2, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_SUM_GS2  = sheetReaderSum(GROUP_SENIOR_2, NASATLX_SINGLE_PERFORMANCE)
NSE_SUM_GS2  = sheetReaderSum(GROUP_SENIOR_2, NASATLX_SINGLE_EFFORT)
NSF_SUM_GS2  = sheetReaderSum(GROUP_SENIOR_2, NASATLX_SINGLE_FRUSTRATION)

NMMD_SUM_GS2 = sheetReaderSum(GROUP_SENIOR_2, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_SUM_GS2 = sheetReaderSum(GROUP_SENIOR_2, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_SUM_GS2 = sheetReaderSum(GROUP_SENIOR_2, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_SUM_GS2  = sheetReaderSum(GROUP_SENIOR_2, NASATLX_MULTI_PERFORMANCE)
NME_SUM_GS2  = sheetReaderSum(GROUP_SENIOR_2, NASATLX_MULTI_EFFORT)
NMF_SUM_GS2  = sheetReaderSum(GROUP_SENIOR_2, NASATLX_MULTI_FRUSTRATION)

NSMD_MEAN_GS2 = sheetReaderMean(GROUP_SENIOR_2, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_MEAN_GS2 = sheetReaderMean(GROUP_SENIOR_2, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_MEAN_GS2 = sheetReaderMean(GROUP_SENIOR_2, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_MEAN_GS2  = sheetReaderMean(GROUP_SENIOR_2, NASATLX_SINGLE_PERFORMANCE)
NSE_MEAN_GS2  = sheetReaderMean(GROUP_SENIOR_2, NASATLX_SINGLE_EFFORT)
NSF_MEAN_GS2  = sheetReaderMean(GROUP_SENIOR_2, NASATLX_SINGLE_FRUSTRATION)

NMMD_MEAN_GS2 = sheetReaderMean(GROUP_SENIOR_2, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_MEAN_GS2 = sheetReaderMean(GROUP_SENIOR_2, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_MEAN_GS2 = sheetReaderMean(GROUP_SENIOR_2, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_MEAN_GS2  = sheetReaderMean(GROUP_SENIOR_2, NASATLX_MULTI_PERFORMANCE)
NME_MEAN_GS2  = sheetReaderMean(GROUP_SENIOR_2, NASATLX_MULTI_EFFORT)
NMF_MEAN_GS2  = sheetReaderMean(GROUP_SENIOR_2, NASATLX_MULTI_FRUSTRATION)

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                                                #
#                 NASA-TLX MEANS                 #
#                                                #
# ============================================== #

NSMD_ALL = nasaColMean(NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_ALL = nasaColMean(NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_ALL = nasaColMean(NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_ALL  = nasaColMean(NASATLX_SINGLE_PERFORMANCE)
NSE_ALL  = nasaColMean(NASATLX_SINGLE_EFFORT)
NSF_ALL  = nasaColMean(NASATLX_SINGLE_FRUSTRATION)

NMMD_ALL = nasaColMean(NASATLX_MULTI_MENTAL_DEMAND)
NMPD_ALL = nasaColMean(NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_ALL = nasaColMean(NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_ALL  = nasaColMean(NASATLX_MULTI_PERFORMANCE)
NME_ALL  = nasaColMean(NASATLX_MULTI_EFFORT)
NMF_ALL  = nasaColMean(NASATLX_MULTI_FRUSTRATION)

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                                                #
#         SUM OF SQUARES BETWEEN GROUPS          #
#                                                #
# ============================================== #

# ============================================== #
#                 GROUP_INTERN_1                 #
# ============================================== #

SSbetween_NSMD_GI1 = ((NSMD_SUM_GI1)**2 / N) - ((NSMD_ALL)**2 / (N * 2))
SSbetween_NSPD_GI1 = ((NSPD_SUM_GI1)**2 / N) - ((NSPD_ALL)**2 / (N * 2))
SSbetween_NSTD_GI1 = ((NSTD_SUM_GI1)**2 / N) - ((NSTD_ALL)**2 / (N * 2))
SSbetween_NSP_GI1  = ((NSP_SUM_GI1)**2  / N) - ((NSP_ALL)**2  / (N * 2))
SSbetween_NSE_GI1  = ((NSE_SUM_GI1)**2  / N) - ((NSE_ALL)**2  / (N * 2))
SSbetween_NSF_GI1  = ((NSF_SUM_GI1)**2  / N) - ((NSF_ALL)**2  / (N * 2))

SSbetween_NMMD_GI1 = ((NMMD_SUM_GI1)**2 / N) - ((NMMD_ALL)**2 / (N * 2))
SSbetween_NMPD_GI1 = ((NMPD_SUM_GI1)**2 / N) - ((NMPD_ALL)**2 / (N * 2))
SSbetween_NMTD_GI1 = ((NMTD_SUM_GI1)**2 / N) - ((NMTD_ALL)**2 / (N * 2))
SSbetween_NMP_GI1  = ((NMP_SUM_GI1)**2  / N) - ((NMP_ALL)**2  / (N * 2))
SSbetween_NME_GI1  = ((NME_SUM_GI1)**2  / N) - ((NME_ALL)**2  / (N * 2))
SSbetween_NMF_GI1  = ((NMF_SUM_GI1)**2  / N) - ((NMF_ALL)**2  / (N * 2))

# ============================================== #
#                 GROUP_INTERN_2                 #
# ============================================== #

SSbetween_NSMD_GI2 = ((NSMD_SUM_GI2)**2 / N) - ((NSMD_ALL)**2 / (N * 2))
SSbetween_NSPD_GI2 = ((NSPD_SUM_GI2)**2 / N) - ((NSPD_ALL)**2 / (N * 2))
SSbetween_NSTD_GI2 = ((NSTD_SUM_GI2)**2 / N) - ((NSTD_ALL)**2 / (N * 2))
SSbetween_NSP_GI2  = ((NSP_SUM_GI2)**2  / N) - ((NSP_ALL)**2  / (N * 2))
SSbetween_NSE_GI2  = ((NSE_SUM_GI2)**2  / N) - ((NSE_ALL)**2  / (N * 2))
SSbetween_NSF_GI2  = ((NSF_SUM_GI2)**2  / N) - ((NSF_ALL)**2  / (N * 2))

SSbetween_NMMD_GI2 = ((NMMD_SUM_GI2)**2 / N) - ((NMMD_ALL)**2 / (N * 2))
SSbetween_NMPD_GI2 = ((NMPD_SUM_GI2)**2 / N) - ((NMPD_ALL)**2 / (N * 2))
SSbetween_NMTD_GI2 = ((NMTD_SUM_GI2)**2 / N) - ((NMTD_ALL)**2 / (N * 2))
SSbetween_NMP_GI2  = ((NMP_SUM_GI2)**2  / N) - ((NMP_ALL)**2  / (N * 2))
SSbetween_NME_GI2  = ((NME_SUM_GI2)**2  / N) - ((NME_ALL)**2  / (N * 2))
SSbetween_NMF_GI2  = ((NMF_SUM_GI2)**2  / N) - ((NMF_ALL)**2  / (N * 2))

# ============================================== #
#                 GROUP_JUNIOR_1                 #
# ============================================== #

SSbetween_NSMD_GJ1 = ((NSMD_SUM_GJ1)**2 / N) - ((NSMD_ALL)**2 / (N * 2))
SSbetween_NSPD_GJ1 = ((NSPD_SUM_GJ1)**2 / N) - ((NSPD_ALL)**2 / (N * 2))
SSbetween_NSTD_GJ1 = ((NSTD_SUM_GJ1)**2 / N) - ((NSTD_ALL)**2 / (N * 2))
SSbetween_NSP_GJ1  = ((NSP_SUM_GJ1)**2  / N) - ((NSP_ALL)**2  / (N * 2))
SSbetween_NSE_GJ1  = ((NSE_SUM_GJ1)**2  / N) - ((NSE_ALL)**2  / (N * 2))
SSbetween_NSF_GJ1  = ((NSF_SUM_GJ1)**2  / N) - ((NSF_ALL)**2  / (N * 2))

SSbetween_NMMD_GJ1 = ((NMMD_SUM_GJ1)**2 / N) - ((NMMD_ALL)**2 / (N * 2))
SSbetween_NMPD_GJ1 = ((NMPD_SUM_GJ1)**2 / N) - ((NMPD_ALL)**2 / (N * 2))
SSbetween_NMTD_GJ1 = ((NMTD_SUM_GJ1)**2 / N) - ((NMTD_ALL)**2 / (N * 2))
SSbetween_NMP_GJ1  = ((NMP_SUM_GJ1)**2  / N) - ((NMP_ALL)**2  / (N * 2))
SSbetween_NME_GJ1  = ((NME_SUM_GJ1)**2  / N) - ((NME_ALL)**2  / (N * 2))
SSbetween_NMF_GJ1  = ((NMF_SUM_GJ1)**2  / N) - ((NMF_ALL)**2  / (N * 2))

# ============================================== #
#                 GROUP_JUNIOR_2                 #
# ============================================== #

SSbetween_NSMD_GJ2 = ((NSMD_SUM_GJ2)**2 / N) - ((NSMD_ALL)**2 / (N * 2))
SSbetween_NSPD_GJ2 = ((NSPD_SUM_GJ2)**2 / N) - ((NSPD_ALL)**2 / (N * 2))
SSbetween_NSTD_GJ2 = ((NSTD_SUM_GJ2)**2 / N) - ((NSTD_ALL)**2 / (N * 2))
SSbetween_NSP_GJ2  = ((NSP_SUM_GJ2)**2  / N) - ((NSP_ALL)**2  / (N * 2))
SSbetween_NSE_GJ2  = ((NSE_SUM_GJ2)**2  / N) - ((NSE_ALL)**2  / (N * 2))
SSbetween_NSF_GJ2  = ((NSF_SUM_GJ2)**2  / N) - ((NSF_ALL)**2  / (N * 2))

SSbetween_NMMD_GJ2 = ((NMMD_SUM_GJ2)**2 / N) - ((NMMD_ALL)**2 / (N * 2))
SSbetween_NMPD_GJ2 = ((NMPD_SUM_GJ2)**2 / N) - ((NMPD_ALL)**2 / (N * 2))
SSbetween_NMTD_GJ2 = ((NMTD_SUM_GJ2)**2 / N) - ((NMTD_ALL)**2 / (N * 2))
SSbetween_NMP_GJ2  = ((NMP_SUM_GJ2)**2  / N) - ((NMP_ALL)**2  / (N * 2))
SSbetween_NME_GJ2  = ((NME_SUM_GJ2)**2  / N) - ((NME_ALL)**2  / (N * 2))
SSbetween_NMF_GJ2  = ((NMF_SUM_GJ2)**2  / N) - ((NMF_ALL)**2  / (N * 2))

# ============================================== #
#                 GROUP_MIDDLE_1                 #
# ============================================== #

SSbetween_NSMD_GM1 = ((NSMD_SUM_GM1)**2 / N) - ((NSMD_ALL)**2 / (N * 2))
SSbetween_NSPD_GM1 = ((NSPD_SUM_GM1)**2 / N) - ((NSPD_ALL)**2 / (N * 2))
SSbetween_NSTD_GM1 = ((NSTD_SUM_GM1)**2 / N) - ((NSTD_ALL)**2 / (N * 2))
SSbetween_NSP_GM1  = ((NSP_SUM_GM1)**2  / N) - ((NSP_ALL)**2  / (N * 2))
SSbetween_NSE_GM1  = ((NSE_SUM_GM1)**2  / N) - ((NSE_ALL)**2  / (N * 2))
SSbetween_NSF_GM1  = ((NSF_SUM_GM1)**2  / N) - ((NSF_ALL)**2  / (N * 2))

SSbetween_NMMD_GM1 = ((NMMD_SUM_GM1)**2 / N) - ((NMMD_ALL)**2 / (N * 2))
SSbetween_NMPD_GM1 = ((NMPD_SUM_GM1)**2 / N) - ((NMPD_ALL)**2 / (N * 2))
SSbetween_NMTD_GM1 = ((NMTD_SUM_GM1)**2 / N) - ((NMTD_ALL)**2 / (N * 2))
SSbetween_NMP_GM1  = ((NMP_SUM_GM1)**2  / N) - ((NMP_ALL)**2  / (N * 2))
SSbetween_NME_GM1  = ((NME_SUM_GM1)**2  / N) - ((NME_ALL)**2  / (N * 2))
SSbetween_NMF_GM1  = ((NMF_SUM_GM1)**2  / N) - ((NMF_ALL)**2  / (N * 2))

# ============================================== #
#                 GROUP_MIDDLE_2                 #
# ============================================== #

SSbetween_NSMD_GM2 = ((NSMD_SUM_GM2)**2 / N) - ((NSMD_ALL)**2 / (N * 2))
SSbetween_NSPD_GM2 = ((NSPD_SUM_GM2)**2 / N) - ((NSPD_ALL)**2 / (N * 2))
SSbetween_NSTD_GM2 = ((NSTD_SUM_GM2)**2 / N) - ((NSTD_ALL)**2 / (N * 2))
SSbetween_NSP_GM2  = ((NSP_SUM_GM2)**2  / N) - ((NSP_ALL)**2  / (N * 2))
SSbetween_NSE_GM2  = ((NSE_SUM_GM2)**2  / N) - ((NSE_ALL)**2  / (N * 2))
SSbetween_NSF_GM2  = ((NSF_SUM_GM2)**2  / N) - ((NSF_ALL)**2  / (N * 2))

SSbetween_NMMD_GM2 = ((NMMD_SUM_GM2)**2 / N) - ((NMMD_ALL)**2 / (N * 2))
SSbetween_NMPD_GM2 = ((NMPD_SUM_GM2)**2 / N) - ((NMPD_ALL)**2 / (N * 2))
SSbetween_NMTD_GM2 = ((NMTD_SUM_GM2)**2 / N) - ((NMTD_ALL)**2 / (N * 2))
SSbetween_NMP_GM2  = ((NMP_SUM_GM2)**2  / N) - ((NMP_ALL)**2  / (N * 2))
SSbetween_NME_GM2  = ((NME_SUM_GM2)**2  / N) - ((NME_ALL)**2  / (N * 2))
SSbetween_NMF_GM2  = ((NMF_SUM_GM2)**2  / N) - ((NMF_ALL)**2  / (N * 2))

# ============================================== #
#                 GROUP_SENIOR_1                 #
# ============================================== #

SSbetween_NSMD_GS1 = ((NSMD_SUM_GS1)**2 / N) - ((NSMD_ALL)**2 / (N * 2))
SSbetween_NSPD_GS1 = ((NSPD_SUM_GS1)**2 / N) - ((NSPD_ALL)**2 / (N * 2))
SSbetween_NSTD_GS1 = ((NSTD_SUM_GS1)**2 / N) - ((NSTD_ALL)**2 / (N * 2))
SSbetween_NSP_GS1  = ((NSP_SUM_GS1)**2  / N) - ((NSP_ALL)**2  / (N * 2))
SSbetween_NSE_GS1  = ((NSE_SUM_GS1)**2  / N) - ((NSE_ALL)**2  / (N * 2))
SSbetween_NSF_GS1  = ((NSF_SUM_GS1)**2  / N) - ((NSF_ALL)**2  / (N * 2))

SSbetween_NMMD_GS1 = ((NMMD_SUM_GS1)**2 / N) - ((NMMD_ALL)**2 / (N * 2))
SSbetween_NMPD_GS1 = ((NMPD_SUM_GS1)**2 / N) - ((NMPD_ALL)**2 / (N * 2))
SSbetween_NMTD_GS1 = ((NMTD_SUM_GS1)**2 / N) - ((NMTD_ALL)**2 / (N * 2))
SSbetween_NMP_GS1  = ((NMP_SUM_GS1)**2  / N) - ((NMP_ALL)**2  / (N * 2))
SSbetween_NME_GS1  = ((NME_SUM_GS1)**2  / N) - ((NME_ALL)**2  / (N * 2))
SSbetween_NMF_GS1  = ((NMF_SUM_GS1)**2  / N) - ((NMF_ALL)**2  / (N * 2))

# ============================================== #
#                 GROUP_SENIOR_2                 #
# ============================================== #

SSbetween_NSMD_GS2 = ((NSMD_SUM_GS2)**2 / N) - ((NSMD_ALL)**2 / (N * 2))
SSbetween_NSPD_GS2 = ((NSPD_SUM_GS2)**2 / N) - ((NSPD_ALL)**2 / (N * 2))
SSbetween_NSTD_GS2 = ((NSTD_SUM_GS2)**2 / N) - ((NSTD_ALL)**2 / (N * 2))
SSbetween_NSP_GS2  = ((NSP_SUM_GS2)**2  / N) - ((NSP_ALL)**2  / (N * 2))
SSbetween_NSE_GS2  = ((NSE_SUM_GS2)**2  / N) - ((NSE_ALL)**2  / (N * 2))
SSbetween_NSF_GS2  = ((NSF_SUM_GS2)**2  / N) - ((NSF_ALL)**2  / (N * 2))

SSbetween_NMMD_GS2 = ((NMMD_SUM_GS2)**2 / N) - ((NMMD_ALL)**2 / (N * 2))
SSbetween_NMPD_GS2 = ((NMPD_SUM_GS2)**2 / N) - ((NMPD_ALL)**2 / (N * 2))
SSbetween_NMTD_GS2 = ((NMTD_SUM_GS2)**2 / N) - ((NMTD_ALL)**2 / (N * 2))
SSbetween_NMP_GS2  = ((NMP_SUM_GS2)**2  / N) - ((NMP_ALL)**2  / (N * 2))
SSbetween_NME_GS2  = ((NME_SUM_GS2)**2  / N) - ((NME_ALL)**2  / (N * 2))
SSbetween_NMF_GS2  = ((NMF_SUM_GS2)**2  / N) - ((NMF_ALL)**2  / (N * 2))

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

print(NSMD_SUM_GI1)
print(NSMD_ALL)
print(SSbetween_NSMD_GI1)

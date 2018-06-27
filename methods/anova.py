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
#                 GROUP_INTERN_1                 #
# ============================================== #

NSMD_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_SINGLE_PERFORMANCE)
NSE_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_SINGLE_EFFORT)
NSF_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_SINGLE_FRUSTRATION)

# NMMD_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_MULTI_MENTAL_DEMAND)
# NMPD_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_MULTI_PHYSICAL_DEMAND)
# NMTD_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_MULTI_TEMPORAL_DEMAND)
# NMP_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_MULTI_PERFORMANCE)
# NME_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_MULTI_EFFORT)
# NMF_SUM_GI1 = sheetReaderSum(GROUP_INTERN_1, NASATLX_MULTI_FRUSTRATION)

NSMD_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_SINGLE_PERFORMANCE)
NSE_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_SINGLE_EFFORT)
NSF_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_SINGLE_FRUSTRATION)

print(NSF_MEAN_GI1)

# NMMD_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_MULTI_MENTAL_DEMAND)
# NMPD_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_MULTI_PHYSICAL_DEMAND)
# NMTD_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_MULTI_TEMPORAL_DEMAND)
# NMP_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_MULTI_PERFORMANCE)
# NME_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_MULTI_EFFORT)
# NMF_MEAN_GI1 = sheetReaderMean(GROUP_INTERN_1, NASATLX_MULTI_FRUSTRATION)

# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                 GROUP_INTERN_2                 #
# ============================================== #

# NSMD_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_SINGLE_MENTAL_DEMAND)
# NSPD_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_SINGLE_PHYSICAL_DEMAND)
# NSTD_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_SINGLE_TEMPORAL_DEMAND)
# NSP_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_SINGLE_PERFORMANCE)
# NSE_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_SINGLE_EFFORT)
# NSF_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_SINGLE_FRUSTRATION)

# NMMD_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_MULTI_MENTAL_DEMAND)
# NMPD_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_MULTI_PHYSICAL_DEMAND)
# NMTD_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_MULTI_TEMPORAL_DEMAND)
# NMP_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_MULTI_PERFORMANCE)
# NME_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_MULTI_EFFORT)
# NMF_SUM_GI2 = sheetReaderSum(GROUP_INTERN_2, NASATLX_MULTI_FRUSTRATION)

# NSMD_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_SINGLE_MENTAL_DEMAND)
# NSPD_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_SINGLE_PHYSICAL_DEMAND)
# NSTD_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_SINGLE_TEMPORAL_DEMAND)
# NSP_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_SINGLE_PERFORMANCE)
# NSE_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_SINGLE_EFFORT)
# NSF_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_SINGLE_FRUSTRATION)

# NMMD_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_MULTI_MENTAL_DEMAND)
# NMPD_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_MULTI_PHYSICAL_DEMAND)
# NMTD_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_MULTI_TEMPORAL_DEMAND)
# NMP_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_MULTI_PERFORMANCE)
# NME_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_MULTI_EFFORT)
# NMF_MEAN_GI2 = sheetReaderMean(GROUP_INTERN_2, NASATLX_MULTI_FRUSTRATION)

# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                 GROUP_JUNIOR_1                 #
# ============================================== #

# NSMD_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_SINGLE_MENTAL_DEMAND)
# NSPD_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_SINGLE_PHYSICAL_DEMAND)
# NSTD_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_SINGLE_TEMPORAL_DEMAND)
# NSP_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_SINGLE_PERFORMANCE)
# NSE_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_SINGLE_EFFORT)
# NSF_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_SINGLE_FRUSTRATION)

# NMMD_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_MULTI_MENTAL_DEMAND)
# NMPD_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_MULTI_PHYSICAL_DEMAND)
# NMTD_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_MULTI_TEMPORAL_DEMAND)
# NMP_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_MULTI_PERFORMANCE)
# NME_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_MULTI_EFFORT)
# NMF_SUM_GJ1 = sheetReaderSum(GROUP_JUNIOR_1, NASATLX_MULTI_FRUSTRATION)

# NSMD_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_SINGLE_MENTAL_DEMAND)
# NSPD_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_SINGLE_PHYSICAL_DEMAND)
# NSTD_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_SINGLE_TEMPORAL_DEMAND)
# NSP_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_SINGLE_PERFORMANCE)
# NSE_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_SINGLE_EFFORT)
# NSF_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_SINGLE_FRUSTRATION)

# NMMD_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_MULTI_MENTAL_DEMAND)
# NMPD_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_MULTI_PHYSICAL_DEMAND)
# NMTD_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_MULTI_TEMPORAL_DEMAND)
# NMP_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_MULTI_PERFORMANCE)
# NME_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_MULTI_EFFORT)
# NMF_MEAN_GJ1 = sheetReaderMean(GROUP_JUNIOR_1, NASATLX_MULTI_FRUSTRATION)

# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                 GROUP_JUNIOR_2                 #
# ============================================== #

# NSMD_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_SINGLE_MENTAL_DEMAND)
# NSPD_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_SINGLE_PHYSICAL_DEMAND)
# NSTD_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_SINGLE_TEMPORAL_DEMAND)
# NSP_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_SINGLE_PERFORMANCE)
# NSE_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_SINGLE_EFFORT)
# NSF_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_SINGLE_FRUSTRATION)

# NMMD_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_MULTI_MENTAL_DEMAND)
# NMPD_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_MULTI_PHYSICAL_DEMAND)
# NMTD_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_MULTI_TEMPORAL_DEMAND)
# NMP_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_MULTI_PERFORMANCE)
# NME_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_MULTI_EFFORT)
# NMF_SUM_GJ2 = sheetReaderSum(GROUP_JUNIOR_2, NASATLX_MULTI_FRUSTRATION)

# NSMD_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_SINGLE_MENTAL_DEMAND)
# NSPD_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_SINGLE_PHYSICAL_DEMAND)
# NSTD_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_SINGLE_TEMPORAL_DEMAND)
# NSP_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_SINGLE_PERFORMANCE)
# NSE_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_SINGLE_EFFORT)
# NSF_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_SINGLE_FRUSTRATION)

# NMMD_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_MULTI_MENTAL_DEMAND)
# NMPD_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_MULTI_PHYSICAL_DEMAND)
# NMTD_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_MULTI_TEMPORAL_DEMAND)
# NMP_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_MULTI_PERFORMANCE)
# NME_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_MULTI_EFFORT)
# NMF_MEAN_GJ2 = sheetReaderMean(GROUP_JUNIOR_2, NASATLX_MULTI_FRUSTRATION)

# ============================================== #
# ============================================== #
# ============================================== #

NSMD_ALL = nasaColMean(NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_ALL = nasaColMean(NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_ALL = nasaColMean(NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_ALL = nasaColMean(NASATLX_SINGLE_PERFORMANCE)
NSE_ALL = nasaColMean(NASATLX_SINGLE_EFFORT)
NSF_ALL = nasaColMean(NASATLX_SINGLE_FRUSTRATION)

SSbetween_NSMD_GI1 = ((NSMD_SUM_GI1)**2 / N) - ((NSMD_ALL)**2 / (N * 2))
# SSbetween_NSMD_GI2 = ((NSMD_SUM_GI2)**2 / N) - ((NSMD_ALL)**2 / (N * 2))

print(SSbetween_NSMD_GI1)

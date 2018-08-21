#!/usr/bin/env python

"""anova.py: A python version of ANOVA."""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "ACADEMIC & COMMERCIAL"
__version__     = "1.2.2"
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

sa_scripts_dir = (pathAbsPath + '/statistical-analysis/scripts/')
src_dir = (pathAbsPath + '/sheet-reader/src/')
constants_dir = (pathAbsPath + '/sheet-reader/constants/')
scripts_dir = (pathAbsPath + '/sheet-reader/scripts/')
constants_dir = (pathAbsPath + '/sheet-reader/constants/')

sys.path.append(sa_scripts_dir)
sys.path.append(src_dir)
sys.path.append(constants_dir)
sys.path.append(scripts_dir)
sys.path.append(constants_dir)

from nasa import nasaColMean
import main_variables
import sheetReadersmain_sheet
import main_variables

# ============================================== #
#                IMPORT VARIABLES                #
# ============================================== #

MIN_VAL = main_variables.MIN_VAL
MAX_VAL = main_variables.MAX_VAL
N       = main_variables.N

GROUP_INTERN = main_variables.GROUP_INTERN
GROUP_JUNIOR = main_variables.GROUP_JUNIOR
GROUP_MIDDLE = main_variables.GROUP_MIDDLE
GROUP_SENIOR = main_variables.GROUP_SENIOR

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
#                  GROUP_INTERN                  #
# ============================================== #

NSMD_SUM_GI = sheetReaderSum(GROUP_INTERN, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_SUM_GI = sheetReaderSum(GROUP_INTERN, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_SUM_GI = sheetReaderSum(GROUP_INTERN, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_SUM_GI = sheetReaderSum(GROUP_INTERN, NASATLX_SINGLE_PERFORMANCE)
NSE_SUM_GI = sheetReaderSum(GROUP_INTERN, NASATLX_SINGLE_EFFORT)
NSF_SUM_GI = sheetReaderSum(GROUP_INTERN, NASATLX_SINGLE_FRUSTRATION)

NMMD_SUM_GI = sheetReaderSum(GROUP_INTERN, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_SUM_GI = sheetReaderSum(GROUP_INTERN, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_SUM_GI = sheetReaderSum(GROUP_INTERN, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_SUM_GI = sheetReaderSum(GROUP_INTERN, NASATLX_MULTI_PERFORMANCE)
NME_SUM_GI = sheetReaderSum(GROUP_INTERN, NASATLX_MULTI_EFFORT)
NMF_SUM_GI = sheetReaderSum(GROUP_INTERN, NASATLX_MULTI_FRUSTRATION)

NSMD_MEAN_GI = sheetReaderMean(GROUP_INTERN, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_MEAN_GI = sheetReaderMean(GROUP_INTERN, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_MEAN_GI = sheetReaderMean(GROUP_INTERN, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_MEAN_GI = sheetReaderMean(GROUP_INTERN, NASATLX_SINGLE_PERFORMANCE)
NSE_MEAN_GI = sheetReaderMean(GROUP_INTERN, NASATLX_SINGLE_EFFORT)
NSF_MEAN_GI = sheetReaderMean(GROUP_INTERN, NASATLX_SINGLE_FRUSTRATION)

NMMD_MEAN_GI = sheetReaderMean(GROUP_INTERN, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_MEAN_GI = sheetReaderMean(GROUP_INTERN, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_MEAN_GI = sheetReaderMean(GROUP_INTERN, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_MEAN_GI = sheetReaderMean(GROUP_INTERN, NASATLX_MULTI_PERFORMANCE)
NME_MEAN_GI = sheetReaderMean(GROUP_INTERN, NASATLX_MULTI_EFFORT)
NMF_MEAN_GI = sheetReaderMean(GROUP_INTERN, NASATLX_MULTI_FRUSTRATION)

# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                 GROUP_JUNIOR                 #
# ============================================== #

NSMD_SUM_GJ = sheetReaderSum(GROUP_JUNIOR, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_SUM_GJ = sheetReaderSum(GROUP_JUNIOR, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_SUM_GJ = sheetReaderSum(GROUP_JUNIOR, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_SUM_GJ = sheetReaderSum(GROUP_JUNIOR, NASATLX_SINGLE_PERFORMANCE)
NSE_SUM_GJ = sheetReaderSum(GROUP_JUNIOR, NASATLX_SINGLE_EFFORT)
NSF_SUM_GJ = sheetReaderSum(GROUP_JUNIOR, NASATLX_SINGLE_FRUSTRATION)

NMMD_SUM_GJ = sheetReaderSum(GROUP_JUNIOR, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_SUM_GJ = sheetReaderSum(GROUP_JUNIOR, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_SUM_GJ = sheetReaderSum(GROUP_JUNIOR, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_SUM_GJ = sheetReaderSum(GROUP_JUNIOR, NASATLX_MULTI_PERFORMANCE)
NME_SUM_GJ = sheetReaderSum(GROUP_JUNIOR, NASATLX_MULTI_EFFORT)
NMF_SUM_GJ = sheetReaderSum(GROUP_JUNIOR, NASATLX_MULTI_FRUSTRATION)

NSMD_MEAN_GJ = sheetReaderMean(GROUP_JUNIOR, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_MEAN_GJ = sheetReaderMean(GROUP_JUNIOR, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_MEAN_GJ = sheetReaderMean(GROUP_JUNIOR, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_MEAN_GJ = sheetReaderMean(GROUP_JUNIOR, NASATLX_SINGLE_PERFORMANCE)
NSE_MEAN_GJ = sheetReaderMean(GROUP_JUNIOR, NASATLX_SINGLE_EFFORT)
NSF_MEAN_GJ = sheetReaderMean(GROUP_JUNIOR, NASATLX_SINGLE_FRUSTRATION)

NMMD_MEAN_GJ = sheetReaderMean(GROUP_JUNIOR, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_MEAN_GJ = sheetReaderMean(GROUP_JUNIOR, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_MEAN_GJ = sheetReaderMean(GROUP_JUNIOR, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_MEAN_GJ = sheetReaderMean(GROUP_JUNIOR, NASATLX_MULTI_PERFORMANCE)
NME_MEAN_GJ = sheetReaderMean(GROUP_JUNIOR, NASATLX_MULTI_EFFORT)
NMF_MEAN_GJ = sheetReaderMean(GROUP_JUNIOR, NASATLX_MULTI_FRUSTRATION)

# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                 GROUP_MIDDLE                 #
# ============================================== #

NSMD_SUM_GM = sheetReaderSum(GROUP_MIDDLE, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_SUM_GM = sheetReaderSum(GROUP_MIDDLE, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_SUM_GM = sheetReaderSum(GROUP_MIDDLE, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_SUM_GM = sheetReaderSum(GROUP_MIDDLE, NASATLX_SINGLE_PERFORMANCE)
NSE_SUM_GM = sheetReaderSum(GROUP_MIDDLE, NASATLX_SINGLE_EFFORT)
NSF_SUM_GM = sheetReaderSum(GROUP_MIDDLE, NASATLX_SINGLE_FRUSTRATION)

NMMD_SUM_GM = sheetReaderSum(GROUP_MIDDLE, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_SUM_GM = sheetReaderSum(GROUP_MIDDLE, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_SUM_GM = sheetReaderSum(GROUP_MIDDLE, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_SUM_GM = sheetReaderSum(GROUP_MIDDLE, NASATLX_MULTI_PERFORMANCE)
NME_SUM_GM = sheetReaderSum(GROUP_MIDDLE, NASATLX_MULTI_EFFORT)
NMF_SUM_GM = sheetReaderSum(GROUP_MIDDLE, NASATLX_MULTI_FRUSTRATION)

NSMD_MEAN_GM = sheetReaderMean(GROUP_MIDDLE, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_MEAN_GM = sheetReaderMean(GROUP_MIDDLE, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_MEAN_GM = sheetReaderMean(GROUP_MIDDLE, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_MEAN_GM = sheetReaderMean(GROUP_MIDDLE, NASATLX_SINGLE_PERFORMANCE)
NSE_MEAN_GM = sheetReaderMean(GROUP_MIDDLE, NASATLX_SINGLE_EFFORT)
NSF_MEAN_GM = sheetReaderMean(GROUP_MIDDLE, NASATLX_SINGLE_FRUSTRATION)

NMMD_MEAN_GM = sheetReaderMean(GROUP_MIDDLE, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_MEAN_GM = sheetReaderMean(GROUP_MIDDLE, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_MEAN_GM = sheetReaderMean(GROUP_MIDDLE, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_MEAN_GM = sheetReaderMean(GROUP_MIDDLE, NASATLX_MULTI_PERFORMANCE)
NME_MEAN_GM = sheetReaderMean(GROUP_MIDDLE, NASATLX_MULTI_EFFORT)
NMF_MEAN_GM = sheetReaderMean(GROUP_MIDDLE, NASATLX_MULTI_FRUSTRATION)

# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                 GROUP_SENIOR                 #
# ============================================== #

NSMD_SUM_GS = sheetReaderSum(GROUP_SENIOR, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_SUM_GS = sheetReaderSum(GROUP_SENIOR, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_SUM_GS = sheetReaderSum(GROUP_SENIOR, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_SUM_GS = sheetReaderSum(GROUP_SENIOR, NASATLX_SINGLE_PERFORMANCE)
NSE_SUM_GS = sheetReaderSum(GROUP_SENIOR, NASATLX_SINGLE_EFFORT)
NSF_SUM_GS = sheetReaderSum(GROUP_SENIOR, NASATLX_SINGLE_FRUSTRATION)

NMMD_SUM_GS = sheetReaderSum(GROUP_SENIOR, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_SUM_GS = sheetReaderSum(GROUP_SENIOR, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_SUM_GS = sheetReaderSum(GROUP_SENIOR, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_SUM_GS = sheetReaderSum(GROUP_SENIOR, NASATLX_MULTI_PERFORMANCE)
NME_SUM_GS = sheetReaderSum(GROUP_SENIOR, NASATLX_MULTI_EFFORT)
NMF_SUM_GS = sheetReaderSum(GROUP_SENIOR, NASATLX_MULTI_FRUSTRATION)

NSMD_MEAN_GS = sheetReaderMean(GROUP_SENIOR, NASATLX_SINGLE_MENTAL_DEMAND)
NSPD_MEAN_GS = sheetReaderMean(GROUP_SENIOR, NASATLX_SINGLE_PHYSICAL_DEMAND)
NSTD_MEAN_GS = sheetReaderMean(GROUP_SENIOR, NASATLX_SINGLE_TEMPORAL_DEMAND)
NSP_MEAN_GS = sheetReaderMean(GROUP_SENIOR, NASATLX_SINGLE_PERFORMANCE)
NSE_MEAN_GS = sheetReaderMean(GROUP_SENIOR, NASATLX_SINGLE_EFFORT)
NSF_MEAN_GS = sheetReaderMean(GROUP_SENIOR, NASATLX_SINGLE_FRUSTRATION)

NMMD_MEAN_GS = sheetReaderMean(GROUP_SENIOR, NASATLX_MULTI_MENTAL_DEMAND)
NMPD_MEAN_GS = sheetReaderMean(GROUP_SENIOR, NASATLX_MULTI_PHYSICAL_DEMAND)
NMTD_MEAN_GS = sheetReaderMean(GROUP_SENIOR, NASATLX_MULTI_TEMPORAL_DEMAND)
NMP_MEAN_GS = sheetReaderMean(GROUP_SENIOR, NASATLX_MULTI_PERFORMANCE)
NME_MEAN_GS = sheetReaderMean(GROUP_SENIOR, NASATLX_MULTI_EFFORT)
NMF_MEAN_GS = sheetReaderMean(GROUP_SENIOR, NASATLX_MULTI_FRUSTRATION)

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
#                 GROUP_INTERN                 #
# ============================================== #

SSbetween_NSMD_GI = ((NSMD_SUM_GI)**2 / N) - ((NSMD_ALL)**2 / (N * 2))
SSbetween_NSPD_GI = ((NSPD_SUM_GI)**2 / N) - ((NSPD_ALL)**2 / (N * 2))
SSbetween_NSTD_GI = ((NSTD_SUM_GI)**2 / N) - ((NSTD_ALL)**2 / (N * 2))
SSbetween_NSP_GI  = ((NSP_SUM_GI)**2  / N) - ((NSP_ALL)**2  / (N * 2))
SSbetween_NSE_GI  = ((NSE_SUM_GI)**2  / N) - ((NSE_ALL)**2  / (N * 2))
SSbetween_NSF_GI  = ((NSF_SUM_GI)**2  / N) - ((NSF_ALL)**2  / (N * 2))

SSbetween_NMMD_GI = ((NMMD_SUM_GI)**2 / N) - ((NMMD_ALL)**2 / (N * 2))
SSbetween_NMPD_GI = ((NMPD_SUM_GI)**2 / N) - ((NMPD_ALL)**2 / (N * 2))
SSbetween_NMTD_GI = ((NMTD_SUM_GI)**2 / N) - ((NMTD_ALL)**2 / (N * 2))
SSbetween_NMP_GI  = ((NMP_SUM_GI)**2  / N) - ((NMP_ALL)**2  / (N * 2))
SSbetween_NME_GI  = ((NME_SUM_GI)**2  / N) - ((NME_ALL)**2  / (N * 2))
SSbetween_NMF_GI  = ((NMF_SUM_GI)**2  / N) - ((NMF_ALL)**2  / (N * 2))

# ============================================== #
#                 GROUP_JUNIOR                 #
# ============================================== #

SSbetween_NSMD_GJ = ((NSMD_SUM_GJ)**2 / N) - ((NSMD_ALL)**2 / (N * 2))
SSbetween_NSPD_GJ = ((NSPD_SUM_GJ)**2 / N) - ((NSPD_ALL)**2 / (N * 2))
SSbetween_NSTD_GJ = ((NSTD_SUM_GJ)**2 / N) - ((NSTD_ALL)**2 / (N * 2))
SSbetween_NSP_GJ  = ((NSP_SUM_GJ)**2  / N) - ((NSP_ALL)**2  / (N * 2))
SSbetween_NSE_GJ  = ((NSE_SUM_GJ)**2  / N) - ((NSE_ALL)**2  / (N * 2))
SSbetween_NSF_GJ  = ((NSF_SUM_GJ)**2  / N) - ((NSF_ALL)**2  / (N * 2))

SSbetween_NMMD_GJ = ((NMMD_SUM_GJ)**2 / N) - ((NMMD_ALL)**2 / (N * 2))
SSbetween_NMPD_GJ = ((NMPD_SUM_GJ)**2 / N) - ((NMPD_ALL)**2 / (N * 2))
SSbetween_NMTD_GJ = ((NMTD_SUM_GJ)**2 / N) - ((NMTD_ALL)**2 / (N * 2))
SSbetween_NMP_GJ  = ((NMP_SUM_GJ)**2  / N) - ((NMP_ALL)**2  / (N * 2))
SSbetween_NME_GJ  = ((NME_SUM_GJ)**2  / N) - ((NME_ALL)**2  / (N * 2))
SSbetween_NMF_GJ  = ((NMF_SUM_GJ)**2  / N) - ((NMF_ALL)**2  / (N * 2))

# ============================================== #
#                 GROUP_MIDDLE                 #
# ============================================== #

SSbetween_NSMD_GM = ((NSMD_SUM_GM)**2 / N) - ((NSMD_ALL)**2 / (N * 2))
SSbetween_NSPD_GM = ((NSPD_SUM_GM)**2 / N) - ((NSPD_ALL)**2 / (N * 2))
SSbetween_NSTD_GM = ((NSTD_SUM_GM)**2 / N) - ((NSTD_ALL)**2 / (N * 2))
SSbetween_NSP_GM  = ((NSP_SUM_GM)**2  / N) - ((NSP_ALL)**2  / (N * 2))
SSbetween_NSE_GM  = ((NSE_SUM_GM)**2  / N) - ((NSE_ALL)**2  / (N * 2))
SSbetween_NSF_GM  = ((NSF_SUM_GM)**2  / N) - ((NSF_ALL)**2  / (N * 2))

SSbetween_NMMD_GM = ((NMMD_SUM_GM)**2 / N) - ((NMMD_ALL)**2 / (N * 2))
SSbetween_NMPD_GM = ((NMPD_SUM_GM)**2 / N) - ((NMPD_ALL)**2 / (N * 2))
SSbetween_NMTD_GM = ((NMTD_SUM_GM)**2 / N) - ((NMTD_ALL)**2 / (N * 2))
SSbetween_NMP_GM  = ((NMP_SUM_GM)**2  / N) - ((NMP_ALL)**2  / (N * 2))
SSbetween_NME_GM  = ((NME_SUM_GM)**2  / N) - ((NME_ALL)**2  / (N * 2))
SSbetween_NMF_GM  = ((NMF_SUM_GM)**2  / N) - ((NMF_ALL)**2  / (N * 2))

# ============================================== #
#                 GROUP_SENIOR                 #
# ============================================== #

SSbetween_NSMD_GS = ((NSMD_SUM_GS)**2 / N) - ((NSMD_ALL)**2 / (N * 2))
SSbetween_NSPD_GS = ((NSPD_SUM_GS)**2 / N) - ((NSPD_ALL)**2 / (N * 2))
SSbetween_NSTD_GS = ((NSTD_SUM_GS)**2 / N) - ((NSTD_ALL)**2 / (N * 2))
SSbetween_NSP_GS  = ((NSP_SUM_GS)**2  / N) - ((NSP_ALL)**2  / (N * 2))
SSbetween_NSE_GS  = ((NSE_SUM_GS)**2  / N) - ((NSE_ALL)**2  / (N * 2))
SSbetween_NSF_GS  = ((NSF_SUM_GS)**2  / N) - ((NSF_ALL)**2  / (N * 2))

SSbetween_NMMD_GS = ((NMMD_SUM_GS)**2 / N) - ((NMMD_ALL)**2 / (N * 2))
SSbetween_NMPD_GS = ((NMPD_SUM_GS)**2 / N) - ((NMPD_ALL)**2 / (N * 2))
SSbetween_NMTD_GS = ((NMTD_SUM_GS)**2 / N) - ((NMTD_ALL)**2 / (N * 2))
SSbetween_NMP_GS  = ((NMP_SUM_GS)**2  / N) - ((NMP_ALL)**2  / (N * 2))
SSbetween_NME_GS  = ((NME_SUM_GS)**2  / N) - ((NME_ALL)**2  / (N * 2))
SSbetween_NMF_GS  = ((NMF_SUM_GS)**2  / N) - ((NMF_ALL)**2  / (N * 2))

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

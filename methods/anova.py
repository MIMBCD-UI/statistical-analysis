#!/usr/bin/env python

"""anova.py: A python version of ANOVA."""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "ACADEMIC & COMMERCIAL"
__version__     = "1.1.0"
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
#pathDirname = '/Users/Francisco/Git/statistical-analysis/methods/anova.py'
joinPath = os.path.join(pathDirname, '..', '..')
pathAbsPath = os.path.abspath(joinPath)
#pathAbsPath = '/Users/Francisco/Git/statistical-analysis/methods/anova.py'

print(pathDirname)

sa_scripts_dir = (pathAbsPath + '/statistical-analysis/scripts/')
sys.path.append(sa_scripts_dir)

from nasa import nasaColMean

src_dir = (pathAbsPath + '/sheet-reader/src/')
sys.path.append(src_dir)

constants_dir = (pathAbsPath + '/sheet-reader/constants/')
sys.path.append(constants_dir)
import main_variables

scripts_dir = (pathAbsPath + '/sheet-reader/scripts/')
sys.path.append(scripts_dir)
import sheetReaders

main_sheet_dir = pathAbsPath + '/sheet-reader/temp/main_sheet.csv'
fs_sheet_dir = pathAbsPath + '/sheet-reader/temp/fs_sheet.csv'
fm_sheet_dir = pathAbsPath + '/sheet-reader/temp/fm_sheet.csv'

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

datafile_fs = pd.read_csv(fs_sheet_dir)
datafile_fm = pd.read_csv(fm_sheet_dir)

# ============================================== #
#                                                #
#                 CREATE BOXPLOT                 #
#                                                #
# ============================================== #

# ============================================== #
#                SINGLE-MODALITY                 #
# ============================================== #

datafile_fs.boxplot('mental_demand', by='group', figsize=(12, 8))
datafile_fs.boxplot('physical_demand', by='group', figsize=(12, 8))
datafile_fs.boxplot('temporal_demand', by='group', figsize=(12, 8))
datafile_fs.boxplot('performance', by='group', figsize=(12, 8))
datafile_fs.boxplot('effort', by='group', figsize=(12, 8))
datafile_fs.boxplot('frustration', by='group', figsize=(12, 8))

# ============================================== #
#                 MULTI-MODALITY                 #
# ============================================== #

datafile_fm.boxplot('mental_demand', by='group', figsize=(12, 8))
datafile_fm.boxplot('physical_demand', by='group', figsize=(12, 8))
datafile_fm.boxplot('temporal_demand', by='group', figsize=(12, 8))
datafile_fm.boxplot('performance', by='group', figsize=(12, 8))
datafile_fm.boxplot('effort', by='group', figsize=(12, 8))
datafile_fm.boxplot('frustration', by='group', figsize=(12, 8))

# ============================================== #
# ============================================== #

# ============================================== #
#                 INITIALIZATION                 #
# ============================================== #

intern_1 = datafile_fs['mental_demand'][datafile_fs.group == 'intern_1']

grps = pd.unique(datafile_fs.group.values)
d_data = {grp:datafile_fs['mental_demand'][datafile_fs.group == grp] for grp in grps}

k = len(pd.unique(datafile_fs.group))  # number of conditions
N = len(datafile_fs.values)  # conditions times participants
n = datafile_fs.groupby('group').size()[0] #Participants in each condition

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

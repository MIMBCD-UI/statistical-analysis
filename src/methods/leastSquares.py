#!/usr/bin/env python

""".py: """

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "ACADEMIC & COMMERCIAL"
__version__     = "2.0.0"
__status__      = "Production"
__copyright__   = "Copyright 2019, Instituto Superior Técnico (IST)"
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

saJoinPath = os.path.join(pathAbsPath, 'statistical-analysis')
sys.path.append(saJoinPath)
saAbsPath = os.path.abspath(saJoinPath)

saSrcJoinPath = os.path.join(saAbsPath, 'src')
sys.path.append(saSrcJoinPath)
saSrcAbsPath = os.path.abspath(saSrcJoinPath)

saSrcConsJoinPath = os.path.join(saSrcAbsPath, 'constants')
sys.path.append(saSrcConsJoinPath)
saSrcConsAbsPath = os.path.abspath(saSrcConsJoinPath)

saSrcVarsJoinPath = os.path.join(saSrcAbsPath, 'variables')
sys.path.append(saSrcVarsJoinPath)
saSrcVarsAbsPath = os.path.abspath(saSrcVarsJoinPath)

import pandas as pd
import scipy.stats as stats
import researchpy as rp
import statsmodels.api as sm

from statsmodels.formula.api import ols
    
import matplotlib.pyplot as plt

from dataFrames import *
from sheets import *

from baseStatisticalAnalysis import *
from pathsStatisticalAnalysis import *
from messagesStatisticalAnalysis import *

# ============================================== #
#                                                #
#                     FUNCTIONS                  #
#                                                #
# ============================================== #

def anova_table(aov):
  aov['mean_sq'] = aov[:]['sum_sq'] / aov[:]['df']
  
  aov['eta_sq'] = aov[:-1]['sum_sq'] / sum(aov['sum_sq'])
  
  aov['omega_sq'] = (aov[:-1]['sum_sq']-(aov[:-1]['df']*aov['mean_sq'][-1]))/(sum(aov['sum_sq'])+aov['mean_sq'][-1])
  
  cols = ['sum_sq', 'df', 'mean_sq', 'F', 'PR(>F)', 'eta_sq', 'omega_sq']
  aov = aov[cols]
  
  return aov

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                                                #
#                       UTA7                     #
#                                                #
# ============================================== #

# ============================================== #
#           UTA7: Current vs Assistant           #
# ============================================== #

# BIRADS

# ============================================== #
# ============================================== #

# DOTS

# ============================================== #
# ============================================== #

# NASA-TLX

# ============================================== #
# ============================================== #

# NOC

# ============================================== #
# ============================================== #

# NOE

# ============================================== #
# ============================================== #

# SUS

# ============================================== #
# ============================================== #

# Time

# ============================================== #

res001 = ols('low ~ C(group)', data = df_time_full_crrnt).fit()
res001_summ = res001.summary()
aov_res001 = sm.stats.anova_lm(res001, typ = 2)
aov_t_res001 = anova_table(aov_res001)
res001_diagn = res001.diagn
res001_resid = res001.resid
res001_shp = stats.shapiro(res001_resid)

print(c010)
print(res001_shp)
print(c010)
print(aov_t_res001)
print(c010)
print(res001_diagn)
print(c010)

print(c012)
print(c012)

print(c010)
print(t007, fne002, fne004, fne105)
print(res001_summ)
print(c010)

print(c001)
print(c012)
print(aov_res001)
print(c012)
print(c001)

# ============================================== #

res002 = ols('low ~ C(group)', data = df_time_full_assis).fit()
res002_summ = res002.summary()
res002_resid = res002.resid
res002_shp = stats.shapiro(res002_resid)

print(c010)
print(res002_shp)
print(c010)
print(t007, fne002, fne003, fne105)
print(res002_summ)
print(c010)

# ============================================== #

print(c001)
print(c022)
print(c001)

# ============================================== #

res003 = ols('medium ~ C(group)', data = df_time_full_crrnt).fit()
res003_summ = res003.summary()
res003_resid = res003.resid
res003_shp = stats.shapiro(res003_resid)

print(c010)
print(res003_shp)
print(c010)
print(t007, fne002, fne004, fne104)
print(res003_summ)
print(c010)

# ============================================== #

res004 = ols('medium ~ C(group)', data = df_time_full_assis).fit()
res004_summ = res004.summary()
res004_resid = res004.resid
res004_shp = stats.shapiro(res004_resid)

print(c010)
print(res004_shp)
print(c010)
print(t007, fne002, fne003, fne104)
print(res004_summ)
print(c010)

# ============================================== #

print(c001)
print(c022)
print(c001)

# ============================================== #

res005 = ols('high ~ C(group)', data = df_time_full_crrnt).fit()
res005_summ = res005.summary()
res005_resid = res005.resid
res005_shp = stats.shapiro(res005_resid)

print(c010)
print(res005_shp)
print(c010)
print(t007, fne002, fne004, fne103)
print(res005_summ)
print(c010)

# ============================================== #

res006 = ols('high ~ C(group)', data = df_time_full_assis).fit()
res006_summ = res006.summary()
res006_resid = res006.resid
res006_shp = stats.shapiro(res006_resid)

print(c010)
print(res006_shp)
print(c010)
print(t007, fne002, fne003, fne103)
print(res006_summ)
print(c010)

# ============================================== #

# ============================================== #
# ============================================== #
# ============================================== #
# ============================================== #

# ==================== END File ==================== #
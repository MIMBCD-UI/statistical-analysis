#!/usr/bin/env python
#coding=utf-8

"""
.py:
"""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "MIT"
__version__     = "1.0.0"
__status__      = "Development"
__copyright__   = "Copyright 2019, Instituto Superior Técnico (IST)"
__credits__     = [
  "Bruno Oliveira",
  "Carlos Santiago",
  "Jacinto C. Nascimento",
  "Pedro Miraldo",
  "Nuno Nunes",
  "Duarte Figueirôa"
]

import os
import json
import sys
import requests

from os import path
from pprint import pprint

# The current folder path.
basePath = os.path.dirname(__file__)

# The path to the repository "src" folder.
srcPath = os.path.join(basePath, '..')
srcAbsPath = os.path.abspath(srcPath)
# Add the directory containing the module to
# the Python path (wants absolute paths).
sys.path.append(srcAbsPath)

# The path to the repository "src" folder.
repoPath = os.path.join(basePath, '..', '..')
repoAbsPath = os.path.abspath(repoPath)
# Add the directory containing the module to
# the Python path (wants absolute paths).
sys.path.append(repoAbsPath)

# The path to the repository "root" folder. Mainly,
# this will put us at the `Git` folder level.
rootPath = os.path.join(basePath, '..', '..', '..')
rootAbsPath = os.path.abspath(rootPath)
sys.path.append(rootAbsPath)

# Appending results path.
resultsPath = os.path.join(repoPath, 'results', '')
resultsAbsPath = os.path.abspath(resultsPath)
sys.path.append(resultsAbsPath)

# Appending history path.
resultsHistoryPath = os.path.join(resultsAbsPath, 'history', '')
resultsHistoryAbsPath = os.path.abspath(resultsHistoryPath)
sys.path.append(resultsHistoryAbsPath)

# Appending recent path.
resultsRecentPath = os.path.join(resultsAbsPath, 'recent', '')
resultsRecentAbsPath = os.path.abspath(resultsRecentPath)
sys.path.append(resultsRecentAbsPath)

# Appending temp path.
resultsTempPath = os.path.join(resultsAbsPath, 'temp', '')
resultsTempAbsPath = os.path.abspath(resultsTempPath)
sys.path.append(resultsTempAbsPath)

# Appending methods path.
methsPath = os.path.join(srcPath, 'methods')
methsAbsPath = os.path.abspath(methsPath)
sys.path.append(methsAbsPath)

# Appending tests path.
testsPath = os.path.join(srcPath, 'tests')
testsAbsPath = os.path.abspath(testsPath)
sys.path.append(testsAbsPath)

# Appending uta7-statistical-analysis-charts path.
uta7sacPath = os.path.join(rootAbsPath, 'uta7-statistical-analysis-charts')
uta7sacAbsPath = os.path.abspath(uta7sacPath)
sys.path.append(uta7sacAbsPath)

# Appending UTA7 - SAC: Src path.
uta7sacSrcPath = os.path.join(uta7sacAbsPath, 'src', '')
uta7sacSrcAbsPath = os.path.abspath(uta7sacSrcPath)
sys.path.append(uta7sacSrcAbsPath)

# ============================== #
#       FILE & Folder NAMES      #
# ============================== #

ext101 = '.txt'
ext102 = '.json'
ext103 = '.dcm'
ext104 = '.csv'
ext105 = '.html'

mul001 = '*' + ext101
mul002 = '*' + ext102

scp01 = '_'
scp02 = '-'

fn001 = 'birads'
fn002 = 'dots'
fn003 = 'nasatlx'
fn004 = 'noc'
fn005 = 'noe'
fn006 = 'sus'
fn007 = 'time'
fn008 = 'anova'
fn009 = 'ols'

fnc001 = fn001 + ext101
fnc002 = fn002 + ext101
fnc003 = fn003 + ext101
fnc004 = fn004 + ext101
fnc005 = fn005 + ext101
fnc006 = fn006 + ext101
fnc007 = fn007 + ext101

fnc101 = fn008 + scp01 + fn001 + ext101
fnc102 = fn008 + scp01 + fn002 + ext101
fnc103 = fn008 + scp01 + fn003 + ext101
fnc104 = fn008 + scp01 + fn004 + ext101
fnc105 = fn008 + scp01 + fn005 + ext101
fnc106 = fn008 + scp01 + fn006 + ext101
fnc107 = fn008 + scp01 + fn007 + ext101

fnc201 = fn009 + scp01 + fn001 + ext101
fnc202 = fn009 + scp01 + fn002 + ext101
fnc203 = fn009 + scp01 + fn003 + ext101
fnc204 = fn009 + scp01 + fn004 + ext101
fnc205 = fn009 + scp01 + fn005 + ext101
fnc206 = fn009 + scp01 + fn006 + ext101
fnc207 = fn009 + scp01 + fn007 + ext101

pn001 = 'sus_crrnt_odd'
pn002 = 'sus_crrnt_even'
pn003 = 'sus_assis_odd'
pn004 = 'sus_assis_even'

pnc001 = pn001 + ext105
pnc002 = pn002 + ext105
pnc003 = pn003 + ext105
pnc004 = pn004 + ext105

# ============================== #
# ============================== #

# ============================== #
#              PATHS             #
# ============================== #

# Path to the birads file
fp001 = os.path.join(resultsRecentAbsPath, fnc001)

# Path to the dots file
fp002 = os.path.join(resultsRecentAbsPath, fnc002)

# Path to the nasatlx file
fp003 = os.path.join(resultsRecentAbsPath, fnc003)

# Path to the noc file
fp004 = os.path.join(resultsRecentAbsPath, fnc004)

# Path to the noe file
fp005 = os.path.join(resultsRecentAbsPath, fnc005)

# Path to the sus file
fp006 = os.path.join(resultsRecentAbsPath, fnc006)

# Path to the time file
fp007 = os.path.join(resultsRecentAbsPath, fnc007)

# ============================== #

# Path to the birads file (ANOVA)
fp101 = os.path.join(resultsRecentAbsPath, fnc101)

# Path to the dots file (ANOVA)
fp102 = os.path.join(resultsRecentAbsPath, fnc102)

# Path to the nasatlx file (ANOVA)
fp103 = os.path.join(resultsRecentAbsPath, fnc103)

# Path to the noc file (ANOVA)
fp104 = os.path.join(resultsRecentAbsPath, fnc104)

# Path to the noe file (ANOVA)
fp105 = os.path.join(resultsRecentAbsPath, fnc105)

# Path to the sus file (ANOVA)
fp106 = os.path.join(resultsRecentAbsPath, fnc106)

# Path to the time file (ANOVA)
fp107 = os.path.join(resultsRecentAbsPath, fnc107)

# ============================== #

# Path to the birads file (OLS)
fp201 = os.path.join(resultsRecentAbsPath, fnc201)

# Path to the dots file (OLS)
fp202 = os.path.join(resultsRecentAbsPath, fnc202)

# Path to the nasatlx file (OLS)
fp203 = os.path.join(resultsRecentAbsPath, fnc203)

# Path to the noc file (OLS)
fp204 = os.path.join(resultsRecentAbsPath, fnc204)

# Path to the noe file (OLS)
fp205 = os.path.join(resultsRecentAbsPath, fnc205)

# Path to the sus file (OLS)
fp206 = os.path.join(resultsRecentAbsPath, fnc206)

# Path to the time file (OLS)
fp207 = os.path.join(resultsRecentAbsPath, fnc207)

# ============================== #
# ============================== #

# ============================== #
#         PATHS - Charts         #
# ============================== #

fp301 = os.path.join(uta7sacSrcAbsPath , pnc001)
fp302 = os.path.join(uta7sacSrcAbsPath , pnc002)
fp303 = os.path.join(uta7sacSrcAbsPath , pnc003)
fp304 = os.path.join(uta7sacSrcAbsPath , pnc004)

# ============================== #
# ============================== #

# ==================== END File ==================== #

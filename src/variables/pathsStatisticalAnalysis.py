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

# Appending results path.
resultsHistoryPath = os.path.join(resultsAbsPath, 'history', '')
resultsHistoryAbsPath = os.path.abspath(resultsHistoryPath)
sys.path.append(resultsHistoryAbsPath)

# Appending results path.
resultsRecentPath = os.path.join(resultsAbsPath, 'recent', '')
resultsRecentAbsPath = os.path.abspath(resultsRecentPath)
sys.path.append(resultsRecentAbsPath)

# Appending results path.
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

# ============================== #
#       FILE & Folder NAMES      #
# ============================== #

ext101 = '.txt'
ext102 = '.json'
ext103 = '.dcm'
ext104 = '.csv'

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

fnc001 = fn001 + ext101
fnc002 = fn002 + ext101
fnc003 = fn003 + ext101
fnc004 = fn004 + ext101
fnc005 = fn005 + ext101
fnc006 = fn006 + ext101
fnc007 = fn007 + ext101

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
# ============================== #

# ==================== END File ==================== #
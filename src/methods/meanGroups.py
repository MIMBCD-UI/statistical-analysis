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

sys.path.append(sa_constants_dir)

from dataFileGroups import *
from messageVars import *
from sheet import *
from special import *
from structures import *
from validators import *

import math
import numpy as np

def computeDataFileGroupsMean(arr):
  arr_sums = 0
  arr_std = 0
  for i in range(0, len(arr)):
    arr_sums = arr_sums + arr[i]
  arr_std = np.std(arr, ddof=0)
  arr_mean = arr_sums / len(arr)
  return arr_mean, arr_std

def flagDataFileGroupsMean(arr, flag):
  arr_sums = 0
  arr_std = 0
  for i in range(0, len(arr)):
    arr_sums = arr_sums + arr[i]
  if(flag == isFlag01):
    arr_mean = arr_sums / (elm_size01 * len(arr))
  elif(flag == isFlag02):
    arr_mean = arr_sums / (elm_size02 * len(arr))
  elif(flag == isFlag03):
    arr_mean = arr_sums / (elm_size03 * len(arr))
  elif(flag == isFlag04):
    arr_mean = arr_sums / (elm_size04 * len(arr))
  elif(flag == isFlag05):
    arr_mean = arr_sums / (elm_size05 * len(arr))
  elif(flag == isFlag06):
    arr_mean = arr_sums / (elm_size06 * len(arr))
  else:
    print(m_err_001)
  arr_std = np.std(arr, ddof=0)
  return arr_mean, arr_std

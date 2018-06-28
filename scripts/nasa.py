#!/usr/bin/env python

"""nasa.py: A python version of NASA-TLX Manager."""

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

constants_dir = (pathAbsPath + '/sheet-reader/constants/')
sys.path.append(constants_dir)
import main_variables

sheetReader_dir = (pathAbsPath + '/sheet-reader/src/')
sys.path.append(sheetReader_dir)

scripts_dir = (pathAbsPath + '/sheet-reader/scripts/')
sys.path.append(scripts_dir)
import sheetReaders

MIN_VAL = main_variables.MIN_VAL
MAX_VAL = main_variables.MAX_VAL
N       = main_variables.N

GROUPS_LIST = main_variables.GROUPS_LIST

def nasaColMean(column):
  NS_COL_SUM = 0
  groupsList = GROUPS_LIST
  for i in range(len(groupsList)):
    NS_COL_SUM = sheetReaderSum(groupsList[i], column)
    NS_COL_MEAN = NS_COL_SUM / N
  return NS_COL_MEAN

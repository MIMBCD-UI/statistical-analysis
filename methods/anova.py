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
sheetReader_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
+ '/sheet-reader/src/')
sys.path.append(sheetReader_dir)

import pandas as pd
datafile = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
+ '/sheet-reader/temp/sheet.csv')

data = pd.read_csv(datafile, error_bad_lines=False)

from main import sheetReader
from main import sheetReaderSum
from main import sheetReaderMean

constants_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
+ '/statistical-analysis/constants/')
sys.path.append(constants_dir)
import sheets

MIN_VAL = sheets.MIN_VAL
MAX_VAL = sheets.MAX_VAL
NASATLX_SINGLE_MENTAL_DEMAND = sheets.NASATLX_SINGLE_MENTAL_DEMAND

sheetReader(NASATLX_SINGLE_MENTAL_DEMAND, MIN_VAL, MAX_VAL)

sheetReaderSum(NASATLX_SINGLE_MENTAL_DEMAND, MIN_VAL, MAX_VAL)

sheetReaderMean(NASATLX_SINGLE_MENTAL_DEMAND, MIN_VAL, MAX_VAL)

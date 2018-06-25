import sys, os.path
sheetReader_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
+ '/sheet-reader/src/')
sys.path.append(sheetReader_dir)

import pandas as pd
datafile = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
+ '/sheet-reader/temp/sheet.csv')
print("%s" % datafile)

data = pd.read_csv(datafile, error_bad_lines=False)

from main import sheetReader
from main import sheetReaderSum
from main import sheetReaderMean

MIN_VAL = 4
MAX_VAL = 12

MIN_ROW = str(MIN_VAL)
MAX_ROW = str(MAX_VAL)

MENTAL_DEMAND_ROW = 'C'

sheetReader(MENTAL_DEMAND_ROW, MIN_VAL, MAX_VAL)

sheetReaderSum(MENTAL_DEMAND_ROW, MIN_VAL, MAX_VAL)

sheetReaderMean(MENTAL_DEMAND_ROW, MIN_VAL, MAX_VAL)

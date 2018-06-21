import sys, os.path
sheetReader_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
+ '/sheet-reader/src/')
sys.path.append(sheetReader_dir)
from main import sheetReader

MIN_VAL = 4
MAX_VAL = 12

MIN_ROW = str(MIN_VAL)
MAX_ROW = str(MAX_VAL)

SCAPE_CHAR = ':'
MENTAL_DEMAND_ROW = 'C'

sheetReader(MENTAL_DEMAND_ROW, MIN_VAL, MAX_VAL)

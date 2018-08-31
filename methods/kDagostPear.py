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
joinPath = os.path.join(pathDirname, '..', '..')
pathAbsPath = os.path.abspath(joinPath)

sa_constants_dir = (pathAbsPath + '/statistical-analysis/constants/')

sys.path.append(sa_constants_dir)

from listGroups import *

def kDagostPear(s_min, s_max):
  for s_current in range(s_min, s_max + 1):
    if s_current < 10:
      x_string = "s_" + "00" + str(s_current)
      x = globals()[x_string]
    elif 10 <= s_current < 100:
      x_string = "s_" + "0" + str(s_current)
      x = globals()[x_string]
    else:
      x_string = "s_" + str(s_current)
      x = globals()[x_string]
    dagostino_results = scipy.stats.mstats.normaltest(x)
    str_end = x_string + "\n"
    str_start = "[D'Agostino and Pearson: Kurtosis]"
    str_1 = str_start + " DF of " + str_end
    str_2 = str_start + " Test Statistic of " + str_end
    str_3 = str_start + " p-value of " + x_string + "\n"
    print(str_1, len(x) - 1)
    print(str_2, dagostino_results[0])
    print(str_3, dagostino_results[1])

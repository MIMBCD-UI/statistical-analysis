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

k_fs = len(pd.unique(datafile_fs.group))  # number of conditions
N_fs = len(datafile_fs.values)  # conditions times participants
n_fs = datafile_fs.groupby('group').size()[0] # Participants in each condition

k_fm = len(pd.unique(datafile_fm.group))  # number of conditions
N_fm = len(datafile_fm.values)  # conditions times participants
n_fm = datafile_fm.groupby('group').size()[0] # Participants in each condition

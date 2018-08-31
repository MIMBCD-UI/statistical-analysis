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
sa_methods_dir = (pathAbsPath + '/statistical-analysis/methods/')

sys.path.append(sa_constants_dir)
sys.path.append(sa_methods_dir)

from listGroupStructures import *
from replacers import *

varReplacer_fs_intern = vecReplacer(lg_fs_sus_intern_arr, sus_questions)
varReplacer_fs_junior = vecReplacer(lg_fs_sus_junior_arr, sus_questions)
varReplacer_fs_middle = vecReplacer(lg_fs_sus_middle_arr, sus_questions)
varReplacer_fs_senior = vecReplacer(lg_fs_sus_senior_arr, sus_questions)

varReplacer_fs_intern_p = vecReplacePrinter(lg_fs_sus_intern_arr)
varReplacer_fs_junior_p = vecReplacePrinter(lg_fs_sus_junior_arr)
varReplacer_fs_middle_p = vecReplacePrinter(lg_fs_sus_middle_arr)
varReplacer_fs_senior_p = vecReplacePrinter(lg_fs_sus_senior_arr)

datafile_fs_vec = varReplacer_fs_intern + varReplacer_fs_junior + varReplacer_fs_middle + varReplacer_fs_senior

varReplacer_fm_intern = vecReplacer(lg_fm_sus_intern_arr, sus_questions)
varReplacer_fm_junior = vecReplacer(lg_fm_sus_junior_arr, sus_questions)
varReplacer_fm_middle = vecReplacer(lg_fm_sus_middle_arr, sus_questions)
varReplacer_fm_senior = vecReplacer(lg_fm_sus_senior_arr, sus_questions)

varReplacer_fm_intern_p = vecReplacePrinter(lg_fm_sus_intern_arr)
varReplacer_fm_junior_p = vecReplacePrinter(lg_fm_sus_junior_arr)
varReplacer_fm_middle_p = vecReplacePrinter(lg_fm_sus_middle_arr)
varReplacer_fm_senior_p = vecReplacePrinter(lg_fm_sus_senior_arr)

datafile_fm_vec = varReplacer_fm_intern + varReplacer_fm_junior + varReplacer_fm_middle + varReplacer_fm_senior

datafile_vec = datafile_fs_vec + datafile_fm_vec

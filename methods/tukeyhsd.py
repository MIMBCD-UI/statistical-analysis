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

from structures import *
from dataFileGroups import *
from messageVars import *

from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison

import math
import numpy as np
from scipy.misc import logsumexp
from scipy.stats import f_oneway

def computeTukeyModalities(d_data_fs, d_data_fm, vec):
  limit_t = 0.01
  limit_p = 0.10
  for i in range(len(vec)):
    actual = vec[i]
    ddfs_act = d_data_fs[actual]
    ddfm_act = d_data_fm[actual]
    dd_t, dd_p = f_oneway(ddfs_act, ddfm_act)
    print(m_t_t_001, d_data_fs[actual].name)
    print(m_t_t_002, d_data_fm[actual].name)
    print(m_t_t_003, actual)
    print(m_t_t_004, dd_t)
    print(m_t_t_005, dd_p)
    ddfs_std = np.std(ddfs_act, ddof=0)
    ddfm_std = np.std(ddfm_act, ddof=0)
    print(m_t_t_006, ddfs_std)
    print(m_t_t_007, ddfm_std)
    ddfs_mean = np.mean(ddfs_act)
    ddfm_mean = np.mean(ddfm_act)
    print(m_t_t_008, ddfs_mean)
    print(m_t_t_009, ddfm_mean)
    cond1 = dd_t < 0
    cond2 = dd_p < 0
    cond3 = dd_t < limit_t
    cond4 = dd_p > limit_p
    if(cond1 or cond2 or cond3 or cond4):
      mtnw = m_t_w
      mdf = m_degree_freedom
      print(m_marks_thsd)
      print(mtnw, ddfs_act, an, ddfm_act, mdf)
      print(m_marks_thsd)
    else:
      mc = MultiComparison(ddfs_act, ddfm_act)
      result = mc.tukeyhsd()
      print(m_t_main, ddfs_act, an, ddfm_act, result)
      print(mc_unique_group, mc.groupsunique)

def computeTukeyExperience(d_data, vec):
  limit = 0.05
  for i in range(len(vec)):
    for j in range(len(vec)):
      actVal = vec[i]
      nextVal = vec[j]
      dd_act = d_data[actVal]
      dd_nxt = d_data[nextVal]
      dd_t, dd_p = f_oneway(dd_act, dd_nxt)
      print("COMP----->", dd_t)
      print("COMP----->", dd_p)
      dd_act_std = np.std(dd_act, ddof=1)
      dd_nxt_std = np.std(dd_nxt, ddof=1)
      print("STD----->", dd_act_std)
      print("STD----->", dd_nxt_std)
      cond1 = dd_t < 0
      cond2 = dd_p < 0
      cond3 = dd_p > dd_t
      cond4 = dd_p > limit
      if(cond1 or cond2 or cond3 or cond4):
        mtnw = m_t_w
        mdf = m_degree_freedom
        print(m_marks_thsd)
        print(actVal)
        print(nextVal)
        print(mtnw, dd_act, an, dd_nxt, mdf)
        print(m_marks_thsd)
      else:
        mc = MultiComparison(dd_act, dd_nxt)
        result = mc.tukeyhsd()
        print(actVal)
        print(nextVal)
        print(m_t_main, dd_act, an, dd_nxt, result)
        print(mc_unique_group, mc.groupsunique)

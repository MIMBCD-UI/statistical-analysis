#!/usr/bin/env python

"""falses.py: Operations for  counting the number of
              False-Positives (FP) and False-Negatives (FN)
              among breast severeties."""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "ACADEMIC & COMMERCIAL"
__version__     = "2.0.0"
__status__      = "Production"
__copyright__   = "Copyright 2019, Instituto Superior Técnico (IST)"
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

saJoinPath = os.path.join(pathAbsPath, 'statistical-analysis')
sys.path.append(saJoinPath)
saAbsPath = os.path.abspath(saJoinPath)

saSrcJoinPath = os.path.join(saAbsPath, 'src')
sys.path.append(saSrcJoinPath)
saSrcAbsPath = os.path.abspath(saSrcJoinPath)

saSrcConsJoinPath = os.path.join(saSrcAbsPath, 'constants')
sys.path.append(saSrcConsJoinPath)
saSrcConsAbsPath = os.path.abspath(saSrcConsJoinPath)

saSrcVarsJoinPath = os.path.join(saSrcAbsPath, 'variables')
sys.path.append(saSrcVarsJoinPath)
saSrcVarsAbsPath = os.path.abspath(saSrcVarsJoinPath)

from dataFrames import *

# +++++++++++++++++ Current ++++++++++++++++++++ #

# Total number of samples
total_crrnt_sample = len(df035)

# Total number of each condition
total_crrnt_hgh_fn = len(df029)
total_crrnt_hgh_fp = len(df030)

total_crrnt_med_fn = len(df031)
total_crrnt_med_fp = len(df032)

total_crrnt_low_fn = len(df033)
total_crrnt_low_fp = len(df034)

# Ratio of each condition
ratio_crrnt_hgh_fn = total_crrnt_hgh_fn / total_crrnt_sample
ratio_crrnt_hgh_fp = total_crrnt_hgh_fp / total_crrnt_sample

ratio_crrnt_med_fn = total_crrnt_med_fn / total_crrnt_sample
ratio_crrnt_med_fp = total_crrnt_med_fp / total_crrnt_sample

ratio_crrnt_low_fn = total_crrnt_low_fn / total_crrnt_sample
ratio_crrnt_low_fp = total_crrnt_low_fp / total_crrnt_sample

# ++++++++++++++++++++++++++++++++++++++++++++++ #

# ++++++++++++++++ Physician +++++++++++++++++++ #

# Total number of samples
total_phy_sample = len(df042)

# Total number of each condition
total_phy_hgh_fn = len(df036)
total_phy_hgh_fp = len(df037)

total_phy_med_fn = len(df038)
total_phy_med_fp = len(df039)

total_phy_low_fn = len(df040)
total_phy_low_fp = len(df041)

# Ratio of each condition
ratio_phy_hgh_fn = total_phy_hgh_fn / total_phy_sample
ratio_phy_hgh_fp = total_phy_hgh_fp / total_phy_sample

ratio_phy_med_fn = total_phy_med_fn / total_phy_sample
ratio_phy_med_fp = total_phy_med_fp / total_phy_sample

ratio_phy_low_fn = total_phy_low_fn / total_phy_sample
ratio_phy_low_fp = total_phy_low_fp / total_phy_sample

# ++++++++++++++++++++++++++++++++++++++++++++++ #

# ==================== END File ==================== #
#!/usr/bin/env python

"""biradsCalcs.py: Calculations for the BI-RADS."""

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

sa_dir = os.path.join(pathAbsPath, 'statistical-analysis')
sys.path.append(sa_dir)
saAbsPath = os.path.abspath(sa_dir)

sa_src_dir = os.path.join(saAbsPath, 'src')
sys.path.append(sa_src_dir)
saSrcAbsPath = os.path.abspath(sa_src_dir)

sr_dir = os.path.join(pathAbsPath, 'sheet-reader')
sys.path.append(sr_dir)
srAbsPath = os.path.abspath(sr_dir)

sr_src_dir = os.path.join(srAbsPath, 'src')
sys.path.append(sr_src_dir)
srSrcAbsPath = os.path.abspath(sr_src_dir)

sa_techniques_dir = os.path.join(saSrcAbsPath, 'techniques')
sys.path.append(sa_techniques_dir)
saTechAbsPath = os.path.abspath(sa_techniques_dir)

sa_constants_dir = os.path.join(saSrcAbsPath, 'constants')
sys.path.append(sa_constants_dir)
saConsAbsPath = os.path.abspath(sa_constants_dir)

sa_methods_dir = os.path.join(saSrcAbsPath, 'methods')
sys.path.append(sa_methods_dir)
saMethAbsPath = os.path.abspath(sa_methods_dir)

src_dir = os.path.join(srSrcAbsPath, 'core')
sys.path.append(src_dir)
srcAbsPath = os.path.abspath(src_dir)

src_data_dir = os.path.join(srAbsPath, 'data')
sys.path.append(src_data_dir)
srcDataAbsPath = os.path.abspath(src_data_dir)

src_data_tmp_dir = os.path.join(srcDataAbsPath, 'temp')
sys.path.append(src_data_tmp_dir)
srcDataTmpAbsPath = os.path.abspath(src_data_tmp_dir)

from nasa import nasaColMean

import main_variables
import structures
import sheetReaders
import iterators

MV_N = main_variables.N
experience = structures.experience
nasatlx_columns = structures.nasatlx_columns
sus_columns = structures.sus_columns
sus_questions = structures.sus_questions
measures_columns = structures.measures_columns
birads_columns = structures.birads_columns
filterByColumn = structures.filterByColumn
figSizeX = structures.figSizeX
figSizeY = structures.figSizeY
datafileIteratorPerGroup = iterators.datafileIteratorPerGroup

import plotly.plotly as py
import plotly.graph_objs as go
from plotly import figure_factory as FF

import pandas as pd
import scipy
from scipy import stats

import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})

import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np

# ============================================== #
#                     UTA4                       #
# ============================================== #

main_sheet_dir = os.path.join(srcDataTmpAbsPath, 'main_sheet.csv')
sys.path.append(main_sheet_dir)
mainSheetAbsPath = os.path.abspath(main_sheet_dir)

fs_sheet_dir = os.path.join(srcDataTmpAbsPath, 'fs_sheet.csv')
sys.path.append(fs_sheet_dir)
fsSheetAbsPath = os.path.abspath(fs_sheet_dir)

fm_sheet_dir = os.path.join(srcDataTmpAbsPath, 'fm_sheet.csv')
sys.path.append(fm_sheet_dir)
fmSheetAbsPath = os.path.abspath(fm_sheet_dir)

datafile_fs = pd.read_csv(fsSheetAbsPath, delimiter=',')
datafile_fm = pd.read_csv(fmSheetAbsPath, delimiter=',')

# ============================================== #
# ============================================== #

# ============================================== #
#                     UTA7                       #
# ============================================== #

nasatlx_crrnt_dir = os.path.join(srcDataTmpAbsPath, 'nasatlx_crrnt.csv')
sys.path.append(nasatlx_crrnt_dir)
nasatlx_crrnt_abs_path = os.path.abspath(nasatlx_crrnt_dir)

nasatlx_assis_dir = os.path.join(srcDataTmpAbsPath, 'nasatlx_assis.csv')
sys.path.append(nasatlx_assis_dir)
nasatlx_assis_abs_path = os.path.abspath(nasatlx_assis_dir)

sus_crrnt_dir = os.path.join(srcDataTmpAbsPath, 'sus_crrnt.csv')
sys.path.append(sus_crrnt_dir)
sus_crrnt_abs_path = os.path.abspath(sus_crrnt_dir)

sus_assis_dir = os.path.join(srcDataTmpAbsPath, 'sus_assis.csv')
sys.path.append(sus_assis_dir)
sus_assis_abs_path = os.path.abspath(sus_assis_dir)

dots_assis_dir = os.path.join(srcDataTmpAbsPath, 'dots_assis.csv')
sys.path.append(dots_assis_dir)
dots_assis_abs_path = os.path.abspath(dots_assis_dir)

time_full_crrnt_dir = os.path.join(srcDataTmpAbsPath, 'time_full_crrnt.csv')
sys.path.append(time_full_crrnt_dir)
time_full_crrnt_abs_path = os.path.abspath(time_full_crrnt_dir)

time_full_assis_dir = os.path.join(srcDataTmpAbsPath, 'time_full_assis.csv')
sys.path.append(time_full_assis_dir)
time_full_assis_abs_path = os.path.abspath(time_full_assis_dir)

time_assis_dgns_dir = os.path.join(srcDataTmpAbsPath, 'time_assis_dgns.csv')
sys.path.append(time_assis_dgns_dir)
time_assis_dgns_abs_path = os.path.abspath(time_assis_dgns_dir)

time_assis_avtr_dir = os.path.join(srcDataTmpAbsPath, 'time_assis_avtr.csv')
sys.path.append(time_assis_avtr_dir)
time_assis_avtr_abs_path = os.path.abspath(time_assis_avtr_dir)

time_ext_all_dir = os.path.join(srcDataTmpAbsPath, 'time_ext_all.csv')
sys.path.append(time_ext_all_dir)
time_ext_all_abs_path = os.path.abspath(time_ext_all_dir)

time_ext_reg_dir = os.path.join(srcDataTmpAbsPath, 'time_ext_reg.csv')
sys.path.append(time_ext_reg_dir)
time_ext_reg_abs_path = os.path.abspath(time_ext_reg_dir)

noc_crrnt_dir = os.path.join(srcDataTmpAbsPath, 'noc_crrnt.csv')
sys.path.append(noc_crrnt_dir)
noc_crrnt_abs_path = os.path.abspath(noc_crrnt_dir)

noc_assis_dir = os.path.join(srcDataTmpAbsPath, 'noc_assis.csv')
sys.path.append(noc_assis_dir)
noc_assis_abs_path = os.path.abspath(noc_assis_dir)

noe_ce_crrnt_dir = os.path.join(srcDataTmpAbsPath, 'noe_ce_crrnt.csv')
sys.path.append(noe_ce_crrnt_dir)
noe_ce_crrnt_abs_path = os.path.abspath(noe_ce_crrnt_dir)

noe_ce_assis_dir = os.path.join(srcDataTmpAbsPath, 'noe_ce_assis.csv')
sys.path.append(noe_ce_assis_dir)
noe_ce_assis_abs_path = os.path.abspath(noe_ce_assis_dir)

noe_nce_crrnt_dir = os.path.join(srcDataTmpAbsPath, 'noe_nce_crrnt.csv')
sys.path.append(noe_nce_crrnt_dir)
noe_nce_crrnt_abs_path = os.path.abspath(noe_nce_crrnt_dir)

noe_nce_assis_dir = os.path.join(srcDataTmpAbsPath, 'noe_nce_assis.csv')
sys.path.append(noe_nce_assis_dir)
noe_nce_assis_abs_path = os.path.abspath(noe_nce_assis_dir)

birads_crrnt_dir = os.path.join(srcDataTmpAbsPath, 'birads_crrnt.csv')
sys.path.append(birads_crrnt_dir)
birads_crrnt_abs_path = os.path.abspath(birads_crrnt_dir)

birads_real_dir = os.path.join(srcDataTmpAbsPath, 'birads_real.csv')
sys.path.append(birads_real_dir)
birads_real_abs_path = os.path.abspath(birads_real_dir)

birads_phy_dir = os.path.join(srcDataTmpAbsPath, 'birads_phy.csv')
sys.path.append(birads_phy_dir)
birads_phy_abs_path = os.path.abspath(birads_phy_dir)

birads_assis_dir = os.path.join(srcDataTmpAbsPath, 'birads_assis.csv')
sys.path.append(birads_assis_dir)
birads_assis_abs_path = os.path.abspath(birads_assis_dir)

# birads_assis.csv
# birads_crrnt.csv
# birads_phy.csv
# birads_real.csv
# dots_assis.csv
# nasatlx_assis.csv
# nasatlx_crrnt.csv
# noc_assis.csv
# noc_crrnt.csv
# noe_ce_assis.csv
# noe_ce_crrnt.csv
# noe_nce_assis.csv
# noe_nce_crrnt.csv
# sus_assis.csv
# sus_crrnt.csv
# time_assis_avtr.csv
# time_assis_dgns.csv
# time_ext_all.csv
# time_ext_reg.csv
# time_full_assis.csv
# time_full_crrnt.csv

df_birads_assis = pd.read_csv(birads_assis_abs_path, delimiter=',')
df_birads_crrnt = pd.read_csv(birads_crrnt_abs_path, delimiter=',')
df_birads_phy = pd.read_csv(birads_phy_abs_path, delimiter=',')
df_birads_real = pd.read_csv(birads_real_abs_path, delimiter=',')
df_dots_assis = pd.read_csv(dots_assis_abs_path, delimiter=',')
df_nasatlx_assis = pd.read_csv(nasatlx_assis_abs_path, delimiter=',')
df_nasatlx_crrnt = pd.read_csv(nasatlx_crrnt_abs_path, delimiter=',')
#df_noc_assis = pd.read_csv(noc_assis_abs_path, delimiter=',')
#df_noc_crrnt = pd.read_csv(noc_crrnt_abs_path, delimiter=',')
#df_noe_ce_assis = pd.read_csv(noe_ce_assis_abs_path, delimiter=',')
#df_noe_ce_crrnt = pd.read_csv(noe_ce_crrnt_abs_path, delimiter=',')
#df_noe_nce_assis = pd.read_csv(noe_nce_assis_abs_path, delimiter=',')
#df_noe_nce_crrnt = pd.read_csv(noe_nce_crrnt_abs_path, delimiter=',')
df_sus_assis = pd.read_csv(sus_assis_abs_path, delimiter=',')
df_sus_crrnt = pd.read_csv(sus_crrnt_abs_path, delimiter=',')
#df_time_assis_avtr = pd.read_csv(time_assis_avtr_abs_path, delimiter=',')
#df_time_assis_dgns = pd.read_csv(time_assis_dgns_abs_path, delimiter=',')
#df_time_ext_all = pd.read_csv(time_ext_all_abs_path, delimiter=',')
#df_time_ext_reg = pd.read_csv(time_ext_reg_abs_path, delimiter=',')
df_time_full_assis = pd.read_csv(time_full_assis_abs_path, delimiter=',')
df_time_full_crrnt = pd.read_csv(time_full_crrnt_abs_path, delimiter=',')

# ============================================== #
# ============================================== #

# ==================== END File ==================== #
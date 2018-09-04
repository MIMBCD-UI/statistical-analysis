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

sa_methods_dir = (pathAbsPath + '/statistical-analysis/methods/')

sys.path.append(sa_methods_dir)

import scikit_posthocs as sp

from tukeyhsd import *

# ============================================== #
#                                                #
#                  MEANS & SD                    #
#                                                #
# ============================================== #

print(m_equal_thsd)

print(m_dfg_001, d_data_fs_sus_intern_list)
print(m_dfg_002, d_data_fs_sus_junior_list)
print(m_dfg_003, d_data_fs_sus_middle_list)
print(m_dfg_004, d_data_fs_sus_senior_list)

print(m_equal_thsd)

# ============================================== #
# ============================================== #
# ============================================== #

# ============================================== #
#                                                #
#                  TUCKEYS HSD                   #
#                                                #
# ============================================== #

# ============================================== #
#                Compute Methods                 #
# ============================================== #

computeTukeyModalities(d_data_fs_md, d_data_fm_md, experience)
computeTukeyModalities(d_data_fs_pd, d_data_fm_pd, experience)
computeTukeyModalities(d_data_fs_td, d_data_fm_td, experience)
computeTukeyModalities(d_data_fs_p, d_data_fm_p, experience)
computeTukeyModalities(d_data_fs_e, d_data_fm_e, experience)
computeTukeyModalities(d_data_fs_f, d_data_fm_f, experience)

# print(d_data_fs_sus_intern_arr)

# ddfssusi_mean, ddfssusi_std = computeDataFileGroupsMean(d_data_fs_sus_intern_arr)
# ddfssusj_mean, ddfssusj_std = computeDataFileGroupsMean(d_data_fs_sus_junior_arr)
# ddfssusm_mean, ddfssusm_std = computeDataFileGroupsMean(d_data_fs_sus_middle_arr)
# ddfssuss_mean, ddfssuss_std = computeDataFileGroupsMean(d_data_fs_sus_senior_arr)

# print("----->", ddfssusi_mean, ddfssusi_std)

# ctm_dd_t_md, ctm_dd_p_md = computeTukeyModalities(d_data_fs_md, d_data_fm_md, experience)
# ctm_dd_t_pd, ctm_dd_p_pd = computeTukeyModalities(d_data_fs_pd, d_data_fm_pd, experience)
# ctm_dd_t_td, ctm_dd_p_td = computeTukeyModalities(d_data_fs_td, d_data_fm_td, experience)
# ctm_dd_t_p, ctm_dd_p_p = computeTukeyModalities(d_data_fs_p, d_data_fm_p, experience)
# ctm_dd_t_e, ctm_dd_p_e = computeTukeyModalities(d_data_fs_e, d_data_fm_e, experience)
# ctm_dd_t_f, ctm_dd_p_f = computeTukeyModalities(d_data_fs_f, d_data_fm_f, experience)

# ctm_dd_t_sum = ctm_dd_t_md + ctm_dd_t_pd + ctm_dd_t_td + ctm_dd_t_p + ctm_dd_t_e + ctm_dd_t_f
# ctm_dd_t_mean = ctm_dd_t_sum / 6

# print(m_equal_thsd)

# print(m_t_hsd_001, ctm_dd_t_md)
# print(m_t_hsd_001, ctm_dd_t_pd)
# print(m_t_hsd_001, ctm_dd_t_td)
# print(m_t_hsd_001, ctm_dd_t_p)
# print(m_t_hsd_001, ctm_dd_t_e)
# print(m_t_hsd_001, ctm_dd_t_f)

# print(m_equal_thsd)

# print(m_equal_thsd)

# print(m_t_hsd_002, ctm_dd_p_md)
# print(m_t_hsd_002, ctm_dd_p_pd)
# print(m_t_hsd_002, ctm_dd_p_td)
# print(m_t_hsd_002, ctm_dd_p_p)
# print(m_t_hsd_002, ctm_dd_p_e)
# print(m_t_hsd_002, ctm_dd_p_f)

# print(m_equal_thsd)

computeTukeyModalities(d_data_fs_sus_01, d_data_fm_sus_01, experience)
computeTukeyModalities(d_data_fs_sus_02, d_data_fm_sus_02, experience)
computeTukeyModalities(d_data_fs_sus_03, d_data_fm_sus_03, experience)
computeTukeyModalities(d_data_fs_sus_04, d_data_fm_sus_04, experience)
computeTukeyModalities(d_data_fs_sus_05, d_data_fm_sus_05, experience)
computeTukeyModalities(d_data_fs_sus_06, d_data_fm_sus_06, experience)
computeTukeyModalities(d_data_fs_sus_07, d_data_fm_sus_07, experience)
computeTukeyModalities(d_data_fs_sus_08, d_data_fm_sus_08, experience)
computeTukeyModalities(d_data_fs_sus_09, d_data_fm_sus_09, experience)
computeTukeyModalities(d_data_fs_sus_10, d_data_fm_sus_10, experience)

# ctm_dd_t_sus_01, ctm_dd_p_sus_01 = computeTukeyModalities(d_data_fs_sus_01, d_data_fm_sus_01, experience)
# ctm_dd_t_sus_02, ctm_dd_p_sus_02 = computeTukeyModalities(d_data_fs_sus_02, d_data_fm_sus_02, experience)
# ctm_dd_t_sus_03, ctm_dd_p_sus_03 = computeTukeyModalities(d_data_fs_sus_03, d_data_fm_sus_03, experience)
# ctm_dd_t_sus_04, ctm_dd_p_sus_04 = computeTukeyModalities(d_data_fs_sus_04, d_data_fm_sus_04, experience)
# ctm_dd_t_sus_05, ctm_dd_p_sus_05 = computeTukeyModalities(d_data_fs_sus_05, d_data_fm_sus_05, experience)
# ctm_dd_t_sus_06, ctm_dd_p_sus_06 = computeTukeyModalities(d_data_fs_sus_06, d_data_fm_sus_06, experience)
# ctm_dd_t_sus_07, ctm_dd_p_sus_07 = computeTukeyModalities(d_data_fs_sus_07, d_data_fm_sus_07, experience)
# ctm_dd_t_sus_08, ctm_dd_p_sus_08 = computeTukeyModalities(d_data_fs_sus_08, d_data_fm_sus_08, experience)
# ctm_dd_t_sus_09, ctm_dd_p_sus_09 = computeTukeyModalities(d_data_fs_sus_09, d_data_fm_sus_09, experience)
# ctm_dd_t_sus_10, ctm_dd_p_sus_10 = computeTukeyModalities(d_data_fs_sus_10, d_data_fm_sus_10, experience)

# print(m_equal_thsd)

# print(m_t_hsd_001, ctm_dd_t_sus_01)
# print(m_t_hsd_001, ctm_dd_t_sus_02)
# print(m_t_hsd_001, ctm_dd_t_sus_03)
# print(m_t_hsd_001, ctm_dd_t_sus_04)
# print(m_t_hsd_001, ctm_dd_t_sus_05)
# print(m_t_hsd_001, ctm_dd_t_sus_06)
# print(m_t_hsd_001, ctm_dd_t_sus_07)
# print(m_t_hsd_001, ctm_dd_t_sus_08)
# print(m_t_hsd_001, ctm_dd_t_sus_09)
# print(m_t_hsd_001, ctm_dd_t_sus_10)

# print(m_equal_thsd)

# print(m_equal_thsd)

# print(m_t_hsd_002, ctm_dd_p_sus_01)
# print(m_t_hsd_002, ctm_dd_p_sus_02)
# print(m_t_hsd_002, ctm_dd_p_sus_03)
# print(m_t_hsd_002, ctm_dd_p_sus_04)
# print(m_t_hsd_002, ctm_dd_p_sus_05)
# print(m_t_hsd_002, ctm_dd_p_sus_06)
# print(m_t_hsd_002, ctm_dd_p_sus_07)
# print(m_t_hsd_002, ctm_dd_p_sus_08)
# print(m_t_hsd_002, ctm_dd_p_sus_09)
# print(m_t_hsd_002, ctm_dd_p_sus_10)

# print(m_equal_thsd)

# computeTukeyModalities(d_data_fs_time_94662, d_data_fm_time_94662, experience)
# computeTukeyModalities(d_data_fs_time_607376, d_data_fm_time_607376, experience)
# computeTukeyModalities(d_data_fs_time_737037, d_data_fm_time_737037, experience)
# computeTukeyModalities(d_data_fs_time_total, d_data_fm_time_total, experience)

# computeTukeyModalities(d_data_fs_clicks_94662, d_data_fm_clicks_94662, experience)
# computeTukeyModalities(d_data_fs_clicks_607376, d_data_fm_clicks_607376, experience)
# computeTukeyModalities(d_data_fs_clicks_737037, d_data_fm_clicks_737037, experience)
# computeTukeyModalities(d_data_fs_clicks_total, d_data_fm_clicks_total, experience)

# computeTukeyModalities(d_data_fs_errors_94662, d_data_fm_errors_94662, experience)
# computeTukeyModalities(d_data_fs_errors_607376, d_data_fm_errors_607376, experience)
# computeTukeyModalities(d_data_fs_errors_737037, d_data_fm_errors_737037, experience)
# computeTukeyModalities(d_data_fs_errors_total, d_data_fm_errors_total, experience)

# computeTukeyModalities(d_data_fs_birads_94662, d_data_fm_birads_94662, experience)
# computeTukeyModalities(d_data_fs_birads_607376, d_data_fm_birads_607376, experience)
# computeTukeyModalities(d_data_fs_birads_737037, d_data_fm_birads_737037, experience)

# computeTukeyExperience(d_data_fs_md, experience)
# computeTukeyExperience(d_data_fs_pd, experience)
# computeTukeyExperience(d_data_fs_td, experience)
# computeTukeyExperience(d_data_fs_p, experience)
# computeTukeyExperience(d_data_fs_e, experience)
# computeTukeyExperience(d_data_fs_f, experience)

# computeTukeyExperience(d_data_fm_md, experience)
# computeTukeyExperience(d_data_fm_pd, experience)
# computeTukeyExperience(d_data_fm_td, experience)
# computeTukeyExperience(d_data_fm_p, experience)
# computeTukeyExperience(d_data_fm_e, experience)
# computeTukeyExperience(d_data_fm_f, experience)

# computeTukeyExperience(d_data_fs_sus_01, experience)
# computeTukeyExperience(d_data_fs_sus_02, experience)
# computeTukeyExperience(d_data_fs_sus_03, experience)
# computeTukeyExperience(d_data_fs_sus_04, experience)
# computeTukeyExperience(d_data_fs_sus_05, experience)
# computeTukeyExperience(d_data_fs_sus_06, experience)
# computeTukeyExperience(d_data_fs_sus_07, experience)
# computeTukeyExperience(d_data_fs_sus_08, experience)
# computeTukeyExperience(d_data_fs_sus_09, experience)
# computeTukeyExperience(d_data_fs_sus_10, experience)

# computeTukeyExperience(d_data_fm_sus_01, experience)
# computeTukeyExperience(d_data_fm_sus_02, experience)
# computeTukeyExperience(d_data_fm_sus_03, experience)
# computeTukeyExperience(d_data_fm_sus_04, experience)
# computeTukeyExperience(d_data_fm_sus_05, experience)
# computeTukeyExperience(d_data_fm_sus_06, experience)
# computeTukeyExperience(d_data_fm_sus_07, experience)
# computeTukeyExperience(d_data_fm_sus_08, experience)
# computeTukeyExperience(d_data_fm_sus_09, experience)
# computeTukeyExperience(d_data_fm_sus_10, experience)

# ============================================== #

# ============================================== #
# ============================================== #
# ============================================== #

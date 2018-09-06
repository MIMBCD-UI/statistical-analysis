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

from meanGroups import *
from tukeyhsd import *

# ============================================== #
#                                                #
#                  MEANS & SD                    #
#                                                #
# ============================================== #

# ddfssusim => d_data_fs_sus_interns_means
# ddfssusjm => d_data_fs_sus_junior_means
# ddfssusmm => d_data_fs_sus_middle_means
# ddfssussm => d_data_fs_sus_senior_means

ddfssusi_mean, ddfssusi_std = flagDataFileGroupsMean(d_data_fs_sus_intern_list, flag01)
ddfssusj_mean, ddfssusj_std = flagDataFileGroupsMean(d_data_fs_sus_junior_list, flag01)
ddfssusm_mean, ddfssusm_std = flagDataFileGroupsMean(d_data_fs_sus_middle_list, flag01)
ddfssuss_mean, ddfssuss_std = flagDataFileGroupsMean(d_data_fs_sus_senior_list, flag01)

ddfmsusi_mean, ddfmsusi_std = flagDataFileGroupsMean(d_data_fm_sus_intern_list, flag01)
ddfmsusj_mean, ddfmsusj_std = flagDataFileGroupsMean(d_data_fm_sus_junior_list, flag01)
ddfmsusm_mean, ddfmsusm_std = flagDataFileGroupsMean(d_data_fm_sus_middle_list, flag01)
ddfmsuss_mean, ddfmsuss_std = flagDataFileGroupsMean(d_data_fm_sus_senior_list, flag01)

ddfsnasatlxi_mean, ddfsnasatlxi_std = flagDataFileGroupsMean(d_data_fs_nasatlx_intern_list, flag02)
ddfsnasatlxj_mean, ddfsnasatlxj_std = flagDataFileGroupsMean(d_data_fs_nasatlx_junior_list, flag02)
ddfsnasatlxm_mean, ddfsnasatlxm_std = flagDataFileGroupsMean(d_data_fs_nasatlx_middle_list, flag02)
ddfsnasatlxs_mean, ddfsnasatlxs_std = flagDataFileGroupsMean(d_data_fs_nasatlx_senior_list, flag02)

ddfmnasatlxi_mean, ddfmnasatlxi_std = flagDataFileGroupsMean(d_data_fm_nasatlx_intern_list, flag02)
ddfmnasatlxj_mean, ddfmnasatlxj_std = flagDataFileGroupsMean(d_data_fm_nasatlx_junior_list, flag02)
ddfmnasatlxm_mean, ddfmnasatlxm_std = flagDataFileGroupsMean(d_data_fm_nasatlx_middle_list, flag02)
ddfmnasatlxs_mean, ddfmnasatlxs_std = flagDataFileGroupsMean(d_data_fm_nasatlx_senior_list, flag02)

ddfstimei_mean, ddfstimei_std = flagDataFileGroupsMean(d_data_fs_time_intern_list, flag03)
ddfstimej_mean, ddfstimej_std = flagDataFileGroupsMean(d_data_fs_time_junior_list, flag03)
ddfstimem_mean, ddfstimem_std = flagDataFileGroupsMean(d_data_fs_time_middle_list, flag03)
ddfstimes_mean, ddfstimes_std = flagDataFileGroupsMean(d_data_fs_time_senior_list, flag03)

ddfmtimei_mean, ddfmtimei_std = flagDataFileGroupsMean(d_data_fm_time_intern_list, flag03)
ddfmtimej_mean, ddfmtimej_std = flagDataFileGroupsMean(d_data_fm_time_junior_list, flag03)
ddfmtimem_mean, ddfmtimem_std = flagDataFileGroupsMean(d_data_fm_time_middle_list, flag03)
ddfmtimes_mean, ddfmtimes_std = flagDataFileGroupsMean(d_data_fm_time_senior_list, flag03)

ddfsclicksi_mean, ddfsclicksi_std = flagDataFileGroupsMean(d_data_fs_clicks_intern_list, flag04)
ddfsclicksj_mean, ddfsclicksj_std = flagDataFileGroupsMean(d_data_fs_clicks_junior_list, flag04)
ddfsclicksm_mean, ddfsclicksm_std = flagDataFileGroupsMean(d_data_fs_clicks_middle_list, flag04)
ddfsclickss_mean, ddfsclickss_std = flagDataFileGroupsMean(d_data_fs_clicks_senior_list, flag04)

ddfmclicksi_mean, ddfmclicksi_std = flagDataFileGroupsMean(d_data_fm_clicks_intern_list, flag04)
ddfmclicksj_mean, ddfmclicksj_std = flagDataFileGroupsMean(d_data_fm_clicks_junior_list, flag04)
ddfmclicksm_mean, ddfmclicksm_std = flagDataFileGroupsMean(d_data_fm_clicks_middle_list, flag04)
ddfmclickss_mean, ddfmclickss_std = flagDataFileGroupsMean(d_data_fm_clicks_senior_list, flag04)

ddfserrorsi_mean, ddfserrorsi_std = flagDataFileGroupsMean(d_data_fs_errors_intern_list, flag05)
ddfserrorsj_mean, ddfserrorsj_std = flagDataFileGroupsMean(d_data_fs_errors_junior_list, flag05)
ddfserrorsm_mean, ddfserrorsm_std = flagDataFileGroupsMean(d_data_fs_errors_middle_list, flag05)
ddfserrorss_mean, ddfserrorss_std = flagDataFileGroupsMean(d_data_fs_errors_senior_list, flag05)

ddfmerrorsi_mean, ddfmerrorsi_std = flagDataFileGroupsMean(d_data_fm_errors_intern_list, flag05)
ddfmerrorsj_mean, ddfmerrorsj_std = flagDataFileGroupsMean(d_data_fm_errors_junior_list, flag05)
ddfmerrorsm_mean, ddfmerrorsm_std = flagDataFileGroupsMean(d_data_fm_errors_middle_list, flag05)
ddfmerrorss_mean, ddfmerrorss_std = flagDataFileGroupsMean(d_data_fm_errors_senior_list, flag05)

ddfsbiradsi_mean, ddfsbiradsi_std = flagDataFileGroupsMean(d_data_fs_birads_intern_list, flag06)
ddfsbiradsj_mean, ddfsbiradsj_std = flagDataFileGroupsMean(d_data_fs_birads_junior_list, flag06)
ddfsbiradsm_mean, ddfsbiradsm_std = flagDataFileGroupsMean(d_data_fs_birads_middle_list, flag06)
ddfsbiradss_mean, ddfsbiradss_std = flagDataFileGroupsMean(d_data_fs_birads_senior_list, flag06)

ddfmbiradsi_mean, ddfmbiradsi_std = flagDataFileGroupsMean(d_data_fm_birads_intern_list, flag06)
ddfmbiradsj_mean, ddfmbiradsj_std = flagDataFileGroupsMean(d_data_fm_birads_junior_list, flag06)
ddfmbiradsm_mean, ddfmbiradsm_std = flagDataFileGroupsMean(d_data_fm_birads_middle_list, flag06)
ddfmbiradss_mean, ddfmbiradss_std = flagDataFileGroupsMean(d_data_fm_birads_senior_list, flag06)

print(m_equal_thsd)

print(m_dfg_001, ddfssusi_mean)
print(m_dfg_002, ddfssusj_mean)
print(m_dfg_003, ddfssusm_mean)
print(m_dfg_004, ddfssuss_mean)

print(m_dfg_005, ddfmsusi_mean)
print(m_dfg_006, ddfmsusj_mean)
print(m_dfg_007, ddfmsusm_mean)
print(m_dfg_008, ddfmsuss_mean)

print(m_dfg_009, ddfssusi_std)
print(m_dfg_010, ddfssusj_std)
print(m_dfg_011, ddfssusm_std)
print(m_dfg_012, ddfssuss_std)

print(m_dfg_013, ddfmsusi_std)
print(m_dfg_014, ddfmsusj_std)
print(m_dfg_015, ddfmsusm_std)
print(m_dfg_016, ddfmsuss_std)

print(m_equal_thsd)

print(m_dfg_017, ddfsnasatlxi_mean)
print(m_dfg_018, ddfsnasatlxj_mean)
print(m_dfg_019, ddfsnasatlxm_mean)
print(m_dfg_020, ddfsnasatlxs_mean)

print(m_dfg_021, ddfmnasatlxi_mean)
print(m_dfg_022, ddfmnasatlxj_mean)
print(m_dfg_023, ddfmnasatlxm_mean)
print(m_dfg_024, ddfmnasatlxs_mean)

print(m_dfg_025, ddfsnasatlxi_std)
print(m_dfg_026, ddfsnasatlxj_std)
print(m_dfg_027, ddfsnasatlxm_std)
print(m_dfg_028, ddfsnasatlxs_std)

print(m_dfg_029, ddfmnasatlxi_std)
print(m_dfg_030, ddfmnasatlxj_std)
print(m_dfg_031, ddfmnasatlxm_std)
print(m_dfg_032, ddfmnasatlxs_std)

print(m_equal_thsd)

print(m_dfg_033, ddfstimei_mean)
print(m_dfg_034, ddfstimej_mean)
print(m_dfg_035, ddfstimem_mean)
print(m_dfg_036, ddfstimes_mean)

print(m_dfg_037, ddfmtimei_mean)
print(m_dfg_038, ddfmtimej_mean)
print(m_dfg_039, ddfmtimem_mean)
print(m_dfg_040, ddfmtimes_mean)

print(m_dfg_041, ddfstimei_std)
print(m_dfg_042, ddfstimej_std)
print(m_dfg_043, ddfstimem_std)
print(m_dfg_044, ddfstimes_std)

print(m_dfg_045, ddfmtimei_std)
print(m_dfg_046, ddfmtimej_std)
print(m_dfg_047, ddfmtimem_std)
print(m_dfg_048, ddfmtimes_std)

print(m_equal_thsd)

print(m_dfg_049, ddfsclicksi_mean)
print(m_dfg_050, ddfsclicksj_mean)
print(m_dfg_051, ddfsclicksm_mean)
print(m_dfg_052, ddfsclickss_mean)

print(m_dfg_053, ddfmclicksi_mean)
print(m_dfg_054, ddfmclicksj_mean)
print(m_dfg_055, ddfmclicksm_mean)
print(m_dfg_056, ddfmclickss_mean)

print(m_dfg_057, ddfsclicksi_std)
print(m_dfg_058, ddfsclicksj_std)
print(m_dfg_059, ddfsclicksm_std)
print(m_dfg_060, ddfsclickss_std)

print(m_dfg_061, ddfmclicksi_std)
print(m_dfg_062, ddfmclicksj_std)
print(m_dfg_063, ddfmclicksm_std)
print(m_dfg_064, ddfmclickss_std)

print(m_equal_thsd)

print(m_dfg_065, ddfserrorsi_mean)
print(m_dfg_066, ddfserrorsj_mean)
print(m_dfg_067, ddfserrorsm_mean)
print(m_dfg_068, ddfserrorss_mean)

print(m_dfg_069, ddfmerrorsi_mean)
print(m_dfg_070, ddfmerrorsj_mean)
print(m_dfg_071, ddfmerrorsm_mean)
print(m_dfg_072, ddfmerrorss_mean)

print(m_dfg_073, ddfserrorsi_std)
print(m_dfg_074, ddfserrorsj_std)
print(m_dfg_075, ddfserrorsm_std)
print(m_dfg_076, ddfserrorss_std)

print(m_dfg_077, ddfmerrorsi_std)
print(m_dfg_078, ddfmerrorsj_std)
print(m_dfg_079, ddfmerrorsm_std)
print(m_dfg_080, ddfmerrorss_std)

print(m_equal_thsd)

print(m_dfg_081, ddfsbiradsi_mean)
print(m_dfg_082, ddfsbiradsj_mean)
print(m_dfg_083, ddfsbiradsm_mean)
print(m_dfg_084, ddfsbiradss_mean)

print(m_dfg_085, ddfmbiradsi_mean)
print(m_dfg_086, ddfmbiradsj_mean)
print(m_dfg_087, ddfmbiradsm_mean)
print(m_dfg_088, ddfmbiradss_mean)

print(m_dfg_089, ddfsbiradsi_std)
print(m_dfg_090, ddfsbiradsj_std)
print(m_dfg_091, ddfsbiradsm_std)
print(m_dfg_092, ddfsbiradss_std)

print(m_dfg_093, ddfmbiradsi_std)
print(m_dfg_094, ddfmbiradsj_std)
print(m_dfg_095, ddfmbiradsm_std)
print(m_dfg_096, ddfmbiradss_std)

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

# =================== NASA-TLX ================= #

computeTukeyModalities(d_data_fs_md, d_data_fm_md, experience)
computeTukeyModalities(d_data_fs_pd, d_data_fm_pd, experience)
computeTukeyModalities(d_data_fs_td, d_data_fm_td, experience)
computeTukeyModalities(d_data_fs_p, d_data_fm_p, experience)
computeTukeyModalities(d_data_fs_e, d_data_fm_e, experience)
computeTukeyModalities(d_data_fs_f, d_data_fm_f, experience)

# ====================== SUS =================== #

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

# ============================================== #

# ============================================== #
# ============================================== #
# ============================================== #

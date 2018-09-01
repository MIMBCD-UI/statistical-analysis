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

# ============================================== #
#                    Phrases                     #
# ============================================== #

spc = " "
dpt = ":"
an = "and"

p001 = "Verification of the Mean for"
p002 = "Compute Mean for"
p003 = "Compute Standard Deviation (SD) for"

sm = "(SM)"
mm = "(MM)"

md = "MD"
pd = "PD"
td = "TD"
pe = "PE"
ef = "EF"
fr = "FR"

sus01 = "SUS01"
sus02 = "SUS02"
sus03 = "SUS03"
sus04 = "SUS04"
sus05 = "SUS05"
sus06 = "SUS06"
sus06 = "SUS07"
sus08 = "SUS08"
sus09 = "SUS09"
sus10 = "SUS10"

time001 = "TIME__94662"
time002 = "TIME_607376"
time003 = "TIME_737037"
time004 = "TIME__TOTAL"

clicks001 = "CLICKS__94662"
clicks002 = "CLICKS_607376"
clicks003 = "CLICKS_737037"
clicks004 = "CLICKS__TOTAL"

errors001 = "ERRORS__94662"
errors002 = "ERRORS_607376"
errors003 = "ERRORS_737037"
errors004 = "ERRORS__TOTAL"

birads001 = "BIRADS__94662"
birads002 = "BIRADS_607376"
birads003 = "BIRADS_737037"

# ============================================== #

# ============================================== #
#               Mean Verification                #
# ============================================== #

message_mean_ver_s_001 = p001 + spc + md + spc + sm + "\n"
message_mean_ver_s_002 = p001 + spc + pd + spc + sm + "\n"
message_mean_ver_s_003 = p001 + spc + td + spc + sm + "\n"
message_mean_ver_s_004 = p001 + spc + pe + spc + sm + "\n"
message_mean_ver_s_005 = p001 + spc + ef + spc + sm + "\n"
message_mean_ver_s_006 = p001 + spc + fr + spc + sm + "\n"

message_mean_ver_s_007 = p001 + spc + md + spc + mm + "\n"
message_mean_ver_s_008 = p001 + spc + pd + spc + mm + "\n"
message_mean_ver_s_009 = p001 + spc + td + spc + mm + "\n"
message_mean_ver_s_010 = p001 + spc + pe + spc + mm + "\n"
message_mean_ver_s_011 = p001 + spc + ef + spc + mm + "\n"
message_mean_ver_s_012 = p001 + spc + fr + spc + mm + "\n"

message_mean_ver_s_013 = p001 + spc + sus01 + spc + sm + "\n"
message_mean_ver_s_014 = p001 + spc + sus02 + spc + sm + "\n"
message_mean_ver_s_015 = p001 + spc + sus03 + spc + sm + "\n"
message_mean_ver_s_016 = p001 + spc + sus04 + spc + sm + "\n"
message_mean_ver_s_017 = p001 + spc + sus05 + spc + sm + "\n"
message_mean_ver_s_018 = p001 + spc + sus06 + spc + sm + "\n"
message_mean_ver_s_019 = p001 + spc + sus06 + spc + sm + "\n"
message_mean_ver_s_020 = p001 + spc + sus08 + spc + sm + "\n"
message_mean_ver_s_021 = p001 + spc + sus09 + spc + sm + "\n"
message_mean_ver_s_022 = p001 + spc + sus10 + spc + sm + "\n"

message_mean_ver_s_023 = p001 + spc + sus01 + spc + mm + "\n"
message_mean_ver_s_024 = p001 + spc + sus02 + spc + mm + "\n"
message_mean_ver_s_025 = p001 + spc + sus03 + spc + mm + "\n"
message_mean_ver_s_026 = p001 + spc + sus04 + spc + mm + "\n"
message_mean_ver_s_027 = p001 + spc + sus05 + spc + mm + "\n"
message_mean_ver_s_028 = p001 + spc + sus06 + spc + mm + "\n"
message_mean_ver_s_029 = p001 + spc + sus06 + spc + mm + "\n"
message_mean_ver_s_030 = p001 + spc + sus08 + spc + mm + "\n"
message_mean_ver_s_031 = p001 + spc + sus09 + spc + mm + "\n"
message_mean_ver_s_032 = p001 + spc + sus10 + spc + mm + "\n"

message_mean_ver_s_033 = p001 + spc + time001 + spc + sm + "\n"
message_mean_ver_s_034 = p001 + spc + time002 + spc + sm + "\n"
message_mean_ver_s_035 = p001 + spc + time003 + spc + sm + "\n"
message_mean_ver_s_036 = p001 + spc + time004 + spc + sm + "\n"

message_mean_ver_s_037 = p001 + spc + clicks001 + spc + sm + "\n"
message_mean_ver_s_038 = p001 + spc + clicks002 + spc + sm + "\n"
message_mean_ver_s_039 = p001 + spc + clicks003 + spc + sm + "\n"
message_mean_ver_s_040 = p001 + spc + clicks004 + spc + sm + "\n"

message_mean_ver_s_041 = p001 + spc + errors001 + spc + sm + "\n"
message_mean_ver_s_042 = p001 + spc + errors002 + spc + sm + "\n"
message_mean_ver_s_043 = p001 + spc + errors003 + spc + sm + "\n"
message_mean_ver_s_044 = p001 + spc + errors004 + spc + sm + "\n"

message_mean_ver_s_045 = p001 + spc + birads001 + spc + sm + "\n"
message_mean_ver_s_046 = p001 + spc + birads002 + spc + sm + "\n"
message_mean_ver_s_047 = p001 + spc + birads003 + spc + sm + "\n"

message_mean_ver_s_048 = p001 + spc + time001 + spc + mm + "\n"
message_mean_ver_s_049 = p001 + spc + time002 + spc + mm + "\n"
message_mean_ver_s_050 = p001 + spc + time003 + spc + mm + "\n"
message_mean_ver_s_051 = p001 + spc + time004 + spc + mm + "\n"

message_mean_ver_s_052 = p001 + spc + clicks001 + spc + mm + "\n"
message_mean_ver_s_053 = p001 + spc + clicks002 + spc + mm + "\n"
message_mean_ver_s_054 = p001 + spc + clicks003 + spc + mm + "\n"
message_mean_ver_s_055 = p001 + spc + clicks004 + spc + mm + "\n"

message_mean_ver_s_056 = p001 + spc + errors001 + spc + mm + "\n"
message_mean_ver_s_057 = p001 + spc + errors002 + spc + mm + "\n"
message_mean_ver_s_058 = p001 + spc + errors003 + spc + mm + "\n"
message_mean_ver_s_059 = p001 + spc + errors004 + spc + mm + "\n"

message_mean_ver_s_060 = p001 + spc + birads001 + spc + mm + "\n"
message_mean_ver_s_061 = p001 + spc + birads002 + spc + mm + "\n"
message_mean_ver_s_062 = p001 + spc + birads003 + spc + mm + "\n"

# ============================================== #

# ============================================== #
#           Compute Standard Deviation           #
# ============================================== #

message_001 = p002 + spc + md + spc + sm + "\n"
message_002 = p002 + spc + pd + spc + sm + "\n"
message_003 = p002 + spc + td + spc + sm + "\n"
message_004 = p002 + spc + pe + spc + sm + "\n"
message_005 = p002 + spc + ef + spc + sm + "\n"
message_006 = p002 + spc + fr + spc + sm + "\n"

message_007 = p002 + spc + md + spc + mm + "\n"
message_008 = p002 + spc + pd + spc + mm + "\n"
message_009 = p002 + spc + td + spc + mm + "\n"
message_010 = p002 + spc + pe + spc + mm + "\n"
message_011 = p002 + spc + ef + spc + mm + "\n"
message_012 = p002 + spc + fr + spc + mm + "\n"

message_013 = p002 + spc + sus01 + spc + sm + "\n"
message_014 = p002 + spc + sus02 + spc + sm + "\n"
message_015 = p002 + spc + sus03 + spc + sm + "\n"
message_016 = p002 + spc + sus04 + spc + sm + "\n"
message_017 = p002 + spc + sus05 + spc + sm + "\n"
message_018 = p002 + spc + sus06 + spc + sm + "\n"
message_019 = p002 + spc + sus06 + spc + sm + "\n"
message_020 = p002 + spc + sus08 + spc + sm + "\n"
message_021 = p002 + spc + sus09 + spc + sm + "\n"
message_022 = p002 + spc + sus10 + spc + sm + "\n"

message_023 = p002 + spc + sus01 + spc + mm + "\n"
message_024 = p002 + spc + sus02 + spc + mm + "\n"
message_025 = p002 + spc + sus03 + spc + mm + "\n"
message_026 = p002 + spc + sus04 + spc + mm + "\n"
message_027 = p002 + spc + sus05 + spc + mm + "\n"
message_028 = p002 + spc + sus06 + spc + mm + "\n"
message_029 = p002 + spc + sus06 + spc + mm + "\n"
message_030 = p002 + spc + sus08 + spc + mm + "\n"
message_031 = p002 + spc + sus09 + spc + mm + "\n"
message_032 = p002 + spc + sus10 + spc + mm + "\n"

message_033 = p002 + spc + time001 + spc + sm + "\n"
message_034 = p002 + spc + time002 + spc + sm + "\n"
message_035 = p002 + spc + time003 + spc + sm + "\n"
message_036 = p002 + spc + time004 + spc + sm + "\n"

message_037 = p002 + spc + clicks001 + spc + sm + "\n"
message_038 = p002 + spc + clicks002 + spc + sm + "\n"
message_039 = p002 + spc + clicks003 + spc + sm + "\n"
message_040 = p002 + spc + clicks004 + spc + sm + "\n"

message_041 = p002 + spc + errors001 + spc + sm + "\n"
message_042 = p002 + spc + errors002 + spc + sm + "\n"
message_043 = p002 + spc + errors003 + spc + sm + "\n"
message_044 = p002 + spc + errors004 + spc + sm + "\n"

message_045 = p002 + spc + birads001 + spc + sm + "\n"
message_046 = p002 + spc + birads002 + spc + sm + "\n"
message_047 = p002 + spc + birads003 + spc + sm + "\n"

message_048 = p002 + spc + time001 + spc + mm + "\n"
message_049 = p002 + spc + time002 + spc + mm + "\n"
message_050 = p002 + spc + time003 + spc + mm + "\n"
message_051 = p002 + spc + time004 + spc + mm + "\n"

message_052 = p002 + spc + clicks001 + spc + mm + "\n"
message_053 = p002 + spc + clicks002 + spc + mm + "\n"
message_054 = p002 + spc + clicks003 + spc + mm + "\n"
message_055 = p002 + spc + clicks004 + spc + mm + "\n"

message_056 = p002 + spc + errors001 + spc + mm + "\n"
message_057 = p002 + spc + errors002 + spc + mm + "\n"
message_058 = p002 + spc + errors003 + spc + mm + "\n"
message_059 = p002 + spc + errors004 + spc + mm + "\n"

message_060 = p002 + spc + birads001 + spc + mm + "\n"
message_061 = p002 + spc + birads002 + spc + mm + "\n"
message_062 = p002 + spc + birads003 + spc + mm + "\n"

# ============================================== #

# ============================================== #
#                Compute Variance                #
# ============================================== #

message_stdS_001 = p003 + spc + md + spc + sm + "\n"
message_stdS_002 = p003 + spc + pd + spc + sm + "\n"
message_stdS_003 = p003 + spc + td + spc + sm + "\n"
message_stdS_004 = p003 + spc + pe + spc + sm + "\n"
message_stdS_005 = p003 + spc + ef + spc + sm + "\n"
message_stdS_006 = p003 + spc + fr + spc + sm + "\n"

message_stdS_007 = p003 + spc + md + spc + mm + "\n"
message_stdS_008 = p003 + spc + pd + spc + mm + "\n"
message_stdS_009 = p003 + spc + td + spc + mm + "\n"
message_stdS_010 = p003 + spc + pe + spc + mm + "\n"
message_stdS_011 = p003 + spc + ef + spc + mm + "\n"
message_stdS_012 = p003 + spc + fr + spc + mm + "\n"

message_stdS_013 = p003 + spc + sus01 + spc + sm + "\n"
message_stdS_014 = p003 + spc + sus02 + spc + sm + "\n"
message_stdS_015 = p003 + spc + sus03 + spc + sm + "\n"
message_stdS_016 = p003 + spc + sus04 + spc + sm + "\n"
message_stdS_017 = p003 + spc + sus05 + spc + sm + "\n"
message_stdS_018 = p003 + spc + sus06 + spc + sm + "\n"
message_stdS_019 = p003 + spc + sus06 + spc + sm + "\n"
message_stdS_020 = p003 + spc + sus08 + spc + sm + "\n"
message_stdS_021 = p003 + spc + sus09 + spc + sm + "\n"
message_stdS_022 = p003 + spc + sus10 + spc + sm + "\n"

message_stdS_023 = p003 + spc + sus01 + spc + mm + "\n"
message_stdS_024 = p003 + spc + sus02 + spc + mm + "\n"
message_stdS_025 = p003 + spc + sus03 + spc + mm + "\n"
message_stdS_026 = p003 + spc + sus04 + spc + mm + "\n"
message_stdS_027 = p003 + spc + sus05 + spc + mm + "\n"
message_stdS_028 = p003 + spc + sus06 + spc + mm + "\n"
message_stdS_029 = p003 + spc + sus06 + spc + mm + "\n"
message_stdS_030 = p003 + spc + sus08 + spc + mm + "\n"
message_stdS_031 = p003 + spc + sus09 + spc + mm + "\n"
message_stdS_032 = p003 + spc + sus10 + spc + mm + "\n"

message_stdS_033 = p003 + spc + time001 + spc + sm + "\n"
message_stdS_034 = p003 + spc + time002 + spc + sm + "\n"
message_stdS_035 = p003 + spc + time003 + spc + sm + "\n"
message_stdS_036 = p003 + spc + time004 + spc + sm + "\n"

message_stdS_037 = p003 + spc + clicks001 + spc + sm + "\n"
message_stdS_038 = p003 + spc + clicks002 + spc + sm + "\n"
message_stdS_039 = p003 + spc + clicks003 + spc + sm + "\n"
message_stdS_040 = p003 + spc + clicks004 + spc + sm + "\n"

message_stdS_041 = p003 + spc + errors001 + spc + sm + "\n"
message_stdS_042 = p003 + spc + errors002 + spc + sm + "\n"
message_stdS_043 = p003 + spc + errors003 + spc + sm + "\n"
message_stdS_044 = p003 + spc + errors004 + spc + sm + "\n"

message_stdS_045 = p003 + spc + birads001 + spc + sm + "\n"
message_stdS_046 = p003 + spc + birads002 + spc + sm + "\n"
message_stdS_047 = p003 + spc + birads003 + spc + sm + "\n"

message_stdS_048 = p003 + spc + time001 + spc + mm + "\n"
message_stdS_049 = p003 + spc + time002 + spc + mm + "\n"
message_stdS_050 = p003 + spc + time003 + spc + mm + "\n"
message_stdS_051 = p003 + spc + time004 + spc + mm + "\n"

message_stdS_052 = p003 + spc + clicks001 + spc + mm + "\n"
message_stdS_053 = p003 + spc + clicks002 + spc + mm + "\n"
message_stdS_054 = p003 + spc + clicks003 + spc + mm + "\n"
message_stdS_055 = p003 + spc + clicks004 + spc + mm + "\n"

message_stdS_056 = p003 + spc + errors001 + spc + mm + "\n"
message_stdS_057 = p003 + spc + errors002 + spc + mm + "\n"
message_stdS_058 = p003 + spc + errors003 + spc + mm + "\n"
message_stdS_059 = p003 + spc + errors004 + spc + mm + "\n"

message_stdS_060 = p003 + spc + birads001 + spc + mm + "\n"
message_stdS_061 = p003 + spc + birads002 + spc + mm + "\n"
message_stdS_062 = p003 + spc + birads003 + spc + mm + "\n"


# ============================================== #

# ============================================== #
#                   Tukeys HSD                   #
# ============================================== #

mc_unique_group = "MC Unique Group" + "\n"
m_t_main = "Compute Tukeys HSD for" + spc
m_t_t_001 = "[SM]" + spc + "Data:" + spc
m_t_t_002 = "[MM]" + spc + "Data:" + spc
m_t_t_003 = "Group:" + spc
m_t_t_004 = "F-test" + spc + "=" + spc
m_t_t_005 = "p-value" + spc + "=" + spc
m_t_t_006 = "[SM]" + spc + "SD" + spc + "=" + spc
m_t_t_007 = "[MM]" + spc + "SD" + spc + "=" + spc
m_t_t_008 = "[SM]" + spc + "Mean" + spc + "=" + spc
m_t_t_009 = "[MM]" + spc + "Mean" + spc + "=" + spc
m_t_w = "\n" + "When computing Tukeys HSD for" + spc
m_degree_freedom = spc + "there is no enough Degree of Freedom (DF)." + "\n"
m_marks_thsd = "\n" + "++++++++++++++++++++++++++++++++++++++++" + "\n"

# ============================================== #

# ============================================== #
# ============================================== #
# ============================================== #

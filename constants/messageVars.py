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
ent = "\n"
of = "of"
pfor = "for"

p001 = "Verification of the Mean for"
p002 = "Compute Mean for"
p003 = "Compute Standard Deviation (SD) for"

sm = "(SM)"
mm = "(MM)"

sma = "[SM]"
mma = "[MM]"

nasatlx = "NASA-TLX"
md = "MD"
pd = "PD"
td = "TD"
pe = "PE"
ef = "EF"
fr = "FR"

sus = "SUS"
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

ptime = "Time"
time001 = "TIME__94662"
time002 = "TIME_607376"
time003 = "TIME_737037"
time004 = "TIME__TOTAL"

clicks = "Clicks"
clicks001 = "CLICKS__94662"
clicks002 = "CLICKS_607376"
clicks003 = "CLICKS_737037"
clicks004 = "CLICKS__TOTAL"

errors = "Errors"
errors001 = "ERRORS__94662"
errors002 = "ERRORS_607376"
errors003 = "ERRORS_737037"
errors004 = "ERRORS__TOTAL"

birads = "BIRADS"
birads001 = "BIRADS__94662"
birads002 = "BIRADS_607376"
birads003 = "BIRADS_737037"

m_mean = "Mean"
m_means = "Means"

m_std = "SD"
m_stds = "SDs"

m_intern = "Intern"
m_junior = "Junior"
m_middle = "Middle"
m_senior = "Senior"

m_interns = "Interns"
m_juniors = "Juniors"
m_middles = "Middles"
m_seniors = "Seniors"

# ============================================== #

# ============================================== #
#                 Error Messages                 #
# ============================================== #

m_err_001 = ent + "Please try another flag..." + ent

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
m_equal_thsd = "\n" + "========================================" + "\n"

m_t_hsd_001 = "[Compute Tukey Modalities]" + spc + "F-test" + spc + "=" + spc
m_t_hsd_002 = "[Compute Tukey Modalities]" + spc + "p-value" + spc + "=" + spc

# ============================================== #

# ============================================== #
#                Data File Groups                #
# ============================================== #

sma_means = sma + spc + m_means + spc + of + spc
mma_means = mma + spc + m_means + spc + of + spc

sma_stds = sma + spc + m_stds + spc + of + spc
mma_stds = mma + spc + m_stds + spc + of + spc

m_dfg_001 = sma_means + sus + spc + pfor + spc + m_interns + ent
m_dfg_002 = sma_means + sus + spc + pfor + spc + m_juniors + ent
m_dfg_003 = sma_means + sus + spc + pfor + spc + m_middles + ent
m_dfg_004 = sma_means + sus + spc + pfor + spc + m_seniors + ent

m_dfg_005 = mma_means + sus + spc + pfor + spc + m_interns + ent
m_dfg_006 = mma_means + sus + spc + pfor + spc + m_juniors + ent
m_dfg_007 = mma_means + sus + spc + pfor + spc + m_middles + ent
m_dfg_008 = mma_means + sus + spc + pfor + spc + m_seniors + ent

m_dfg_009 = sma_stds + sus + spc + pfor + spc + m_interns + ent
m_dfg_010 = sma_stds + sus + spc + pfor + spc + m_juniors + ent
m_dfg_011 = sma_stds + sus + spc + pfor + spc + m_middles + ent
m_dfg_012 = sma_stds + sus + spc + pfor + spc + m_seniors + ent

m_dfg_013 = mma_stds + sus + spc + pfor + spc + m_interns + ent
m_dfg_014 = mma_stds + sus + spc + pfor + spc + m_juniors + ent
m_dfg_015 = mma_stds + sus + spc + pfor + spc + m_middles + ent
m_dfg_016 = mma_stds + sus + spc + pfor + spc + m_seniors + ent

m_dfg_017 = sma_means + nasatlx + spc + pfor + spc + m_interns + ent
m_dfg_018 = sma_means + nasatlx + spc + pfor + spc + m_juniors + ent
m_dfg_019 = sma_means + nasatlx + spc + pfor + spc + m_middles + ent
m_dfg_020 = sma_means + nasatlx + spc + pfor + spc + m_seniors + ent

m_dfg_021 = mma_means + nasatlx + spc + pfor + spc + m_interns + ent
m_dfg_022 = mma_means + nasatlx + spc + pfor + spc + m_juniors + ent
m_dfg_023 = mma_means + nasatlx + spc + pfor + spc + m_middles + ent
m_dfg_024 = mma_means + nasatlx + spc + pfor + spc + m_seniors + ent

m_dfg_025 = sma_stds + nasatlx + spc + pfor + spc + m_interns + ent
m_dfg_026 = sma_stds + nasatlx + spc + pfor + spc + m_juniors + ent
m_dfg_027 = sma_stds + nasatlx + spc + pfor + spc + m_middles + ent
m_dfg_028 = sma_stds + nasatlx + spc + pfor + spc + m_seniors + ent

m_dfg_029 = mma_stds + nasatlx + spc + pfor + spc + m_interns + ent
m_dfg_030 = mma_stds + nasatlx + spc + pfor + spc + m_juniors + ent
m_dfg_031 = mma_stds + nasatlx + spc + pfor + spc + m_middles + ent
m_dfg_032 = mma_stds + nasatlx + spc + pfor + spc + m_seniors + ent

m_dfg_033 = sma_means + ptime + spc + pfor + spc + m_interns + ent
m_dfg_034 = sma_means + ptime + spc + pfor + spc + m_juniors + ent
m_dfg_035 = sma_means + ptime + spc + pfor + spc + m_middles + ent
m_dfg_036 = sma_means + ptime + spc + pfor + spc + m_seniors + ent

m_dfg_037 = mma_means + ptime + spc + pfor + spc + m_interns + ent
m_dfg_038 = mma_means + ptime + spc + pfor + spc + m_juniors + ent
m_dfg_039 = mma_means + ptime + spc + pfor + spc + m_middles + ent
m_dfg_040 = mma_means + ptime + spc + pfor + spc + m_seniors + ent

m_dfg_041 = sma_stds + ptime + spc + pfor + spc + m_interns + ent
m_dfg_042 = sma_stds + ptime + spc + pfor + spc + m_juniors + ent
m_dfg_043 = sma_stds + ptime + spc + pfor + spc + m_middles + ent
m_dfg_044 = sma_stds + ptime + spc + pfor + spc + m_seniors + ent

m_dfg_045 = mma_stds + ptime + spc + pfor + spc + m_interns + ent
m_dfg_046 = mma_stds + ptime + spc + pfor + spc + m_juniors + ent
m_dfg_047 = mma_stds + ptime + spc + pfor + spc + m_middles + ent
m_dfg_048 = mma_stds + ptime + spc + pfor + spc + m_seniors + ent

m_dfg_049 = sma_means + clicks + spc + pfor + spc + m_interns + ent
m_dfg_050 = sma_means + clicks + spc + pfor + spc + m_juniors + ent
m_dfg_051 = sma_means + clicks + spc + pfor + spc + m_middles + ent
m_dfg_052 = sma_means + clicks + spc + pfor + spc + m_seniors + ent

m_dfg_053 = mma_means + clicks + spc + pfor + spc + m_interns + ent
m_dfg_054 = mma_means + clicks + spc + pfor + spc + m_juniors + ent
m_dfg_055 = mma_means + clicks + spc + pfor + spc + m_middles + ent
m_dfg_056 = mma_means + clicks + spc + pfor + spc + m_seniors + ent

m_dfg_057 = sma_stds + clicks + spc + pfor + spc + m_interns + ent
m_dfg_058 = sma_stds + clicks + spc + pfor + spc + m_juniors + ent
m_dfg_059 = sma_stds + clicks + spc + pfor + spc + m_middles + ent
m_dfg_060 = sma_stds + clicks + spc + pfor + spc + m_seniors + ent

m_dfg_061 = mma_stds + clicks + spc + pfor + spc + m_interns + ent
m_dfg_062 = mma_stds + clicks + spc + pfor + spc + m_juniors + ent
m_dfg_063 = mma_stds + clicks + spc + pfor + spc + m_middles + ent
m_dfg_064 = mma_stds + clicks + spc + pfor + spc + m_seniors + ent

m_dfg_065 = sma_means + errors + spc + pfor + spc + m_interns + ent
m_dfg_066 = sma_means + errors + spc + pfor + spc + m_juniors + ent
m_dfg_067 = sma_means + errors + spc + pfor + spc + m_middles + ent
m_dfg_068 = sma_means + errors + spc + pfor + spc + m_seniors + ent

m_dfg_069 = mma_means + errors + spc + pfor + spc + m_interns + ent
m_dfg_070 = mma_means + errors + spc + pfor + spc + m_juniors + ent
m_dfg_071 = mma_means + errors + spc + pfor + spc + m_middles + ent
m_dfg_072 = mma_means + errors + spc + pfor + spc + m_seniors + ent

m_dfg_073 = sma_stds + errors + spc + pfor + spc + m_interns + ent
m_dfg_074 = sma_stds + errors + spc + pfor + spc + m_juniors + ent
m_dfg_075 = sma_stds + errors + spc + pfor + spc + m_middles + ent
m_dfg_076 = sma_stds + errors + spc + pfor + spc + m_seniors + ent

m_dfg_077 = mma_stds + errors + spc + pfor + spc + m_interns + ent
m_dfg_078 = mma_stds + errors + spc + pfor + spc + m_juniors + ent
m_dfg_079 = mma_stds + errors + spc + pfor + spc + m_middles + ent
m_dfg_080 = mma_stds + errors + spc + pfor + spc + m_seniors + ent

m_dfg_081 = sma_means + birads + spc + pfor + spc + m_interns + ent
m_dfg_082 = sma_means + birads + spc + pfor + spc + m_juniors + ent
m_dfg_083 = sma_means + birads + spc + pfor + spc + m_middles + ent
m_dfg_084 = sma_means + birads + spc + pfor + spc + m_seniors + ent

m_dfg_085 = mma_means + birads + spc + pfor + spc + m_interns + ent
m_dfg_086 = mma_means + birads + spc + pfor + spc + m_juniors + ent
m_dfg_087 = mma_means + birads + spc + pfor + spc + m_middles + ent
m_dfg_088 = mma_means + birads + spc + pfor + spc + m_seniors + ent

m_dfg_089 = sma_stds + birads + spc + pfor + spc + m_interns + ent
m_dfg_090 = sma_stds + birads + spc + pfor + spc + m_juniors + ent
m_dfg_091 = sma_stds + birads + spc + pfor + spc + m_middles + ent
m_dfg_092 = sma_stds + birads + spc + pfor + spc + m_seniors + ent

m_dfg_093 = mma_stds + birads + spc + pfor + spc + m_interns + ent
m_dfg_094 = mma_stds + birads + spc + pfor + spc + m_juniors + ent
m_dfg_095 = mma_stds + birads + spc + pfor + spc + m_middles + ent
m_dfg_096 = mma_stds + birads + spc + pfor + spc + m_seniors + ent

# ============================================== #

# ============================================== #
# ============================================== #
# ============================================== #

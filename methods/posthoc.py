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

from tukeyhsd import *

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

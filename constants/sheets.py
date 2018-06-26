#!/usr/bin/env python

"""anova.py: A python version of ANOVA."""

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
#                   VARIABLES                    #
# ============================================== #

MIN_VAL = 4
MAX_VAL = 12

MIN_STR = str(MIN_VAL)
MAX_STR = str(MAX_VAL)

# ============================================== #
#                    NASA-TLX                    #
# ============================================== #

NASATLX_SINGLE_MENTAL_DEMAND   = 'D'
NASATLX_SINGLE_PHYSICAL_DEMAND = 'E'
NASATLX_SINGLE_TEMPORAL_DEMAND = 'F'
NASATLX_SINGLE_PERFORMANCE     = 'G'
NASATLX_SINGLE_EFFORT          = 'H'
NASATLX_SINGLE_FRUSTRATION     = 'I'

NASATLX_MULTI_MENTAL_DEMAND    = 'J'
NASATLX_MULTI_PHYSICAL_DEMAND  = 'K'
NASATLX_MULTI_TEMPORAL_DEMAND  = 'L'
NASATLX_MULTI_PERFORMANCE      = 'M'
NASATLX_MULTI_EFFORT           = 'N'
NASATLX_MULTI_FRUSTRATION      = 'O'

# ============================================== #
#                       SUS                      #
# ============================================== #

SUS_SINGLE_1  = 'P'
SUS_SINGLE_2  = 'Q'
SUS_SINGLE_3  = 'R'
SUS_SINGLE_4  = 'S'
SUS_SINGLE_5  = 'T'
SUS_SINGLE_6  = 'U'
SUS_SINGLE_7  = 'V'
SUS_SINGLE_8  = 'W'
SUS_SINGLE_9  = 'X'
SUS_SINGLE_10 = 'Y'

SUS_MULTI_1   = 'Z'
SUS_MULTI_2   = 'AA'
SUS_MULTI_3   = 'AB'
SUS_MULTI_4   = 'AC'
SUS_MULTI_5   = 'AD'
SUS_MULTI_6   = 'AE'
SUS_MULTI_7   = 'AF'
SUS_MULTI_8   = 'AG'
SUS_MULTI_9   = 'AH'
SUS_MULTI_10  = 'AI'

# ============================================== #
#                      TIME                      #
# ============================================== #

TIME_SINGLE_94662  = 'AJ'
TIME_SINGLE_607376 = 'AK'
TIME_SINGLE_737037 = 'AL'
TIME_SINGLE_TOTAL  = 'AM'

TIME_MULTI_94662   = 'AN'
TIME_MULTI_607376  = 'AO'
TIME_MULTI_737037  = 'AP'
TIME_MULTI_TOTAL   = 'AQ'

# ============================================== #
#                NUMBER OF CLICKS                #
# ============================================== #

CLICKS_SINGLE_94662  = 'AR'
CLICKS_SINGLE_607376 = 'AS'
CLICKS_SINGLE_737037 = 'AT'
CLICKS_SINGLE_TOTAL  = 'AU'

CLICKS_MULTI_94662   = 'AV'
CLICKS_MULTI_607376  = 'AW'
CLICKS_MULTI_737037  = 'AX'
CLICKS_MULTI_TOTAL   = 'AY'

# ============================================== #
#                NUMBER OF ERRORS                #
# ============================================== #

ERRORS_SINGLE_94662  = 'AZ'
ERRORS_SINGLE_607376 = 'BA'
ERRORS_SINGLE_737037 = 'BB'
ERRORS_SINGLE_TOTAL  = 'BC'

ERRORS_MULTI_94662   = 'BD'
ERRORS_MULTI_607376  = 'BE'
ERRORS_MULTI_737037  = 'BF'
ERRORS_MULTI_TOTAL   = 'BG'

# ============================================== #
#                     BIRADS                     #
# ============================================== #

BIRADS_SINGLE_94662  = 'BH'
BIRADS_SINGLE_607376 = 'BI'
BIRADS_SINGLE_737037 = 'BJ'

BIRADS_MULTI_94662   = 'BK'
BIRADS_MULTI_607376  = 'BL'
BIRADS_MULTI_737037  = 'BM'

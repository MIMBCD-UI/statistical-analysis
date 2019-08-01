#!/usr/bin/env python
#coding=utf-8

"""
.py:
"""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "MIT"
__version__     = "1.0.0"
__status__      = "Development"
__copyright__   = "Copyright 2019, Instituto Superior Técnico (IST)"
__credits__     = [
  "Bruno Oliveira",
  "Carlos Santiago",
  "Jacinto C. Nascimento",
  "Pedro Miraldo",
  "Nuno Nunes",
  "Duarte Figueirôa"
]

import logging

logging.basicConfig(format='%(message)s')
log = logging.getLogger()

# Set a severity threshold to one above:
# CRITICAL, ERROR, WARNING, INFO, DEBUG
#
# see:
#
# https://docs.python.org/3/library/logging.html
levelNameToSet = 'CRITICAL'
level = logging.getLevelName(levelNameToSet)
log.setLevel(level)

# This MESSAGES will not reach the Humans.
log.debug('MODE: debug')
log.info('MODE: info')
log.warn('MODE: warn')
log.error('MODE: error')
log.critical('MODE: critical')

## Citizens of Earth, your planet will be removed NOW!

tot001 = 'total'

birads_1 = 1
birads_2 = 2
birads_3 = 3
birads_4 = 4
birads_5 = 5

ext001 = '.txt'
ext002 = '.dcm'
ext003 = '.json'

fne001 = 'cloud'
fne002 = 'full'
fne003 = 'assistant'
fne004 = 'current'
fne005 = 'dgns'
fne006 = 'avtr'
fne007 = 'ext'
fne008 = 'all'
fne009 = 'reg'
fne010 = 'real'
fne011 = 'physician'
fne012 = 'group'

fne103 = 'high'
fne104 = 'medium'
fne105 = 'low'

fne201 = 'understanding'
fne202 = 'capability'
fne203 = 'benevolence'

fne301 = 'mental_demand'
fne302 = 'physical_demand'
fne303 = 'temporal_demand'
fne304 = 'performance'
fne305 = 'effort'
fne306 = 'frustration'

fne601 = 'sus_01'
fne602 = 'sus_02'
fne603 = 'sus_03'
fne604 = 'sus_04'
fne605 = 'sus_05'
fne606 = 'sus_06'
fne607 = 'sus_07'
fne608 = 'sus_08'
fne609 = 'sus_09'
fne610 = 'sus_10'

# ==================== END File ==================== #

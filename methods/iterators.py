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

datafileList = []
datafileListVec = []

def datafileIteratorPerGroup(datafile):
  for i in range(0, 31):
    for j in range(9, 19):
      datafileIndexGroup = datafile.loc[i, "group"]
      datafileIndexGroupStr = str(datafileIndexGroup)
      datafileList.insert(len(datafileList) ,datafileIndexGroupStr)
  return datafileList

def datafileIteratorPerVector(datafile, vector):
  for i in range(0, 31):
    for j in range(9, 19):
      for m in range(len(vector)):
        datafileIndexVec = datafile.loc[i, "group"]
        datafileIndexVecStr = str(datafileIndexVec)
        datafileListVec.insert(len(datafileListVec), vector[m])
    return datafileListVec

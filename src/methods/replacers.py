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

def vecReplacer(arr, vec):
  vecReplacerList = []
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      vecReplacerList.insert(len(vecReplacerList), vec[i])
  return vecReplacerList

def vecReplacePrinter(arr):
  for i in range(len(arr)):
    return arr[i]

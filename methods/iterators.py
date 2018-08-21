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
        # print("datafileIndexVecStr", datafileIndexVecStr)
        # print("vector[m]", vector[m])
        # if(datafileIndexVecStr == vector[m]):
        datafileListVec.insert(len(datafileListVec), vector[m])
    return datafileListVec

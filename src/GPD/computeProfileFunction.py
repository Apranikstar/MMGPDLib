import numpy as np
import src.GPD.csvdataparser as csvdataparser

def computationHandeler(parameters, x):
    results =[]
    for points in x:
        funcAtPoint = parameters[0] * np.power(1 - points, 3) * np.log(1/points) + parameters[1] * np.power(1 - points, 3) + parameters[2] * points * np.power(1-points,2)
        results.append(funcAtPoint)
    return results


def _profileFuncH(analysisType,analysisSet, analysisFlavour, x): 
    if isinstance(x, np.ndarray):
        x = x.tolist()
    else:
        x = [float(x)]
    dataFile = "src/GPD/data/"+analysisType+"/H/"+analysisSet+".csv"
    flavourKeyList = analysisFlavour
    if isinstance(flavourKeyList,str):
        flavourKeyList = [flavourKeyList]
    paramterDict = csvdataparser.get_flavour_values(dataFile, flavourKeyList) # [aprime,B,A]
    results = {}
    for flavours in flavourKeyList:
        parameters = paramterDict[flavours]
        results[flavours] = computationHandeler(parameters, x)
    return results

def _profileFuncHt(analysisType,analysisSet, analysisFlavour, x): 
    if isinstance(x, np.ndarray):
        x = x.tolist()
    else:
        x = [float(x)]
    dataFile = "src/GPD/data/"+analysisType+"/Ht/"+analysisSet+".csv"
    flavourKeyList = analysisFlavour
    if isinstance(flavourKeyList,str):
        flavourKeyList = [flavourKeyList]
    paramterDict = csvdataparser.get_flavour_values(dataFile, flavourKeyList) #  [aprime,B,A]
    results = {}
    for flavours in flavourKeyList:
        parameters = paramterDict[flavours]
        results[flavours] = computationHandeler(parameters, x)
    return results

def _profileFuncE(analysisType,analysisSet, analysisFlavour, x): 
    if isinstance(x, np.ndarray):
        x = x.tolist()
    else:
        x = [float(x)]
    dataFile = "src/GPD/data/"+analysisType+"/E/"+analysisSet+".csv"
    flavourKeyList = analysisFlavour
    if isinstance(flavourKeyList,str):
        flavourKeyList = [flavourKeyList]
    paramterDict = csvdataparser.get_flavour_values(dataFile, flavourKeyList) #[aprime,B,A]
    results = {}
    for flavours in flavourKeyList:
        parameters = paramterDict[flavours]
        results[flavours] = computationHandeler(parameters, x)
    return results
    
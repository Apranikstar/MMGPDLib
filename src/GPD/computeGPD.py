import numpy as np

def computeH(pdfFunction, profileFunction, t, flavourslist):
    if isinstance(t, np.ndarray):
        t = t.tolist()
    else:
        t = [float(t)]
    if isinstance(flavourslist,str):
        flavourslist = [flavourslist]
        
    for flavour in flavourslist:
        resultList = []
        for i in range(len(pdfFunction[flavour])):
            resultList.append(pdfFunction[flavour][i] * np.exp(t[0] * profileFunction[flavour][i]))
    return resultList[0]


def computeHt(pdfFunction, profileFunction, t, flavourslist):
    if isinstance(t, np.ndarray):
        t = t.tolist()
    else:
        t = [float(t)]
    if isinstance(flavourslist,str):
        flavourslist = [flavourslist]
        
    for flavour in flavourslist:
        resultList = []
        for i in range(len(pdfFunction[flavour])):
            resultList.append(pdfFunction[flavour][i] * np.exp(t[0] * profileFunction[flavour][i]))
    return resultList[0]

def computeE(pdfFunction, profileFunction, t, flavourslist):
    if isinstance(t, np.ndarray):
        t = t.tolist()
    else:
        t = [float(t)]
    if isinstance(flavourslist,str):
        flavourslist = [flavourslist]
        
    for flavour in flavourslist:
        resultList = []
        for i in range(len(pdfFunction[flavour])):
            resultList.append(pdfFunction[flavour][i] * np.exp(t[0] * profileFunction[flavour][i]))
    return resultList[0]
import lhapdf
import numpy as np
import src.GPD.csvdataparser as csvdataparser
from scipy.integrate import quad

# First we calculate PDF from LHAPDF and then we calculate PDF from our parameterization 
#############  Subroutines  #############
def GetAnalysisUPDF(AnalysisType):
    if AnalysisType == "HGAG23":
        return lhapdf.mkPDF("NNPDF40_nlo_as_01180",0)
    if AnalysisType == "Analysis2":
        return lhapdf.mkPDF("CT10nlo",0)

def GetAnalysisPPDF(AnalysisType):
    if AnalysisType == "HGAG23":
        return lhapdf.mkPDF("NNPDFpol11_100",0)
    if AnalysisType == "Analysis2":
        return lhapdf.mkPDF("CT10nlo",0)


def _uv(x,analysisPDFSET,Q2):
    results = []
    for items in x:
        results.append(analysisPDFSET.xfxQ(2,items,np.sqrt(Q2)) - analysisPDFSET.xfxQ(-2,items,np.sqrt(Q2)))
    return results
def _dv(x,analysisPDFSET,Q2):
    results = []
    for items in x:
        results.append(analysisPDFSET.xfxQ(1,items,np.sqrt(Q2)) - analysisPDFSET.xfxQ(-1,items,np.sqrt(Q2)))
    return results
def _sv(x,analysisPDFSET,Q2):
    results = []
    for items in x:
        results.append(analysisPDFSET.xfxQ(3,items,np.sqrt(Q2)) - analysisPDFSET.xfxQ(-3,items,np.sqrt(Q2)))
    return results
def _ubar(x,analysisPDFSET,Q2):
    results = []
    for items in x:
        results.append(analysisPDFSET.xfxQ(-2,items,np.sqrt(Q2)) )
    return results
def _dbar(x,analysisPDFSET,Q2):
    results = []
    for items in x:
        results.append(analysisPDFSET.xfxQ(-1,items,np.sqrt(Q2)))
    return results
def _sbar(x,analysisPDFSET,Q2):
    results = []
    for items in x:
        results.append(analysisPDFSET.xfxQ(-3,items,np.sqrt(Q2)) )
    return results
 

def _PDF(x,Q2, flavourList, analysisPDFSET):
    if isinstance(x, np.ndarray):
        x = x.tolist()
    else:
        x = [float(x)]
    if isinstance(Q2, np.ndarray):
        Q2 = Q2.tolist()
    else:
        Q2 = float(Q2)

    if isinstance(flavourList,str):
        flavourList = [flavourList]

    results = {}
    for flavour in flavourList:
        if flavour == "uv":
            results["uv"] = _uv(x,analysisPDFSET,Q2)
        elif flavour == "dv":
            results["dv"] = _dv(x,analysisPDFSET,Q2) 
        elif flavour == "sv":
            results["sv"] = _sv(x,analysisPDFSET,Q2)
        elif flavour =="ubar":
            results["ubar"] =  _ubar(x,analysisPDFSET,Q2)
        elif flavour =="dbar":
            results["dbar"]= _dbar(x,analysisPDFSET,Q2)
        elif flavour =="sbar":
            results["sbar"]=  _sbar(x,analysisPDFSET,Q2)

    return results
        

### PDF for GPD E :
# Define the function to integrate
def integrand(x, alpha_q, beta_q, gamma_q):
    return (np.power(x, -alpha_q) * np.power(1-x, beta_q) * (1 + gamma_q * np.sqrt(x)))


def ComputePDFEFunction(analysisType,analysisSet, analysisFlavour, x):
    if isinstance(x, str):
        x = np.array([float(x)])
    elif isinstance(x, float):
        x = np.array([x])
    elif isinstance(x, int):
        x = np.array([x])


    k={}
    k["uv"]=1.67
    k["dv"]=-2.03

    dataFile = "src/GPD/data/"+analysisType+"/E/"+analysisSet+".csv"
    flavourKeyList = analysisFlavour
    if isinstance(flavourKeyList,str):
        flavourKeyList = [flavourKeyList]

    paramterDict = csvdataparser.get_flavour_values(dataFile, flavourKeyList) 
    alpha= {}
    beta = {}
    gamma = {}
    for flavours in flavourKeyList:
        alpha[flavours] = paramterDict[flavours][3] #alpha
        beta[flavours]= paramterDict[flavours][4] #beta
        gamma[flavours] = paramterDict[flavours][5] # gamma for "uv"

    N = {}
    for flavours in flavourKeyList:
        Nitem , error = quad(integrand, 0, 1, args=(alpha[flavours], beta[flavours], gamma[flavours]))
        N[flavours] = np.divide(1,Nitem)

    E = {}
    for flavours in flavourKeyList: # note that we added a x to make the final results xE[flavour]
        E[flavours] = x * k[flavours] * N[flavours]  * np.power(x,-alpha[flavours]) * np.power(1-x,beta[flavours]) * (1+ gamma[flavours] * np.sqrt(x))
    return E


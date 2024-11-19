import lhapdf
import csv 
import numpy as np
import src.GPD.csvdataparser as csvdataparser
from scipy.integrate import quad
import src.GPD.computeGPD as computeGPD
import src.GPD.computePDF as computePDF
import src.GPD.computeProfileFunction as computeProfileFunction
#import src.GPD.analysisHandler as analysisHandler
import src.GPD.computeGA as computeGA
import src.GPD.initializeAnalysis as initializeAnalysis
import src.GPD.computeF1F2 as computeF1F2
from src.GPD.computeGPDxi import xGPDxiIntegrand 
def listAnalysis():
    initializeAnalysis.List()

def xGPD(InitlizerArgs, analysisSet, analysisGPD, analysisFlavour, x, t):
    Q2 = initializeAnalysis.getQ2(InitlizerArgs[0])
    if analysisGPD == "H":
        profileFunction = computeProfileFunction._profileFuncH(InitlizerArgs[0],analysisSet,analysisFlavour, x)
        pdfFunction = computePDF._PDF(x,Q2, analysisFlavour, InitlizerArgs[1])
        results = computeGPD.computeH(pdfFunction, profileFunction, t, analysisFlavour)
        return results
    if analysisGPD == "Ht":
        profileFunction = computeProfileFunction._profileFuncHt(InitlizerArgs[0],analysisSet,analysisFlavour, x)
        pdfFunction = computePDF._PDF(x,Q2, analysisFlavour, InitlizerArgs[2])
        results = computeGPD.computeHt(pdfFunction, profileFunction, t, analysisFlavour)
        return results
    if analysisGPD == "E":
        profileFunction = computeProfileFunction._profileFuncE(InitlizerArgs[0],analysisSet, analysisFlavour, x)
        analysisPDF = computePDF.ComputePDFEFunction(InitlizerArgs[0],analysisSet, analysisFlavour, x)
        results = computeGPD.computeE(analysisPDF, profileFunction, t, analysisFlavour)
        return results
        
def xGPDxi(InitilizerArgs, Set, GPDType , Flavour, x, t,xi):
    if xi == 0:
        return xGPD(InitilizerArgs, Set, GPDType , Flavour, x, t)
        
    b0 = np.divide(x+xi,1+xi)
    if x <= xi:
        a0 = 1e-5 
    else:
        a0 = np.divide(x-xi,1-xi)
    return quad(xGPDxiIntegrand, a0, b0, args=(InitilizerArgs, Set, GPDType , Flavour,x,t,xi),epsabs=1e-9, limit = 150 )[0]
    
####################
def G_A(InitlizerArgs, analysisSet,t,percision ):
    def GAintegrand(x,t,InitlizerArgs, analysisSet):
        HtUV = computeGA.Ht_uv(x,t,InitlizerArgs, analysisSet)
        HtDV = computeGA.Ht_dv(x,t,InitlizerArgs, analysisSet)
        HtUBAR = computeGA.Ht_ubar(x,t,InitlizerArgs, analysisSet)
        HtDBAR = computeGA.Ht_dbar(x,t,InitlizerArgs, analysisSet)
        return HtUV - HtDV + 2*HtUBAR - 2*HtDBAR
    
    return quad(GAintegrand, 1e-15, 1, args=(t, InitlizerArgs, analysisSet,),  epsabs=percision, epsrel=percision) [0]
    
####################

def G_D(t):
    Lambda2 = 0.71
    return (  1 - t / Lambda2 )**(-2) 
####################

def G_ME_P(InitlizerArgs,analysisSet, t):
    flavourChargeDict = {
    "uv" : np.divide(2,3),
    "dv" : np.divide(-1,3),
    "sv" : np.divide(-1,3)}
 
    m_p = 0.93827 #GeV Proton Mass
    F1 = computeF1F2.F1(InitlizerArgs,analysisSet, t)
    F2 = computeF1F2.F2(InitlizerArgs,analysisSet, t)
    F1P = flavourChargeDict["uv"] * F1["uv"]  + flavourChargeDict["dv"] * F1["dv"] + flavourChargeDict["sv"] * F1["sv"]
    F2P = flavourChargeDict["uv"] * F2["uv"]  + flavourChargeDict["dv"] * F2["dv"] + flavourChargeDict["sv"] * F2["sv"]
    G_M_P = F1P + F2P
    G_E_P = F1P + np.divide(t,4 * np.power(m_p,2)) * F2P
    #print("Results are : [G_M_Proton , G_E_Proton]")
    return G_M_P, G_E_P
####################

def G_ME_N(InitlizerArgs,analysisSet, t):
    flavourChargeDict = {
    "uv" : np.divide(2,3),
    "dv" : np.divide(-1,3),
    "sv" : np.divide(-1,3)}

    m_n = 0.93956
    F1 = computeF1F2.F1(InitlizerArgs,analysisSet, t)
    F2 = computeF1F2.F2(InitlizerArgs,analysisSet, t)
    F1N = flavourChargeDict["dv"] * F1["uv"]  + flavourChargeDict["uv"] * F1["dv"] + flavourChargeDict["sv"] * F1["sv"]
    F2N = flavourChargeDict["dv"] * F2["uv"]  + flavourChargeDict["uv"] * F2["dv"] + flavourChargeDict["sv"] * F2["sv"]
    G_M_N = F1N + F2N
    G_E_N = F1N + np.divide(t,4 * np.power(m_n,2)) * F2N
    #print("Results are : [G_M_Neutron , G_E_Neutron]")
    return G_M_N, G_E_N

####################





    
        

import lhapdf
import csv 
import numpy as np
import src.GPD.csvdataparser as csvdataparser
from scipy.integrate import quad
import src.GPD.computeGPD as computeGPD
import src.GPD.computePDF as computePDF
import src.GPD.computeProfileFunction as computeProfileFunction
import src.GPD.analysisHandler as analysisHandler
import src.GPD.computeGA as computeGA
import src.GPD.initializeAnalysis as initializeAnalysis

def listAnalysis():
    analysisHandler.List()

def xGPD(InitlizerArgs, analysisSet, analysisGPD, analysisFlavour, x, t):
    Q2 = analysisHandler.getQ2(InitlizerArgs[0])
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
        
def G_A(InitlizerArgs, analysisSet,t,percision ):
    def GAintegrand(x,t,InitlizerArgs, analysisSet):
        HtUV = computeGA.Ht_uv(x,t,InitlizerArgs, analysisSet)
        HtDV = computeGA.Ht_dv(x,t,InitlizerArgs, analysisSet)
        HtUBAR = computeGA.Ht_ubar(x,t,InitlizerArgs, analysisSet)
        HtDBAR = computeGA.Ht_dbar(x,t,InitlizerArgs, analysisSet)
        return HtUV - HtDV + 2*HtUBAR - 2*HtDBAR
    
    return quad(GAintegrand, 1e-15, 1, args=(t, InitlizerArgs, analysisSet,),  epsabs=percision, epsrel=percision) [0]
    




    
        

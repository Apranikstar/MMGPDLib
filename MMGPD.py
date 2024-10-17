import lhapdf
import csv
import numpy as np
import src.GPD.csvdataparser as csvdataparser
from scipy.integrate import quad
import src.GPD.computeGPD as computeGPD
import src.GPD.computePDF as computePDF
import src.GPD.computeProfileFunction as computeProfileFunction
import src.GPD.analysisHandler as analysisHandler
def xGPD(analysisType, analysisSet, analysisGPD, analysisFlavour, x, t):
    Q2 = analysisHandler.getQ2(analysisType)
    if analysisGPD == "H":
        analysisUPDF = computePDF.GetAnalysisUPDF(analysisType)
        profileFunction = computeProfileFunction._profileFuncH(analysisType,analysisSet,analysisFlavour, x)
        pdfFunction = computePDF._PDF(x,Q2, analysisFlavour, analysisUPDF)
        results = computeGPD.computeH(pdfFunction, profileFunction, t, analysisFlavour)
        return results
    if analysisGPD == "Ht":
        analysisPPDF = computePDF.GetAnalysisPPDF(analysisType)
        profileFunction = computeProfileFunction._profileFuncHt(analysisType,analysisSet,analysisFlavour, x)
        pdfFunction = computePDF._PDF(x,Q2, analysisFlavour, analysisPPDF)
        results = computeGPD.computeHt(pdfFunction, profileFunction, t, analysisFlavour)
        return results
    if analysisGPD == "E":
        profileFunction = computeProfileFunction._profileFuncE(analysisType,analysisSet, analysisFlavour, x)
        analysisPDF = computePDF.ComputePDFEFunction(analysisType,analysisSet, analysisFlavour, x)
        results = computeGPD.computeE(analysisPDF, profileFunction, t, analysisFlavour)
        return results
        



        

import lhapdf
import os


############
def List():
    directory = 'src/GPD/data'
    
    # List all directories in the 'data' folder
    print ([d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))])

###########
def getQ2(analysisType):
    if analysisType == "HGAG23":
        Q2 = 4.0
        return Q2
    else:
        return 4.0

#########
def GetAnalysisDOI(AnalysisType):
    if AnalysisType == "HGAG23":
        print("#############################################################################")
        print("Thanks for using our analysis! The corresponding paper is: arXiv:2211.09522v2")
        print("#############################################################################")
        print("\n")
#########
def GetAnalysisUPDF(AnalysisType):
    if AnalysisType == "HGAG23":
        return lhapdf.mkPDF("NNPDF40_nlo_as_01180",0)
    if AnalysisType == "Analysis2":
        return lhapdf.mkPDF("NNPDF40_nlo_as_01180",0)

def GetAnalysisPPDF(AnalysisType):
    if AnalysisType == "HGAG23":
        return lhapdf.mkPDF("NNPDFpol11_100",0)
    if AnalysisType == "Analysis2":
        return lhapdf.mkPDF("NNPDFpol11_100",0)
###########

def SelectUGridPDFSet(AnalysisType):
    if AnalysisType == "HGAG23":
        return lhapdf.getPDFSet("NNPDF40_nlo_as_01180") 

def SelectPGridPDFSet(AnalysisType):
    if AnalysisType == "HGAG23":
        return lhapdf.getPDFSet("NNPDFpol11_100") 

#############
def GetUGridPDFSet(AnalysisType):
    if AnalysisType == "HGAG23":
        pset = SelectUGridPDFSet(AnalysisType)
        return  pset.mkPDFs()

def GetPGridPDFSet(AnalysisType):
    if AnalysisType == "HGAG23":
        pset = SelectPGridPDFSet(AnalysisType)
        return  pset.mkPDFs()
##############
    

def Initialize(AnalysisType):
    GetAnalysisDOI(AnalysisType)
    return [AnalysisType, GetAnalysisUPDF(AnalysisType),GetAnalysisPPDF(AnalysisType),SelectUGridPDFSet(AnalysisType),SelectPGridPDFSet(AnalysisType),GetUGridPDFSet(AnalysisType),GetPGridPDFSet(AnalysisType)]





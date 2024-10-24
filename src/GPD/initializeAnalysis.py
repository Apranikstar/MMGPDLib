import lhapdf
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

def GetAnalysisDOI(AnalysisType):
    if AnalysisType == "HGAG23":
        print("#############################################################################")
        print("Thanks for using our analysis! The corresponding paper is: arXiv:2211.09522v2")
        print("#############################################################################")
        print("\n")

def Initialize(AnalysisType):
    GetAnalysisDOI(AnalysisType)
    return [AnalysisType, GetAnalysisUPDF(AnalysisType),GetAnalysisPPDF(AnalysisType)]


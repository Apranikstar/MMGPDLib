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

def Initialize(AnalysisType):
    return [AnalysisType, GetAnalysisUPDF(AnalysisType),GetAnalysisPPDF(AnalysisType)]


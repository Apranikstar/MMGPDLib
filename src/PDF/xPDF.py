import lhapdf as lhf 
import numpy as np
import src.GPD.computePDF as computePDF
from uncertainties import ufloat

def InitializePDF(pdfSetName):
    pset = lhf.getPDFSet(pdfSetName)
    pdfs = pset.mkPDFs()  
    cen = lhf.mkPDF(pdfSetName, 0)  
    xfAll = [0.0 for i in range(pset.size)]
    return [pset,pdfs, cen, xfAll]

def ComputationHandlers(x,Q2,flavour,pset,pdfs,cen,xfAll):
    if flavour=="uv":  
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(2, x, np.sqrt(Q2)) - pdfs[imem].xfxQ(-2, x, np.sqrt(Q2))
    elif flavour=="u":  
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(2, x, np.sqrt(Q2))
    elif flavour=="ubar":  
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(-2, x, np.sqrt(Q2))
    elif flavour=="dv":  
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(1, x, np.sqrt(Q2)) - pdfs[imem].xfxQ(-1, x, np.sqrt(Q2))
    elif flavour=="d":  
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(1, x, np.sqrt(Q2)) 
    elif flavour=="dbar":  
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(-1, x, np.sqrt(Q2))
    elif flavour=="sv":  
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(3, x, np.sqrt(Q2)) - pdfs[imem].xfxQ(-3, x, np.sqrt(Q2))
    elif flavour=="s":  
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(3, x, np.sqrt(Q2)) 
    elif flavour=="sbar":  
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(-3, x, np.sqrt(Q2)) 
    elif flavour=="g":  
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(21, x, np.sqrt(Q2))
    elif flavour=="cv": 
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(4, x, np.sqrt(Q2)) - pdfs[imem].xfxQ(-4, x, np.sqrt(Q2)) 
    elif flavour=="c":  
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(4, x, np.sqrt(Q2)) 
    elif flavour=="cbar":  
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(-4, x, np.sqrt(Q2)) 
    elif flavour=="bv":  
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(5, x, np.sqrt(Q2)) - pdfs[imem].xfxQ(-5, x, np.sqrt(Q2)) 
    elif flavour=="b":  
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(5, x, np.sqrt(Q2)) 
    elif flavour=="bbar": 
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(-5, x, np.sqrt(Q2)) 
    elif flavour=="tv":  
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(6, x, np.sqrt(Q2)) - pdfs[imem].xfxQ(-6, x, np.sqrt(Q2)) 
    elif flavour=="t": 
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(6, x, np.sqrt(Q2)) 
    elif flavour=="tbar":  
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(-6, x, np.sqrt(Q2)) 

    Uncf = pset.uncertainty(xfAll, cl = pset.errorConfLevel) 
    w = (Uncf.errplus + Uncf.errminus)/2 
    s = Uncf.scale  
    return (w * 1/s)


def PDFwUnc(PDFARGS,flavourKey,x,Q2):
    xPDF = computePDF._PDF(x,Q2, flavourKey, PDFARGS[2])[flavourKey][0]
    unc = ComputationHandlers(x,Q2,flavourKey,PDFARGS[0],PDFARGS[1],PDFARGS[2],PDFARGS[3])
    return ufloat(xPDF, unc)
    
    

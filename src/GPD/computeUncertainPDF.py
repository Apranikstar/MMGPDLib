import src.GPD.initializeAnalysis as init
import numpy as np
from src.GPD.computePDF import _PDF

def PDFUncertainty(x,Q2,flavour,pset,pdfs,cen,xfAll):
    if flavour=="uv":  
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(2, x, np.sqrt(Q2)) - pdfs[imem].xfxQ(-2, x, np.sqrt(Q2))
    elif flavour=="ubar": 
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(-2, x, np.sqrt(Q2))
    elif flavour=="dv":  
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(1, x, np.sqrt(Q2)) - pdfs[imem].xfxQ(-1, x, np.sqrt(Q2))
    elif flavour=="dbar": 
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(-1, x, np.sqrt(Q2))
    elif flavour=="sv":  
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(3, x, np.sqrt(Q2)) - pdfs[imem].xfxQ(-3, x, np.sqrt(Q2))
    elif flavour=="sbar": 
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(-3, x, np.sqrt(Q2)) - pdfs[imem].xfxQ(-2, x, np.sqrt(Q2))
    elif flavour=="g":  
        for imem in range(pset.size):
            xfAll[imem] = pdfs[imem].xfxQ(21, x, np.sqrt(Q2)) 
    Uncf = pset.uncertainty(xfAll, cl = pset.errorConfLevel)
    w = (Uncf.errplus + Uncf.errminus)/2  
    s = Uncf.scale  
    return (w * 1/s)


def uncertainxPDFH(InitlizerArgs, x, flavour):
    Q2 = init.getQ2(InitlizerArgs[0])
    # Unpolarized PDF --> H
    cen = InitlizerArgs[1]  # The central value of grid files
    pset = InitlizerArgs[3]
    pdfs = InitlizerArgs[5]   #selecting grid file (PPDF set) from LHAPDF
    xfAll = [0.0 for i in range(pset.size)] ##Fill vectors xfAll using all PDF members.
   
    return  _PDF(x,Q2, [flavour], cen)[flavour][0], PDFUncertainty(x,Q2,flavour,pset,pdfs,cen,xfAll)


def uncertainxPDFHt(InitlizerArgs, x, flavour):
    Q2 = init.getQ2(InitlizerArgs[0])
    # Unpolarized PDF --> H
    cen = InitlizerArgs[2]  # The central value of grid files
    pset = InitlizerArgs[4]
    pdfs = InitlizerArgs[6]   #selecting grid file (PPDF set) from LHAPDF
    xfAll = [0.0 for i in range(pset.size)] ##Fill vectors xfAll using all PDF members.
    return  _PDF(x,Q2, [flavour], cen)[flavour][0], PDFUncertainty(x,Q2,flavour,pset,pdfs,cen,xfAll)

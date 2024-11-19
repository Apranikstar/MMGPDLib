import MMGPD
import numpy as np
from scipy.integrate import quad

def xGPDxiIntegrand(b,InitilizerArgs, Set, GPDType , Flavour,x,t,xi):
    Hv = MMGPD.xGPD(InitilizerArgs, Set, GPDType , Flavour, b, t) / b
    sd = np.divide(Hv, np.power(1-b,3))
    return np.divide(3,4)*sd*(np.power(1-b,2)-np.power(x-b,2)/np.power(xi,2))/xi


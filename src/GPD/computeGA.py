import MMGPD
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

def Ht_uv(x,t):
    return MMGPD.xGPD("HGAG23", "9", "Ht", "uv", x, t) / x

def Ht_dv(x,t):
    return MMGPD.xGPD("HGAG23", "9", "Ht", "dv", x, t) / x

def Ht_ubar(x,t):
    return MMGPD.xGPD("HGAG23", "9", "Ht", "ubar", x, t) / x

def Ht_dbar(x,t):
    return MMGPD.xGPD("HGAG23", "9", "Ht", "dbar", x, t) / x

def GAintegrand(x,t):
        return ( Ht_uv(x,t) - Ht_dv(x,t) ) + 2*(Ht_ubar(x,t) - 2*Ht_dbar(x,t) )

def calcGA(t,percision):
    return quad(GAintegrand, 1e-3, 1, args=(t,), epsabs=percision)  # epsabs is the absolute error margins of integrations
    

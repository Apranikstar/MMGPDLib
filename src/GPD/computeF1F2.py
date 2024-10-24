import MMGPD
from scipy.integrate import quad

def F1 (InitilizeArgs,analysisSet, t):
    result = {}
    def F1integrand(x ,t, InitilizeArgs,analysisSet,flavour):#combine integration * charge
        return MMGPD.xGPD(InitilizeArgs, analysisSet, "H", flavour, x, t) / x
    for flavour in (MMGPD.csvdataparser.getFlavourListFromCSV(InitilizeArgs[0], "H", analysisSet)):
        if flavour == "uv" or flavour =="dv" or flavour =="sv":
            result[flavour]=(quad(F1integrand, 1e-9, 1 , args = (t, InitilizeArgs,analysisSet,flavour,))[0])
    result["sv"] = result.get("sv", 0)
    return result

def F2 (InitilizeArgs,analysisSet, t):
    result = {}
    FlavourList = MMGPD.csvdataparser.getFlavourListFromCSV(InitilizeArgs[0], "E", analysisSet)
    def F2integrand(x ,t, InitilizeArgs,analysisSet,flavour):
        return MMGPD.xGPD(InitilizeArgs, analysisSet, "E", flavour, x, t) / x
        
    for flavour in FlavourList:
        if flavour == "uv" or flavour =="dv" or flavour =="sv":
            result[flavour]=(quad(F2integrand, 1e-9, 1 , args = (t, InitilizeArgs,analysisSet,flavour,))[0])
    result["sv"] = result.get("sv", 0)
    return result
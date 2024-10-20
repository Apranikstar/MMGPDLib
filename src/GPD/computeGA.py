import MMGPD


def Ht_uv(x,t,InitlizerArgs, analysisSet):
    return MMGPD.xGPD(InitlizerArgs, analysisSet, "Ht", "uv", x, t) / x

def Ht_dv(x,t,InitlizerArgs, analysisSet):
    return MMGPD.xGPD(InitlizerArgs, analysisSet, "Ht", "dv", x, t) / x

def Ht_ubar(x,t,InitlizerArgs, analysisSet):
    return MMGPD.xGPD(InitlizerArgs, analysisSet, "Ht", "ubar", x, t) / x

def Ht_dbar(x,t,InitlizerArgs, analysisSet):
    return MMGPD.xGPD(InitlizerArgs, analysisSet, "Ht", "dbar", x, t) / x




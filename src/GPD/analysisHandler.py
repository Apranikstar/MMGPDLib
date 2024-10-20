import os


def getQ2(analysisType):
    if analysisType == "HGAG23":
        Q2 = 4.0
        return Q2
    else:
        return 4.0

import os

def List():
    directory = 'src/GPD/data'
    
    # List all directories in the 'data' folder
    print ([d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))])

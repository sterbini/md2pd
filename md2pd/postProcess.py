import numpy as np
import pandas as pd

def raw2bbbDF(rawInput):
    '''
    Input: 
    rawInput is a pandas Series containing vectors (FBCT, lumi, etc...)
    
    Output: 
    A df containing the same data, splitted bbb in each column
    '''
    DF = pd.DataFrame()
    for i in range(len(rawInput)):
        DF[i] = rawInput.dropna().apply(lambda x:x[i])
    return DF

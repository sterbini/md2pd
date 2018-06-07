import numpy as np
import pandas as pd

def initializeDF(variables, LastMinutesToConsider = 2., startTime = pd.Timestamp.now(tz='CET')):
    '''
    Initialize a DF, downloading the data from CALS for a given amount of time. 
    By defaut, it downloads the data for the two last minutes countung from now. 
    '''
    return cals2pd(variables,startTime-pd.offsets.Minute(LastMinutesToConsider),startTime)

def _addRowsFromCals(myDF, deltaTime = pd.offsets.Minute(2)):
    '''
    This function allows the user to update a previsously initialized DF with the data for a given amount of time. 
    By defaut, it adds two minutes from the last index of the input DF. 
    '''
    aux=cals2pd(list(myDF),myDF.index[-1],myDF.index[-1]+deltaTime)
    myDF=pd.concat([myDF,aux])
    return myDF

def addColumnsFromCals(myDF, listOfVariables):
    '''
    It allows the user to add columns to a previsouly initialized DF.
    This will not update in time. 
    '''
    aux=cals2pd(listOfVariables,myDF.index[0],myDF.index[-1])
    myDF=pd.concat([myDF,aux])
    return myDF

def refreshData(raw_data, minutesToAdd=10):
    '''
    This is the function to us ein order to refresh a DF with the last data in time. 
    By defaut, it downloads 10 minutes of data with respect to the last index of the input DF. 
    '''
    raw_data = _addRowsFromCals(raw_data,deltaTime=pd.offsets.Minute(minutesToAdd))
    return raw_data

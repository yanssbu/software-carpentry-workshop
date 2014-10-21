import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

def change_to_celsius(x):
    '''change temperature from Fahr to C'''
    degree = (x-32)*5/9
    return degree

def analyze(data):
    '''perform analysis on mosquito data
    
       data is a DataFrame with columns 'temperature', 'rainfall' and 'mosquitos'.
       Performs a least squares regression, plots the result and returns the fit parameters'''
    
    assert data['temperature'].max() < 70, 'check the input temp is less than 70'
    regr_results = sm.OLS.from_formula('mosquitos ~ temperature + rainfall', data).fit()
    parameters = regr_results.params
    rsquared = regr_results.rsquared
    predicted = parameters[0] + parameters[1] * data['temperature'] + parameters[2] * data['rainfall']
    plt.plot(predicted, data['mosquitos'], 'ro')
    min_mosquitos, max_mosquitos = min(data['mosquitos']), max(data['mosquitos'])
    plt.plot([min_mosquitos, max_mosquitos], [min_mosquitos, max_mosquitos], 'k-')
    plt.show() # use this to show multi figures
    
    return parameters
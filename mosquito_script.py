import pandas as pd
import analyze_mosquito_data as am

filename = 'A1_mosquito_data.csv'
data = pd.read_csv(filename)


data['temperature'] = am.change_to_celsius(data['temperature'])


parameters = am.analyze(data, 'plot.png')
# if the function is defined with 2 parameters, when the function is called, 2 parameters have to be called

# save parameters to file
parameters.to_csv('parameters.csv')

import pandas as pd
import analyze_mosquito_data as am

filename = 'A1_mosquito_data.csv'
data = pd.read_csv(filename)


data['temperature'] = am.change_to_celsius(data['temperature'])


parameters = am.analyze(data)

# save parameters to file
parameters.to_csv('parameters.csv')

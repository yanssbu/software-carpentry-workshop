import sys # to interface with system
import pandas as pd
import analyze_mosquito_data as am

filename = sys.argv[1] # 1st argument

print 'Analyzing', filename

data = pd.read_csv(filename)

data['temperature'] = am.change_to_celsius(data['temperature'])

print 'Running analyze'
parameters = am.analyze(data, filename.replace('csv','png'))
# if the function is defined with 2 parameters, when the function is called, 2 parameters have to be called
# arguments can be called by positions or by keyname eg figure_filename='plot.png'

# save parameters to file

print 'Saving parameters'
parameters.to_csv(filename.replace('data', 'parameters'))

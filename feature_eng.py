import pandas as pd
import numpy as np
import sys
import os

# Read the filename of the raw training data
print('PLZ input the filename of the raw data:')
infile = sys.stdin.readline()
infile = infile.strip() 

# Read the raw training data
data = pd.read_csv(infile)

# Transform the date_time format so that pandas can recognize 
data['date_time'] = pd.to_datetime(data['date_time'])
date_time = data['date_time']

# Seperate the YEAR, MONTH, DAY and TIME(seconds in a day)
data['year'] = [t.year for t in date_time]
data['month'] = [t.month for t in date_time]
data['day'] = [t.day for t in date_time]
data['time_in_second'] = [t.hour * 3600 + t.minute * 60 + t.second for t in date_time]

# Generate the filename for saving the data with new feature
outfile_data = os.path.splitext(infile)[0] + '_newfeature.txt'

# Generate the filename for saving the names of features(columns)
outfile_flist = os.path.splitext(infile)[0] + '_featurelist.txt'

# Save the data with new features
data.to_csv(outfile_data, index = False)

# Save the names of new features
data.columns.tofile(outfile_flist, sep = ',')

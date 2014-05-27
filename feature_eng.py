import pandas as pd
import numpy as np
import sys
import os

#sys.stdout.write('PLZ input the filename of the raw data:')
print('PLZ input the filename of the raw data:')
infile = sys.stdin.readline()
infile = infile.strip() 
data = pd.read_csv(infile)

data['date_time'] = pd.to_datetime(data['date_time'])
date_time = data['date_time']

data['year'] = [t.year for t in date_time]
data['month'] = [t.month for t in date_time]
data['day'] = [t.day for t in date_time]
data['time_in_second'] = [t.hour * 3600 + t.minute * 60 + t.second for t in date_time]

outfile_data = os.path.splitext(infile)[0] + '_newfeature.txt'
outfile_flist = os.path.splitext(infile)[0] + '_featurelist.txt'

data.to_csv(outfile_data, index = False)

data.columns.tofile(outfile_flist, sep = ',')

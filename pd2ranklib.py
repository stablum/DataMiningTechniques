import pandas as pd
import numpy as np
import re
import sys
import os
import string

# Read the data with new features
print('PLZ input the filename of the input data:')
datafilename = sys.stdin.readline()
datafilename = datafilename.strip()
data = pd.read_csv(datafilename)

# Read the feature list that we use(Generated by feature_eng.py, selected manually before imported here)
print('PLZ input the filename of the feature list:')
featurefilename = sys.stdin.readline()
featurefilename = featurefilename.strip()
features = pd.read_csv(featurefilename).columns.tolist()

# Filter the data by features
data = data[features]

# Fill out the missing value with mean value
#data = data.fillna(data.mean())

# Add a new column for relevance value, which is required by RankLib
data['rel'] = 0

# Translate the click and booking behaviour in to relvance values
data.loc[data['click_bool'] == 1, 'rel'] = 1
data.loc[data['booking_bool'] == 1, 'rel'] = 5

# Pick out the numerical features
num_cols = data.columns.tolist()
num_cols.remove('rel')
num_cols.remove('booking_bool')
num_cols.remove('click_bool')
num_cols.remove('gross_bookings_usd')
num_cols.remove('srch_id')

# Going to use to_string() to transform the data into RankLib style
# A column-format dictionary is required.

# Format the numerical features
formats = []
for i, v in enumerate(num_cols):
	if data[v].dtype in ['int32', 'int64']:
		formats.append(lambda x, i=i: str(i + 1) + ':%i' %x)
	else:
		formats.append(lambda x, i=i: str(i + 1) + ':%.4f' %x)

# Build the dictionary for numerical features
formats_dict = dict(zip(num_cols, formats))

# Create entries for the 'rel' and 'srch_id' ('qid' in RankLib)
formats_dict['srch_id'] = lambda x: 'qid:%i' %x
formats_dict['rel'] = lambda x: '%i' %x

# Change numerical features into float
data[num_cols].astype(float)

# Put all columns together
all_cols = ['rel', 'srch_id'] + num_cols

length = data.shape[0] - 1

# Write to file
outfilename = datafilename.replace('_newfeature.txt', '_ranklib.txt')

f = open(outfilename, 'w')
f.close()

for i in range(0, int(length / 10000)):

	# Write the data to string buffer
	buf = data[i * 10000 : (i + 1) * 10000].to_string(columns = all_cols, formatters = formats_dict, index = False, header = False)

	# Strip extra spaces
	buf = re.sub(' +', ' ', buf)

	f = open(outfilename, 'a')
	f.write(buf + '\n')
	f.close()

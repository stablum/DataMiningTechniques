import pandas as pd
import numpy as np
import re
import sys
import os
import string

print('PLZ input the filename of the input data:')
datafilename = sys.stdin.readline()
datafilename = datafilename.strip()
print('PLZ input the filename of the feature list:')
featurefilename = sys.stdin.readline()
featurefilename = featurefilename.strip()

data = pd.read_csv(datafilename)
features = pd.read_csv(featurefilename).columns.tolist()

data = data[features]
data = data.fillna(data.mean())

data['rel'] = 0
data.loc[data['click_bool'] == 1, 'rel'] = 1
data.loc[data['booking_bool'] == 1, 'rel'] = 5

cols = data.columns.tolist()

cols.remove('rel')
cols.remove('booking_bool')
cols.remove('click_bool')
cols.remove('srch_id')

formats = []
for i, v in enumerate(cols):
	formats.append(lambda x, i=i: str(i + 1) + ':%.4f' %x)

formats_dict = dict(zip(cols, formats))

formats_dict['srch_id'] = lambda x: 'qid:%i' %x
formats_dict['rel'] = lambda x: '%i' %x

data[cols].astype(float)

cols = ['rel', 'srch_id'] + cols

length = data.shape[0] - 1

buf = data.to_string(columns = cols, formatters = formats_dict, index = False, header = False)
buf = re.sub(' +', ' ', buf)
outfilename = datafilename.replace('_newfeature.txt', '_ranklib.txt')
f = open(outfilename, 'w')
f.write(buf)
f.close()

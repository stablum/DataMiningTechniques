import pandas as pd
import numpy as np
import re

data = pd.read_csv('data/train_sel.csv')
data = data.fillna(data.mean())

data['rel'] = 0
data.loc[data['click_bool'] == 1, 'rel'] = 1
data.loc[data['booking_bool'] == 1, 'rel'] = 5

cols = data.columns.tolist()

cols.remove('rel')
cols.remove('gross_bookings_usd')
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

f = open('data/train.txt', 'w')
#for i in range(0, length):
#	row = data.iloc[i].to_frame().T.to_string(columns = cols, formatters = formats_dict, index = False, header = False)
#	f.write(row + '\n')
#	print(str(i / length * 100) + '%, ' + str(i))
buf = data.to_string(columns = cols, formatters = formats_dict, index = False, header = False)
buf = re.sub(' +', ' ', buf)
f.write(buf)
f.close()

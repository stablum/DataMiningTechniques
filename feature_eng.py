import pandas as pd
import numpy as np

data = pd.read_csv('data/training_set_VU_DM_2014.csv')

data['date_time'] = pd.to_datetime(data['date_time'])
date_time = data['date_time']

data['year'] = [t.year for t in date_time]
data['month'] = [t.month for t in date_time]
data['day'] = [t.day for t in date_time]
data['time_in_second'] = [t.hour * 3600 + t.minute * 60 + t.second for t in date_time]

data.to_csv('data/fe_training_set_VU_DM_2014.csv', index = False)

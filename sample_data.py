import pandas as pd
import numpy as np
import random

data = pd.read_csv('data/training_set_VU_DM_2014.csv')

srch_id_all = pd.unique(data['srch_id']);
srch_id_sample = random.sample(list(srch_id_all), 100)
data_sample = data[data.srch_id.isin(srch_id_sample)]

data_sample.to_csv('data/training_set_VU_DM_2014_sample.csv', index=False)

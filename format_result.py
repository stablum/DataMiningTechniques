import pandas as pd
import sys
import os

# Input filename of raw test data
print('PLZ input the original test dataset:')
datafile = sys.stdin.readline()
datafile = datafile.strip()
print('input filename:', datafile)

# Input filename of prediction
print('PLZ input the ranking file of RankLib:')
rankfile = sys.stdin.readline()
rankfile = rankfile.strip()
print('input filename:', rankfile)

# Read data
data = pd.read_csv(datafile)
data = data[['srch_id', 'prop_id']]
data['group_idx'] = data.groupby('srch_id').cumcount()
result = pd.read_csv(rankfile, sep = '\t', header = None, names = ['srch_id', 'group_idx', 'score'])

# Join the two tables
merged = pd.merge(data, result, how = 'inner')

# Pick out the columns we need
merged = merged[['srch_id', 'prop_id', 'score']]

# Sort the result according to the score in each group
sort = merged.sort(['srch_id', 'score'], ascending = [1, 0])
sort.rename(columns = {'srch_id' : 'SearchId', 'prop_id' : 'PropertyId'}, inplace = True)

# Input filename of output file
print('PLZ input the filename of the output:')
outfile = sys.stdin.readline()
outfile = outfile.strip()
print('input filename', outfile)
sort[['SearchId', 'PropertyId']].to_csv(outfile, index = False)

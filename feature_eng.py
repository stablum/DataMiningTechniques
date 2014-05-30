import pandas as pd
import numpy as np
import sys
import os
import missing_data_detection
import normalization

# Read the filename of the raw training data
if len(sys.argv) < 2:
    print('PLZ input the filename of the raw data:')
    infile = sys.stdin.readline()
else:
    infile = sys.argv[1]

infile = infile.strip()
print("input filename:",infile)

# Generate the filename for saving the data with new feature
print("generating output filename...")
outfile_data = os.path.splitext(infile)[0] + '_newfeature.txt'
print("will be:",outfile_data)

# Generate the filename for saving the names of features(columns)
print("generating output featurelist filename...")
outfile_flist = os.path.splitext(infile)[0] + '_featurelist.txt'
print("will be:",outfile_flist)

# Read the raw training data
print("reading input raw training data...")
data = pd.read_csv(infile)
print("done.")

# Save the data with new features
# detect attributes with missing data and add a new 1/0-valued attribute
# which indicates if the attribute of reference is empty or not
print("running missing_data_detection...")
missing_data_detection.run(data)
print("done.")

# add z-score attributes to all numerical attributes
print("normalizing the numerical features...")
normalization.zscore_dataset(data)
print("done.")

# Transform the date_time format so that pandas can recognize 
print("converting date_time to type datetime")
data['date_time'] = pd.to_datetime(data['date_time'])
date_time = data['date_time']
print("done")

# Seperate the YEAR, MONTH, DAY and TIME(seconds in a day)
print("extrating year...")
data['year'] = [t.year for t in date_time]
print("done. extracting month...")
data['month'] = [t.month for t in date_time]
print("done. extracting day...")
data['day'] = [t.day for t in date_time]
print("done. extracting time_in_second...")
data['time_in_second'] = [t.hour * 3600 + t.minute * 60 + t.second for t in date_time]
print("done.")


print("saving data to csv...")
data.to_csv(outfile_data, index = False)
print("done.")

# Save the names of new features
print("saving the names of the new features...")
data.columns.tofile(outfile_flist, sep = ',')
print("done.")


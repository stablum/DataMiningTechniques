import pandas as pd
import sys
import pdb
import random

def main():
	if len(sys.argv) < 2:
		print('input dataset filename:')
		infile = sys.stdin.readline()
	else:
		infile = sys.argv[1]
	
	outfile_positive = infile.replace(".csv","_featureranking_positive.csv")
	outfile_positive = outfile_positive.replace(".txt","_featureranking_positive.csv")
	outfile_negative = infile.replace(".csv","_featureranking_negative.csv")
	outfile_negative = outfile_negative.replace(".txt","_featureranking_negative.csv")
	print("outfile_positive",outfile_positive)
	print("outfile_negative",outfile_negative)
	chunksize = 10000
	reader = pd.read_csv(infile, iterator=True, chunksize=chunksize)
	i = 0
	positive_dataset = None
	negative_dataset = None
	for chunk in reader:
		tmp_positive = chunk[chunk.booking_bool > 0]
		tmp_negative = chunk[chunk.booking_bool < 1]
		tmp_negative = tmp_negative[tmp_negative.click_bool < 1]
		
		for j in range(0,10):
			index_positive = int(random.uniform(0,len(tmp_positive)))
			index_negative = int(random.uniform(0,len(tmp_negative)))
			selected_row_positive = tmp_positive.iloc[index_positive:index_positive+1]
			selected_row_negative = tmp_negative.iloc[index_negative:index_negative+1]
			positive_dataset = pd.concat([positive_dataset,selected_row_positive])
			negative_dataset = pd.concat([negative_dataset,selected_row_negative])
		
		print(i,end=" ",flush=True)
		i+=1
	
	positive_dataset.to_csv(outfile_positive)
	negative_dataset.to_csv(outfile_negative)
	
	print("\nall done.")
if __name__ == "__main__":
    main()

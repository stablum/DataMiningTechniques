# create reader for the dataset
# please note: we cannot store it entirely in memory,
# hence we need to read every time the data from disk

import csv

FILENAME="data/training_set_VU_DM_2014.csv"

def create_reader(filename):
	file_obj = open(filename)
	reader = csv.DictReader(file_obj)
	return reader

def main():
	print "inside __main__"
	global FILENAME
	reader = create_reader(FILENAME)
	print reader.fieldnames

if __name__ == "__main__":
	main()

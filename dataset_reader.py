# load dataset

import csv

FILENAME="data/training_set_VU_DM_2014.csv"

def create_reader(filename):
	file_obj = open(filename)
	reader = csv.reader(file_obj)
	return reader

def main():
	print "inside __main__"
	global FILENAME
	reader = load(FILENAME)

if __name__ == "__main__":
	main()
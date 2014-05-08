import sys
import csv
import dataset_reader

def main():
	reader = dataset_reader.create_reader('data/test.csv')
	
	write_file_obj = open('test_fake_data.csv', 'w')
	writer = csv.DictWriter(write_file_obj, delimiter=',', lineterminator='\n', fieldnames = reader.fieldnames)
	writer.writeheader();

	i = 0
	for row in reader:
		i += 1
		if i >= 1000:
			break
		writer.writerow(row)
		print(row)
	
	write_file_obj.close()

main()

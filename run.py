# main script. Used for launching commands.

# libraries imports
import sys

# local imports
import ratiocharts
import dataset_reader

def main():
	cmd = sys.argv[1]
	
	if cmd == "ratiocharts": # FIME: refactor with lambdas?
		reader = dataset_reader.create_default_reader()
		ratiocharts.create_charts(reader)

	if cmd == "testpie":
		testcounter = {
			'foo': 1,
			'bar': 2,
			'quux': 3,
		}
		ratiocharts.plot_pie(testcounter, "testpie.png")

	if cmd == "header":
		reader = dataset_reader.create_default_reader()
		print("dataset's fieldnames (header)")
		print(reader.fieldnames)

	if cmd == "row":
		rownr = int(sys.argv[2])
		reader = dataset_reader.create_default_reader()
		i = 0
		for row in reader:
			i+=1
			if i == rownr:
				print(row)
				break

if __name__ == "__main__":
	main()

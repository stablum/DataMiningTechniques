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

if __name__ == "__main__":
	main()

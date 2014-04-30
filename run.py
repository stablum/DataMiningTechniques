# main script. Used for launching commands.

# libraries imports
import sys

# local imports
import ratiocharts
import dataset_reader

def main():
	cmd = sys.argv[1]
	if cmd == "ratiocharts":
		reader = dataset_reader.create_default_reader()
		ratiocharts.create_charts(reader)

if __name__ == "__main__":
	main()

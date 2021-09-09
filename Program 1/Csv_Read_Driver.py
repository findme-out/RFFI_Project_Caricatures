import argparse
import Csv_Read


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("path", help="a path to the csv file")
	args = parser.parse_args()
	data = Csv_Read.read_csv(args.path)
	print(data)
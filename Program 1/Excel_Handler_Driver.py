#!/usr/bin/env python3



import argparse
import Excel_Handler


#----------------------- RFFI Project Caricatures ---------------------
# 2021
# Excel Handler Driver File
#----------------------------------------------------------------------


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("path", help="a path to the catalog for input Excel data")
	args = parser.parse_args()
	file_location = Excel_Handler.get_file_location(args.path)
	data, status = Excel_Handler.get_result_data(file_location)
	file_success = 0
	for i in status:
    		if i[0] == 'success':
        		file_success += 1
	print('finished: ', file_success, '/', len(file_location), ' successfully', sep='')

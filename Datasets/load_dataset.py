#!/usr/bin/env python

import sys
import hickle

#============================================

if __name__ == '__main__':

	if not len(sys.argv) == 2:
		print 'ERROR: You need to provide the name of the dataset file to load'
		print '       >> python load_dataset.py dataset.hkl'

	dataset_name = sys.argv[1]
	
	# load the content of the dataset file into a python dictionary
	dataset = hickle.load(dataset_name)


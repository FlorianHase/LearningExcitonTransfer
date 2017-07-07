#!/usr/bin/env python

import hickle
import numpy as np 


data = hickle.load('fmo_dataset.hkl')

for key, value in data.items():
	print key, value
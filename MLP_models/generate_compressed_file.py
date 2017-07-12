#!/usr/bin/env python 

import hickle
import numpy as np

#================================================

# create a set of random 8x8 matrices
features = np.random.rand(1000, 8, 8)

# reshape matrices into a vector
features = np.reshape(features, (1000, 64))

# create dictionary, store features under key 'features'
dataset = {'features': features}

# dump dictionary to file 
hickle.dump(dataset, 'dataset.hkl')


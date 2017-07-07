#!/usr/bin/env python

import hickle 
import numpy as np

#===============================================================

cp43_params = {'layers': 3,
	  	       'in_dim': 21*21,
		       'out_dim': 2,
		       'hidden_dim': 1899,
		       'act': 'tanh',
		       'upper_feature': 109.10804098,
		       'lower_feature': 0.,
		       'upper_target': np.array([12.5613375, 0.2404482]),
		       'lower_target': np.array([0., 0.])}

#===============================================================

if __name__ == '__main__':

	hickle.dump(cp43_params, 'hyperparams_cp43.hkl')
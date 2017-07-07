#!/usr/bin/env python

import hickle 
import numpy as np

#===============================================================

rc_params = {'layers': 3,
	  	     'in_dim': 8*8,
		     'out_dim': 2,
		     'hidden_dim': 1729,
		     'act': 'softsign',
		     'upper_feature': 72.6350507303,
		     'lower_feature': 0.,
		     'upper_target': np.array([4.518815, 0.24848872]),
		     'lower_target': np.array([0., 0.])}

cp43_params = {'layers': 3,
	  	       'in_dim': 21*21,
		       'out_dim': 2,
		       'hidden_dim': 1899,
		       'act': 'tanh',
		       'upper_feature': 109.10804098,
		       'lower_feature': 0.,
		       'upper_target': np.array([12.5613375, 0.2404482]),
		       'lower_target': np.array([0., 0.])}

cp47_params = {'layers': 3,
	  	       'in_dim': 24*24,
		       'out_dim': 2,
		       'hidden_dim': 749,
		       'act': 'softsign',
		       'upper_feature': 284.436362105,
		       'lower_feature': 0.,
		       'upper_target': np.array([34.771175, 0.2444959]),
		       'lower_target': np.array([0., 0.])}

#===============================================================

if __name__ == '__main__':

	hickle.dump(rc_params, 'hyperparams_rc.hkl')
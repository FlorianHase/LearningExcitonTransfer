#!/usr/bin/env python 

import hickle
import numpy as np

#================================================

template = hickle.load('../../Database/ps2_cp47_all_12000.hkl')
print template.keys()

data = {}

data['transfer_times']        = np.array(template['times'])
data['transfer_efficiencies'] = np.array(template['efficiencies'])
data['hamiltonians']          = np.array(template['hamiltonians'])

for i in range(12000):
	for j in range(8):
		data['hamiltonians'][i][j, j] += template['meanEnergies'][i]

data['units'] = {'transfer_times': 'ps', 
				 'transfer_efficiencies': 'unitless (bound between 0 and 1)',
				 'hamiltonians': 'cm^-1'}

data['spectral densities'] = {'lambda': '35 cm^-1',
							  'nu^-1': '50 fs'}

data['donor']    = 'site 0'
data['acceptor'] = 'site 3'

hickle.dump(data, 'cp47_dataset.hkl')

print data['hamiltonians'][0]


#print data['times'][:10]
#print data['efficiencies'][:10]
#print data['hamiltonians'][:2]
print np.array(template['meanEnergies']).shape

print data.keys()
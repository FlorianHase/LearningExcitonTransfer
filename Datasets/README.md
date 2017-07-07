
# Exciton energy transfer datasets

We report the results of our exciton dynamics calculations with the HEOM method and the secular Redfield approach on the four datasets presented in the study. Excited state energies and inter-site couplings were sampled uniformly from the ranges in reported in the table below.


| Reference | Sites | Excited state energies [cm<sup>-1</sup>] | Inter-site couplings [cm<sup>-1</sup>] | 
| --------- | ----- | ---------------------------------------- | -------------------------------------- |  
| FMO       |    8  |      12000 ... 12800                     |   -100 ... 100                         | 
| RC        |    8  |      14800 ... 15000                     |    -50 ... 50                          | 
| CP43      |   21  |      14800 ... 15100                     |    -60 ... 60                          | 
| CP47      |   24  |      14500 ... 15300                     |   -100 ... 100                         | 


Exciton energy transfer times and efficiencies were computed from population dynamics simulations starting from a fully populated site 0. For all Hamiltonians we assumed identical Drude-Lorentz spectral densities and defined site 3 as the target site. Details on the simulations procedure can be found in the paper ...

## How to access the datasets

We provide a script `load_dataset.py` which illustrates how to access the datasets. To run the script, simply type 
```bash
	python load_dataset.py dataset.hkl
```
to load a dataset file called `dataset.hkl`. The dataset contained within the file will then be loaded as a python dictionary. All of our datasets uploaded here contain the information listed in the table below.

| Key                    | Variable type | Contained data                        | 
| ---------------------- | ------------- | ------------------------------------- |
| `acceptor`             | `string`      | target site                           | 
| `donor`                | `string`      | initial site                          | 
| `hamiltonians`         | `numpy array` | exciton hamiltonians [cm<sup>-1</sup> | 
| `spectral densities`   | `dictionary`  | spectral density paramters            |
| `transfer_efficiences` | `numpy array` | exciton transfer efficiencies         |  
| `transfer_times`       | `numpy array` | exciton transfer times [ps]           |
|  units                 | `dictionary`  | physical units for stored quantities  | 


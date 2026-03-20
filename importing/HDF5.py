"""
HDF5 files
- Hierarchical Data Format version 5
- Standard for storing large quanties of numerical data
- Datasets Can be hundreds of gigabyte or terabytes

"""

import h5py
import numpy as np
filename = 'H-H1_LOSC_4_Va-890230123002-323.hdf5'

data = h5py.File(filename, 'r') # 'r' is to read only

print(type(data))


## STRUCTURE OF HDF5
"""HDF5 structure can be explored like we do for Python Dictionary using the method keys"""
"""
    - HDF5 file can be accessed with theirs just like we do in Dictionary
    - HDF5 has 3 main keys 
        - meta: This contains the meta-data for the HDF5 file
        - Quality: This refers to data qualituy. The main itme here is a 1HZ time series describing the data quality
        - Strain: Strain data from the interferometer

"""
# HOW TO DISPLAY HDF5 file Meta-Data

for key in data['meta'].keys():
    print(key)
    print(np.array(data['meta']['mete-data']), np.array(data['meta']['meta-data']))

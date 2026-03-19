"""
HDF5 files
- Hierarchical Data Format version 5
- Standard for storing large quanties of numerical data
- Datasets Can be hundreds of gigabyte or terabytes

"""

import h5py

filename = 'H-H1_LOSC_4_Va-890230123002-323.hdf5'

data = h5py.File(filename, 'r') # 'r' is to read only

print(type(data))


## STRUCTURE OF HDF5
"""HDF5 structure can be explored like we do for Python Dictionary using the method keys"""

for key in data.key():
    print(key)
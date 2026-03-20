"""
MATLAB: Matrix Laboratory, its a numerical computing environment
        that is an industry standard in the discipline of engineering and science
        It is powerful for linear algebra and matrix capabilities
"""

import scipy.io as matlab

filename = 'workspace.mat'

mat = matlab.loadmat(filename)

print(type(mat)) # <class 'dict>

"""
-  keys = MATLAB variable name
-  values = objects assigned to variables 
"""


## EXAMPLE 2

# Import package
import scipy.io
import numpy as np
# Load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')

# Print the datatype type of mat
print(type(mat))

for key in mat.keys():
    print(mat[key])
    print(np.array(mat[key]))
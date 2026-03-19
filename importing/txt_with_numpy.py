# WHAT FLAT FILES are basic text file containing records, i.e 
    ## table data without a structured relationships
    # Cotains Record: row of fields or attributes


# HOW TO IMPORT FILE FROM A FLAT FILE (.csv or .txt)
    ## There are 2 main packages for importing FLAT FILES : NumPy, Pandas
        ## NumPy: use this if the Flat file consist entirely of numbers
        ## pandas: use this if we wanna store the data in a dataframe


## IMPORTING .txt FLAT FILE  using NumPy

import numpy as np

filename = 'MNIST.txt'

data = np.loadtxt(filename, delimiter=', ', skiprows=1, usecols=[0,2])

print(data)

## delimiter=', ' This use comma delimeter
## skiprows=1 : This is use skip the first ROW in the case the data has a HEADER container text
## ecols=[0,2] : Only import the  first and third columns
## dtype=str : This ensures that all enrties are imported as strings


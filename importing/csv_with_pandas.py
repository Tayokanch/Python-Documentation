# Pandas are used for import TWO-dimensional Labeled data structures
# Data structure with column of potentailly different types
# Its used for Manipulating, Slicing, Reshaping, Groupby, Join, Merge
# Perform Statistics
# Work with Time Series

# DataFrame: This is the most data structure relevant to the data manipulation and analysis workflow that pandas offers


import pandas as pd

filename = 'winequality.csv'

data = pd.read_csv(filename)

data.head() # To check the first 5 Rows of the data with the Header

data.to_numpy() # To covert the data to a NumPy Array
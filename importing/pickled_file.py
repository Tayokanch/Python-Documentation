# USES OF PICKLE

# For Converting  Python objects (like dictionaries, lists, models, etc.) into a binary (computer readable format) → this is called pickling
# For Converting that binary data back into the original Python object → unpickling

import pickle

with open('pickled_fruit.pkl', 'rb') as file: ##'rb': ReadOnly and Binary file(Computer readable only)
    data = pickle.load(file)
    print(data)
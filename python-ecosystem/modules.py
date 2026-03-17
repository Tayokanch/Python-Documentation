## What are modules

# Modules are Python Scripts, meaning they are files ending with `.py` extension that container reuseable code

# Modules contain functions and attributes

# There are around 200 built-in moudles in Python

# Example:

# - OS module : This lets us interact with our Operating System
import os 

wrk_dir = os.getcwd() # get the current working directory
print( "The current working Dir is:",wrk_dir) # This is to print the current working directory


os.environ # to get information about our environment variable



# - STRING module
# This can be used for text validation, for checking of a string contains letters, numbers, or special characters

import string

a_z_lower_case = string.ascii_lowercase # This returns abcdefghijklmnopqrstuvwxyz

_0_9_ = string.digits # This returns 0123456789

punctuation = string.punctuation # This returns special characters


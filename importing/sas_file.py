# How to Import SAS files

"""SAS and Stata Files"""

"""SAS: Statistical: Analysis System"""

"""Stata: Statistical + Data """

import pandas as pd

from sas7bdat import SAS7BDAT

with SAS7BDAT('urbanpop.sas7bdat') as file:
    df_sas = file.to_data_fram()


## STATA files

import pandas as pd

data = pd.read_stata('urbanpop.dta')


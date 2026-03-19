import pandas as pd

file = 'urbanpop.xlsx'

data = pd.ExcelFile(file)

print(data.sheet_names) ##.sheet_names : To determine the sheets we have in the file ['Sales', 'Inventory', 'Summary']

df1 = data.parse('string') #sheet_name as as string
df2 = data.parse(0) ## sheet index, as a float


## Example 2

xls = pd.ExcelFile(file)
# Parse the first sheet and rename the columns: df1
df1 = xls.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
df2 = xls.parse(1, usecols=[0], skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())


"""
Key Points

- skiprows=[0] → skips the first row of the sheet.
- names=[...] → sets column names for the resulting DataFrame.
- usecols=[0] → selects only the first column (index 0).
- Both skiprows and names must be lists, not single values.

"""
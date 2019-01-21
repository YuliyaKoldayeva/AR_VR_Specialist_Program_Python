import pandas as pd

original_dataframe = pd.read_csv("7_-_100_Sales_Records.csv") # Read the data from 7_-_100_Sales_Records.csv

print("\n\tCheck the dimensions of the data set (ROWS, COLUMNS): ", original_dataframe.shape)

print("\n\tPrint column names and data types ('object' means general, non numeric data type, i.e. string or mixed)\n")
print(original_dataframe.dtypes)

print("\n\tStatistics on any column of interest containing numeric data \n")
print(original_dataframe["Units Sold"].describe())

print("\n\tPrint the value frequencies of all records in Region column\n")
print(original_dataframe["Region"].value_counts())

print(original_dataframe['Order Date'].head())
print("Change 'Order Date' format from string to datetime format: ")
original_dataframe['Order Date Formatted'] = pd.to_datetime(original_dataframe['Order Date'], errors='coerce', yearfirst=True,format='%m/%d/%Y')
print(original_dataframe['Order Date Formatted'].head())

print("\n\tCheck if the formatting was successful\n")
print(original_dataframe['Order Date Formatted'].dtypes)

print(original_dataframe['Order Date Formatted'])
print(original_dataframe['Order Date Formatted'].isnull().value_counts())
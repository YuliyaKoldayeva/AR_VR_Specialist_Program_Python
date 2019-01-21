import pandas as pd

original_dataframe = pd.read_csv("7_-_100_Sales_Records.csv") # Read the data from 7_-_100_Sales_Records.csv

print("\n\tNumber of records from Europe: ", (original_dataframe["Region"]=="Europe").sum())

print("\n\tThe total of units sold: ", original_dataframe["Units Sold"].sum())

print("\n\tThe list of item types without duplicates:\n")
print(original_dataframe["Item Type"].unique().tolist())

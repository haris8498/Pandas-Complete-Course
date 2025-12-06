import pandas as pd

var = pd.read_csv("people-15.csv")
print(var)


# To drop null values
# This drop is along rows
print(var.dropna()) # It will skip the rows which have null values


# If we want to drop along columns
print(var.dropna(axis=1))


# If we want to delete complete null row
# We can use how = any or all
print(var.dropna(how="any"))  # any will delete row if any one value is null 

print(var.dropna(how="all"))  # all will delete row if all values are null


# To remove null value based on particular column
# The use of submit parameter thresh

print(var.dropna(subset=["Phone"]))


# Inplace
var.dropna(inplace=True)
print(var)


# The use of thresh ( jis my single null value hy usy drop kary ga)
var.dropna(thresh=1)
print(var)





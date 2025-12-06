import pandas as pd
var = pd.read_csv("people-15.csv")
print(var)


# It will replace all the occurrences of 1 with 22
var.replace(to_replace=1.0,value=22)

# To replace name
print(var.replace(to_replace="Shelby",value="Jonathan"))



# To replace multiple values
print(var.replace(to_replace=[1.0, "Shelby"], value=[22, "Jonathan"]))


# To replace Alpha numeric
print(var.replace("[A-Za-z]","python",regex=True))


# To replace using a dictionary
print(var.replace({"Phone":"[A-Za-z]"},22,regex=True))

# Method parameter
print(var.replace(pd.NA,method="bfill"))



# Limit parameter
print(var.replace(pd.NA,method="ffill",limit=1))


# Use of inplace (Will modify the original dataframe)
var.replace(pd.NA,method="ffill",limit=1,inplace=True)
print(var)
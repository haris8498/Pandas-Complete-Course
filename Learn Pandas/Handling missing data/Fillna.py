# +++++++++++++++++++++++++++++++++++++++ 
# The use of fillna
# ++++++++++++++++++++++++++++++++++++++
import pandas as pd
var=pd.read_csv("people-15.csv")


print(var.fillna("python")) 


# To fill data in particular column 
print(var.fillna({"Phone":000000000,"Name":"Unknown" , "User Id": "Unknown"}))


# To fill with backward value
print(var.fillna(method="bfill"))

# To fill with forward value
print(var.fillna(method="ffill"))


# To fill along a particular axis
print(var.fillna(method="ffill", axis=1))

print(var.fillna(method="ffill", axis=1))


# The use of implace
print(var.fillna(12,inplace=True))


# The use of limit parameter
print(var.fillna("Python",limit=1))
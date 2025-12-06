import pandas as pd
var = pd.read_csv("people-15.csv")
print(var)

print(var.interpolate()) # Works only for numerical data

#Method parameter
print(var.interpolate(method="linear",axis=0))  # linear is default method


# Use of limit
print(var.interpolate(limit=7))  # It will fill only 7 consecutive NaN values


# The use of limit_direction 
print(var.interpolate(limit_direction="forward"))  # It will fill NaN values in forward direction only
print(var.interpolate(limit_direction="backward"))  # It will fill NaN values in backward direction only
print(var.interpolate(limit_direction="both"))  # It will fill NaN values in both directions



# Use of limit Area
print(var.interpolate(limit_area="inside"))  # It will fill NaN values which are in between two values
print(var.interpolate(limit_area="outside"))  # It will fill NaN values which are at

# Use of inplace
var.interpolate(inplace=True)
print(var)
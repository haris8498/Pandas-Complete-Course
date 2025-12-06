import pandas as pd

var=pd.DataFrame({
    "name":["Alice","Bob","Charlie","David","Eva","Frank","Grace","Charlie","David","Eva","Frank",],
    "city":["New York","Los Angeles","New York","Chicago","Los Angeles","Chicago","New York","Los Angeles","Chicago","New York","Los Angeles"],
    "age":[25,30,35,40,45,50,55,35,40,45,50],
})

print(var)


var_new = var.groupby("name")   # Grouping by name column
for name,group in var_new:
    print(name)
    print(group)

# To get particular group
print(var_new.get_group("Charlie"))


# How to find means maximum and minimum of groups
print(var_new.mean())  # Mean of age for each name
print(var_new.max())   # Maximum age for each name
print(var_new.min())   # Minimum age for each name
print(var_new.size())  # Size of each group
print(var_new.describe())  # Statistical description of each group
print(var_new.count())  # Count of non null values in each group
print(var_new.sum())    # Sum of age for each name
print(var_new.std())    # Standard deviation of age for each name
print(var_new.var())    # Variance of age for each name
print(var_new.first())  # First entry of each group
print(var_new.last())   # Last entry of each group
print(var_new.nth(2))   # Nth entry of each group (2nd entry here)
print(var_new.head(1))  # First n entries of each group (1 here)
print(var_new.tail(1))  # Last n entries of each group (1 here)
import pandas as pd

csv1=pd.read_csv("people-15.csv")
print(csv1)


# To get index
print(csv1.Index)
print(type(csv1.Index))


# To get column names
print(csv1.columns)


# Use of describe() function

print(csv1.describe())


csv1.head()  # by default it will give first 5 rows
print(csv1.head())

csv1.tail(3)  # it will give last 3 rows
print(csv1.tail(3))


# To get data to a particular index
print(csv1[:2])  # it will give data from 0 to 1 index that is first two rows




# To change index to array form
print(csv1.index.array)


# To change columns to array form
print(csv1.columns.array)


# To convert it to numpy array
print(csv1.to_numpy())


# To sort data in descending order 
print(csv1.sort_index(ascending =False,axis=0))



# To change data
csv1.loc[0,"Index"] = "Python"
print(csv1)



# To get a particular data
print(csv1.loc[[2,3],["Email"]])


print(csv1.loc[:,["First Name","Last Name"]])




# The use of iloc function
print(csv1.iloc[0,2])



# To drop a column 
csv1_drop=csv1.drop("Index",axis=1)  # axis=1 for column and axis=0 for row
print(csv1_drop)

# To drop a row
csv1_drop_row=csv1.drop(0,axis=0)
print(csv1_drop_row)
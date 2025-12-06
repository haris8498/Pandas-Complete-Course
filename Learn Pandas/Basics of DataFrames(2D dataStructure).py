import pandas as pd 

# Using list
l=[11,2,3,5,6,4,2,3,4,3,33]
var=pd.DataFrame(l)  # Create a Pandas DataFrame from the list l DataFrames are 2D...
print(var)
print(type(var))  # ...and have their own data type


# Making dataFrame from dictionary
dic={
    "name":["Mahnoor","Ayesha","Fatima","Ali"],
    "age":[20,21,19,22],
    "city":["Karachi","Lahore","Islamabad","Quetta"],
}
data=pd.DataFrame(dic)
print(data)
print(type(data))


d={
    "a":[1,2,3,4],
    "b":[5,6,7,8],
    "c":[9,10,11,12]
}
df=pd.DataFrame(d)
print(df)

# To get only one column
df1=pd.DataFrame(d,columns=["b","c"],index=["row1","row2","row3","row4"])  
print(df1)


# To get sepecific value 
print(df1["c"]["row3"])  # 11
print(df1["b"]["row3"])


list_1=[[2,3,4,1,2,3,4],[3,2,3,7,4,6,1]]
df2=pd.DataFrame(list_1,columns=["a","b","c","d","e","f","g"],index=["row1","row2"])
print(df2)


# Give series in dataFrame
sr={
    "a":pd.Series([1,2,3,4]),
    "b":pd.Series([5,6,7,8]),
    "c":pd.Series([9,10,11,12])
}
df3=pd.DataFrame(sr)
print(df3)
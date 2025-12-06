import pandas as pd

var1=pd.DataFrame({
    "A":[1,2,3],
    "B":[4,5,6]
})
var2=pd.DataFrame({
    "A":[1,2,3],
    "C":[10,11,12]
})


# Merging two dataframes
print(pd.merge(var1,var2))  # It will merge on common columns by default


# The use of on parameter
print(pd.merge(var2,var1,on="A"))  # Merging on particular common column 



# The use of how parameter
print(pd.merge(var1,var2,how="inner"))  # inner is default method
print(pd.merge(var1,var2,how="left"))  # left will keep all values of left dataframe
print(pd.merge(var1,var2,how="right"))  # right will keep all values of right dataframe
print(pd.merge(var1,var2,how="outer"))  # outer will keep all values



# INdicator parameter
print(pd.merge(var1,var2,how="outer",indicator=True))  # It will show from which dataframe the row is coming


var3=pd.DataFrame({
    "A":[1,2,3,4],
    "B":[5,6,7,8]
})
var4=pd.DataFrame({
    "A":[3,4,5,6],
    "C":[10,11,12,13]
})

print(pd.merge(var3,var4,left_index=True,right_index=True,how="outer"))  # Merging on index


# To change Name
print(pd.merge(var3,var4,how="outer",left_index=True,right_index=True,suffixes=("_left","_right")))  # It will add suffix to same column names




# +++++++++++++++++++++++++++
# Concatenation of dataframes
# +++++++++++++++++++++++++++

sr1=pd.Series([1,2,3,4])
sr2=pd.Series([5,6,7,8])
print(pd.concat([sr1,sr2]))  # Concatenation along rows


# Concatenation of dataframes 
df1=pd.DataFrame({
    "A":[1,2,3],
    "B":[4,5,6]
})
df2=pd.DataFrame({
    "A":[7,8,9],
    "B":[10,11,12]
})
print(pd.concat([df1,df2]))  # Concatenation along rows
print(pd.concat([df1,df2],axis=1))  # Concatenation along columns



# Use of join parameter
pd.concat([df1,df2],axis=1,join="inner")  # inner is default method



# The use of key 
print(pd.concat([df1,df2],keys=["First","Second"]))  # It will create multi index

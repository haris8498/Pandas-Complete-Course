import pandas as pd
var1=pd.DataFrame(
    {
        "A":[1,2,3],
        "B":[4,5,6],
         "index":["a","b","c"]
    }
)
var2=pd.DataFrame(
    {
        "A":[7,8,9],
        "B":[10,11,12],
         "index":["a","b","c"]
    }

)

print(var1.join(var2,lsuffix="_left",rsuffix="_right"))  # Joining on index by default

var2.join(var1,lsuffix="_left",rsuffix="_right")  

var1.join(var2,lsuffix="_left",rsuffix="_right", how="right")  # right will keep all values of right dataframe
var1.join(var2,lsuffix="_left",rsuffix="_right", how="left")  # left will keep all values of left dataframe
var1.join(var2,lsuffix="_left",rsuffix="_right", how="outer")  # outer will keep all values
var1.join(var2,lsuffix="_left",rsuffix="_right", how="inner")  # inner is default method







# ++++++++++++++++++++++++++++++
# Appending of dataframes
# ++++++++++++++++++++++++++++++

var3=pd.DataFrame(
    {
        "A":[1,2,3],
        "B":[4,5,6],
         "index":["a","b","c"]
    }
)
var4=pd.DataFrame(
    {
        "A":[7,8,9],
        "B":[10,11,12],
         "index":["a","b","c"]
    }

)

result = var3._append(var4, ignore_index=True)  # Note the underscore
print(result)
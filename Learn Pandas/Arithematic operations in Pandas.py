import pandas as pd
var = pd.DataFrame({
    "A":[2,3,5,1,2,3],
    "B":[5,6,7,8,5,4],
})
print(var)

# In column C i want sum of A and B
var["C"]=var["A"]+var["B"]
print(var)

# In column D i want difference of B and A
var["D"]=var["B"]-var["A"]
print(var)







# Logical operators

var1=pd.DataFrame({
    "X":[10,20,30,40,50],
    "Y":[5,15,25,35,45],
})
print(var1)


var1["Z"]=var1["X"]>20
var1["Python"]=var1["Y"]<=50
print(var1)


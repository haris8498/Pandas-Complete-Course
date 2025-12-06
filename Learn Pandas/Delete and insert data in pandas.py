import pandas as pd
var=pd.DataFrame(
    {
        "A":[2,3,5,1,2,3],
        "B":[3,8,3,4,2,8],
    }
)

print(var)


# Insert data in new column C as sum of A and B


# 1 is the location at which i have to insert the data
# C is new column name 
# var["A"] + var["B"] is new data in the column
var.insert(1,"C",var["A"]+var["B"])  # Unserting data length should be equal
print(var)

# var.insert(1,"D",[3,4,5,3])  This will through error as length of data is not equal to other columns data
# print(var)



# Copy limited data in new column 
# We want data upto three rows of A we will use slicing 
var["Python"]=var["A"][:3]
print(var)



# How to delete 

var1=pd.DataFrame({
    "X":[10,20,30,40,50],
    "Y":[5,15,25,35,45],
    "Z":[8,26,3,4,2]
})
print(var1)

# Deleting column Y

# 1st method
var2=var1.pop("Y")
print(var1)
print(var2)

#Second method
del var1["X"]
print(var1)
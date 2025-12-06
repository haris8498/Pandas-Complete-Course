import pandas as pd

var = pd.DataFrame(
    {
        "A":["foo","bar","foo","bar","foo","bar","foo","foo"],
        "B":["one","one","two","three","two","two","one","three"],
        "C":[1,2,3,4,5,6,7,8],
        "D":[10,20,30,40,50,60,70,80],
    })
print(var)



# Melt function is used to reshape the dataframe
print(pd.melt(var))  # It will melt all columns into two columns variable and value



# Make id_vars parameter
print(pd.melt(var,id_vars=["A"]))


# To give name to variable and value columns
print(pd.melt(var,id_vars=["A"],var_name="Variable_Name",value_name="Value_Name"))



# ++++++++++++++++++++++++++
# Pivot table function
# ++++++++++++++++++++++++++

var1 = pd.DataFrame(
    {
        "st_name":["Mahnoor","Adeel","Ayesha","Fatima"]
        ,"subject":["Math","Physics","Chemistry","Science"]
        ,"score":[90,80,85,95]
    })
print(var1)


print(var1.pivot(index="st_name",columns="subject"))

# To get particular column
print(var1.pivot(index="st_name",columns="subject",values="subject"))  


# Pivot table with aggregation

print(var1.pivot_table(index="st_name",columns="subject",values="score",aggfunc="sum"))  # sum is default function

print(var1.pivot_table(index="st_name",columns="subject",values="score",aggfunc="mean"))  # sum is default function


# Margin parameter
print(var1.pivot_table(index="st_name",columns="subject",values="score",aggfunc="mean",margins=True))  # It will give total mean score
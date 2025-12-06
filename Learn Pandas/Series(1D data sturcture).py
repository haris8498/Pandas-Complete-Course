import pandas as pd

# Using list

x = [2,3,73,71,29,73,46,74,85]

var = pd.Series(x)  # Create a Pandas Series from the list x Series are 1D...

print(var)
print(type(var))  # ...and have their own data type
print(var[0])  # Accessing the first element of the Series  





# Using dictionary  

dic = {
    "name":["Mahnoor,Ayesha,Fatima,Ali"],
    "age":[20,21,19,22],
    "city":["Karachi","Lahore","Islamabad","Quetta"],
}
data=pd.Series(dic)
print(data)




# Making series from single data 
s=pd.Series(12)
print(s)
print(type(s))



# Making multiple blocks of single data
s1=pd.Series(12,index=[0,2,3,1,23,4])
print(s1)



print("Sum of two series")
# Addition of two series
s3=s+s1
print(s3)
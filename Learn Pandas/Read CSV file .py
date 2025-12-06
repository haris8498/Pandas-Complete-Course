import pandas as pd

csv1=pd.read_csv("people-100000.csv")
print(csv1)


# To get rows

csv2=pd.read_csv("people-100000.csv",nrows=5)
print(csv2)
print(type(csv2))


# To get a particular column

csv3=pd.read_csv("people-100000.csv",usecols=["First Name"] )
print(csv3)


# To get multiple columns
csv4=pd.read_csv("people-100000.csv",usecols=["First Name","Last Name","Email"] )
print(csv4)





# To get specific column by column number
csv5 = pd.read_csv("people-100000.csv",usecols=[0,1,3])  # 0 for first column ,1 for second column and 3 for fourth column
print(csv5)





# To skip a particular row
csv6 = pd.read_csv("people-100000.csv",skiprows=[1,2])  
print(csv6)




# For index call
csv7 = pd.read_csv("people-100000.csv",index_col="First Name")
print(csv7)



# To make files header
csv8 = pd.read_csv("people-100000.csv",header=2)
print(csv8)



# To change heading 
csv9 = pd.read_csv("people-100000.csv",names=["A","B","C","D","E","F","G","H","I","J"])
print(csv9)



# To covert integer type data to float 
csv10=pd.read_csv("people-100000.csv",dtype={"Index": float})

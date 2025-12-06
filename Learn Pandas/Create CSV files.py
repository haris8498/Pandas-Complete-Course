# CSV is comma seperated value
import pandas as pd 

dis={
    "Name":["Ali","Ayesha","Fatima","Mahnoor"],
    "Age":[20,21,19,22],
    "City":["Karachi","Lahore","Islamabad","Quetta"],
}

var=pd.DataFrame(dis)
print(var)


# To create CSV file in current directory

var.to_csv("data.csv")  


# To remove index column from csv file
var.to_csv("data_no_index.csv",index=False)


# To change header data 

var.to_csv("data_new_header.csv",header=["N","A","C"],index=False)
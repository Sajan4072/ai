## for json
import panda as pd 
hiking=pd.read_json("datasets/hiking.json")
print(hiking.head())


#for colums attribute colum attribute
print(hiking.colums)

# see the datatypes with dtype attribute 
print(hiking.dtypes)

#generate basic stats like mean,standard deviation and quartiles using describe method 

print(wine.describe())  # here wine is same as hiking 



#one of the step to preprocess is to remove missing data 
#there are lot of ways to deal with it here for instance removing colums or rows 

# drop all rows that contain missing values with dropna 
print(df)
print(df.dropna())


#drop sppecific rows with passing index to drop func
print(df.drop([1,2,3]))

#drop a colum if all or most of its  value are missing  with drop fun
print(df.drop("A",axis=1))  #here a is name of colum axis=1 inorder to designate we want to drop a column


#drop rows where data is missing at particular column with the help of boolean indexing 
# it is more like filtering 

print(df[df["B"]==7])  #output only rows which have 7 in B colum



#look how many null values are there in colum b using isnull funn


print(df["B"].isnull().sum)  #gives 2 since there are 2 null values in B

# to filter those out we can use notnutll method on columb B as boolean index
print(df[df["B"].notnutll()])



# we can also do something like this 
movies[movies.duration >=200] # here movies is something like hiking
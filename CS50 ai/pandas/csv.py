
To read the CSV file using pandas, we can use the read_csv() function.

import pandas as pd
pd.read_csv("people.csv")


To write to a CSV file, we need to call the to_csv() function of a DataFrame.
#creating a data frame 
df= pd.DataFrame([['jack',24],['rose',22]],columns=['name','age'])


#writing data frame to a csv file 
df.to_csv('title.csv')



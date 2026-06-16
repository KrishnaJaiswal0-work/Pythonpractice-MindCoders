# pandas start from here 
# import numpy as np
import pandas as pd 

df = pd.DataFrame({
    "name"    : ["sonu",'monu','tinku',"pinku","tillu"],
    "age"     : [20,32,12,45,18],
    'city'    : ['indore', 'bhopal', 'betul', 'bhopal', 'betul'], 
    "marks_1" : [78,99,78,90,96] ,  
    "marks_2" : [89,67,79,97,42]
})



# print(arr)
# print(arr.shape)
# print(arr.head(3))
# print(arr.dtypes)
# print(arr.describe())

# jrr = arr.to_numpy()
# print(jrr)
# print(np.isnan(jrr["marks_2"]))


#  Select column
print("df['name']: \n", df['name'])
print(df[['name','marks_1']])


#Filter rows 
print(df[df['marks_1'] >= 85])
print(df[df['city'] == 'bhopal'])

print()
print( df[ (df['marks_1']>=70) & (df['city']=='indore') ] )   

def get_grade(x):
    if x >= 90:
        return 'A'
    elif x >= 75:
        return 'B'
    else:
        return 'C'
    
df['grade'] = df['marks_1'].apply(get_grade)
print(df['grade'])
print("----------------")
print(df)


# GroupBy - Like Excel pivot
city_avg = df.groupby('city')['marks_2'].mean()
print(city_avg)


# Read real csv file 
df2 = pd.read_csv('FileHandling/students.csv')
#cleaning


df2.to_csv('Libraries/Pandas/clean_output.csv', index=False)  # Save
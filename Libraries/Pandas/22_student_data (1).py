import pandas as pd

data = {
    'Name':  ['Pankaj','Alia','Ram','Kajal','Aman'],
    'Age':  [21,19,22,20,19],
    'Marks':  [85,65,75,90,56],
    'City':  ['Rom','Berlin','Tokyo','Moscow','Landon']
}

df = pd.DataFrame(data)
print(df)

print(df.shape)          #(5,4) - 5 rows , 4 columns
print(df.head(2))        # First 3 Row
print(df.dtypes)         # Data type of each column
print(df.describe())     # Statistical summary


#  Select column
print("df['Name']: \n", df['Name'])
print(df[['Name','Marks']])


#Filter rows 
print(df[df['Marks'] >= 85])
print(df[df['City'] == 'Berlin'])

print()
print( df[ (df['Marks']>=70) & (df['City']=='Landon') ] )   

def get_grade(x):
    if x >= 90:
        return 'A'
    elif x >= 75:
        return 'B'
    else:
        return 'C'
    
df['Grade'] = df['Marks'].apply(get_grade)
print(df['Grade'])
print("----------------")
print(df)


# GroupBy - Like Excel pivot
city_avg = df.groupby('City')['Marks'].mean()
print(city_avg)


# Read real csv file 
df2 = pd.read_csv('FileHandling/students.csv')
#cleaning


df2.to_csv('Libraries/Pandas/clean_output.csv', index=False)  # Save
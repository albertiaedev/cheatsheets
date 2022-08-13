#PANDAS CHEATSHEET

#Import the library
import pandas as pd

#Create a DataFrame
df = pd.DataFrame(
{‘Name_Column’ : [],
  ‘Name_Column’ : [],
           ………
  ‘Name_Column’ : [],
  index = []})

#Show the complete DataFrame in screen
print(df)

#Count the number of rows and columns
print(df.shape)

#Show index
print(df.index)

#Show the name of the columns
print(df.columns)

#Show the data type of each column
print(df.dtype)

#Show the top rows of the DataFrame
print(df.head())

#Show the bottom rows of the DataFrame
print(df.tail())

#Do a quick statistical analysis
print(df.describe())

#Obtain detailed info of the DataFrame
print(df.info())

#Do a statistical analysis for a specific value
print(‘Name_Stat’,df,[‘Name_Column’], mean/std/min/max())

#Delete columns with empty values
var = df[df[‘Name_Column’] != ‘N/A’]
print(var)

#Delete rows with empty values
df = pd.DataFrame(df)
df.dropna(how=‘any’,inplace=True)

#Replace empty values
df = pd.DataFrame(df)
df.fillna(‘0’,inplace=True)

#Read CSV
df = pd.read_csv(‘name.csv’)

#Read EXCEL
df = pd.read_excel(‘name.xlsx’)

#Read JSON
df = pd.read_json(‘name.json’)

#Read TXT
df = pd.read_table(‘name.txt’)

#Read HTML
df = pd.read_html(‘name.html’)

#Read SQL
df = pd.read_sql(‘name.db’)

#Write CSV
df = pd.to_csv(‘name.csv’)

#Write EXCEL
df = pd.to_excel(‘name.xlsx’)

#Write JSON
df = pd.to_json(‘name.json’)

#Write TXT
df = pd.to_table(‘name.txt’)

#Write HTML
df = pd.to_html(‘name.html’)

#Write SQL
df = pd.to_sql(‘name.db’)

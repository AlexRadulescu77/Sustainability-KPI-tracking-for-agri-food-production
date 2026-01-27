import pandas as pd
import sqlite3


df = pd.read_csv(r'C:/Users/alexr/Desktop/Carbon data/Datasets/clean_data.csv')

#  Connect to SQL database
db_path = r'C:/Users/alexr/Desktop/Carbon data/sustainability.db'
connection = sqlite3.connect(db_path)

# Upload data to SQL table
df.to_sql('clean_data', connection, if_exists='replace', index=False)

connection.close()

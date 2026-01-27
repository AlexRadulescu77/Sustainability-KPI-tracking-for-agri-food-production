import pandas as pd
import sqlite3

# Step 1: Read cleaned data
print("Loading cleaned data...")
df = pd.read_csv(r'C:/Users/alexr/Desktop/Carbon data/Datasets/clean_data.csv')

# Step 2: Connect to SQLite database (creates it if it doesn't exist)
print("\nConnecting to database...")
db_path = r'C:/Users/alexr/Desktop/Carbon data/sustainability.db'
connection = sqlite3.connect(db_path)

# Step 3: Upload data to SQL table
print("Uploading data to SQL table...")
df.to_sql('clean_data', connection, if_exists='replace', index=False)

# Step 4: Run a test query
print("\n✅ Testing database connection...")
query = """
SELECT Product, Year, AVG(CO2_per_unit) as Avg_CO2
FROM sustainability_data
GROUP BY Product, Year
"""
result = pd.read_sql(query, connection)
print(result.head(10))

# Step 5: Close connection
connection.close()
print("\n✅ Data successfully uploaded to SQL database!")

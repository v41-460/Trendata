# Module Imports
import mariadb
import sys
import pandas as pd
from sqlalchemy import create_engine


#read xls data into dataframe
df = pd.read_excel('zip_code_database.xls')

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root", #change to your username
        password="pass", #change 
        host="localhost",
        port=3306,
        database="classicmodels"
    )

#error message
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

#Convert DF into mariaDB format
engine = create_engine('mysql+mysqlconnector://root:pass@127.0.0.1/classicmodels') #change root:pass to your username:password
df.to_sql(name='zip', con=engine, if_exists='replace', index=False)


#display table
all_tables = pd.read_sql("show tables",conn)
print(all_tables)


# Get Cursor
cur = conn.cursor()

#Query, can change if need to
query = f"Select * From zip"

cur.execute(query)

rows = cur.fetchall()
conn.close()
  
for row in rows :
    print(row)

from pydoc import doc
import pyodbc
from numpy import random
import datetime
# Trusted Connection to Named Instance
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=SERVERNAME\SQLEXPRESS;DATABASE= DATABASENAME;Trusted_Connection=yes;')
print(connection)
cursor=connection.cursor()
print(cursor)

for i in range(0, 1000):
    city = "Gurgaon"
    company = random.choice(["Collabera","Rolta","Tech Mahindra","Nagarro","Genpact","ThoughtWorks","HCL Technologies","SAP","HP","TCS",], size=(1))
    docs = datetime.datetime.now()
    dom = datetime.datetime.now()

    cursor.execute("INSERT INTO [dbo].[car] VALUES (?, ?, ?, ?)", (city,company[0],docs, dom))
    cursor.commit()
    print("Done - ", i)







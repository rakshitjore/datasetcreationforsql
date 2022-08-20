from pydoc import doc
import pyodbc
from numpy import random
import datetime
# Trusted Connection to Named Instance
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER= ENTERSERVERNAME\SQLEXPRESS;DATABASE= ENTER DATABASE NAME;Trusted_Connection=yes;')
print(connection)
cursor=connection.cursor()
print(cursor)

for i in range(0, 10000):
    city = random.choice(["Indore",  "Bhopal", "Mumbai", "Bengaluru","Pune",], p=[0.1,0.05,0.25,0.3,0.3,], size=(1))
    city_development_index = random.choice(["0.92",  "0.776", "0.624", "0.789","0.767",], p=[0.1,0.05,0.25,0.3,0.3,], size=(1))
    gender = random.choice(["male","female",], p=[0.65,0.35], size=(1))
    relevant_experience = random.choice(["15",  "1", "5", "20","11",], p=[0.1,0.05,0.25,0.3,0.3,], size=(1))
    enrolled_university = random.choice(["full time",  "part time", "not enrolled",], p=[0.6,0.35,0.05,], size=(1))
    company_size = random.choice(["20",  "10", "1000", "50","500",], p=[0.1,0.05,0.25,0.3,0.3,], size=(1))
    education = random.choice(["Masters",  "Graduate", "High School",], p=[0.6,0.35,0.05,], size=(1))
    company_type = random.choice(["Pvt Ltd","Funded Startup",], p=[0.6,0.4,], size=(1))
    reason_switch = random.choice(["less salary","work life balance",], p=[0.6,0.4,], size=(1))
    skill_set = random.choice(["python",  "java", "c++", "sql","c",], p=[0.1,0.05,0.25,0.3,0.3,], size=(1))
    docs = datetime.datetime.now()
    dom = datetime.datetime.now()

    cursor.execute("INSERT INTO [dbo].[Employee] VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (city[0],city_development_index[0],gender[0],relevant_experience[0],enrolled_university[0],company_size[0],education[0],company_type[0],reason_switch[0],skill_set[0], docs, dom))
    #cursor.execute("INSERT INTO [dbo].[Employee] ([city],[city_development_index],[gender],[relevant_experience],[enrolled_university],[company_size],[education],[company_type],[reason_switch],[skill_set],[doc],[dom]) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (city,city_development_index,gender,relevant_experience,enrolled_university,company_size,education,company_type,reason_switch,skill_set,doc,dom))

    cursor.commit()
    print("Done - ", i)

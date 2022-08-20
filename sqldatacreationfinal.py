from pydoc import doc
import pyodbc
from numpy import random
import datetime
# Trusted Connection to Named Instance
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=Servername\SQLEXPRESS;DATABASE=databasename;Trusted_Connection=yes;')
print(connection)
cursor=connection.cursor()
print(cursor)

for i in range(0, 10000):
    city = random.choice(["Ahmedabad","Bangalore","Vizag","Chennai","Coimbatore","Delhi","Dewas","Gurgaon","Guwahati","Hyderabad","Indore","Jamshedpur","Kochi","Kolkata","Lucknow","Mangalore","Mumbai","Nagpur","Noida","Patna","Pune","Vadodara","Varanasi",], size=(1))
    city_development_index = random.choice(["0.92",  "0.776", "0.624", "0.789","0.767","0.254","0.462","0.519","0.236"], size=(1))
    gender = random.choice(["male","female",], size=(1))
    relevant_experience = random.choice(["15",  "1", "5", "20","11","10","18","7"], size=(1))
    enrolled_university = random.choice(["Full Time",  "Part Time", "Not Enrolled",], size=(1))
    company_size = random.choice(["20",  "10", "1000", "50","500","10000","30"], size=(1))
    education = random.choice(["Masters",  "Graduate", "High School",], size=(1))
    company_type = random.choice(["Pvt Ltd","Funded Startup","MNC"], size=(1))
    reason_switch = random.choice(["Less Salary","Work Life Balance","","Better job opportunity"], size=(1))
    skill_set = random.choice(["python","java","c++","sql","c","Ruby","Flutter","Golang","Kotline","Scala","Swift","Typescript"], size=(1))
    docs = datetime.datetime.now()
    dom = datetime.datetime.now()

    cursor.execute("INSERT INTO [dbo].[war] VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (city[0],city_development_index[0],gender[0],relevant_experience[0],enrolled_university[0],company_size[0],education[0],company_type[0],reason_switch[0],skill_set[0], docs, dom))
    #cursor.execute("INSERT INTO [dbo].[war] ([city],[city_development_index],[gender],[relevant_experience],[enrolled_university],[company_size],[education],[company_type],[reason_switch],[skill_set],[doc],[dom]) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (city,city_development_index,gender,relevant_experience,enrolled_university,company_size,education,company_type,reason_switch,skill_set,doc,dom))

    cursor.commit()
    print("Done - ", i)

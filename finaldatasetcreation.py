import numpy as np
from numpy import random
city = random.choice(["Indore",  "Bhopal", "Mumbai", "Bangaluru","Pune",], p=[0.1,0.05,0.25,0.3,0.3,], size=(100))
print(city)
citydevelopmentindex = random.choice(["0.92",  "0.776", "0.624", "0.789","0.767",], p=[0.1,0.05,0.25,0.3,0.3,], size=(100))
print(citydevelopmentindex)
companysize = random.choice(["20",  "10", "1000", "50","500",], p=[0.1,0.05,0.25,0.3,0.3,], size=(100))
print(companysize)
companytype = random.choice(["Pvt Ltd","Funded Startup",], p=[0.6,0.4,], size=(100))
print(companytype)
education = random.choice(["Masters",  "Graduate", "High School",], p=[0.6,0.35,0.05,], size=(100))
print(education)
enrolleduniversity = random.choice(["full time",  "part time", "not enrolled",], p=[0.6,0.35,0.05,], size=(100))
print(enrolleduniversity)
gender = random.choice(["male","female",], p=[0.65,0.35], size=(100))
print(gender)
reasonswitch = random.choice(["less salary","work life balance",], p=[0.6,0.4,], size=(100))
print(reasonswitch)
relevantexperience = random.choice(["15",  "1", "5", "20","11",], p=[0.1,0.05,0.25,0.3,0.3,], size=(100))
print(relevantexperience)
skillset = random.choice(["python",  "java", "c++", "sql","c",], p=[0.1,0.05,0.25,0.3,0.3,], size=(100))
print(skillset)
import numpy as np
from numpy import random
city = random.choice(["Indore",  "Bhopal", "Mumbai", "Bangaluru","Pune",], p=[0.1,0.05,0.25,0.3,0.3,], size=(100))
print(city)

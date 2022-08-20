import numpy as np
from numpy import random
companytype = random.choice(["Pvt Ltd","Funded Startup",], p=[0.6,0.4,], size=(100))
print(companytype)
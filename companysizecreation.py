import numpy as np
from numpy import random
companysize = random.choice(["20",  "10", "1000", "50","500",], p=[0.1,0.05,0.25,0.3,0.3,], size=(100))
print(companysize)

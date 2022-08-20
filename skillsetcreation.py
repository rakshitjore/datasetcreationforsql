import numpy as np
from numpy import random
skillset = random.choice(["python",  "java", "c++", "sql","c",], p=[0.1,0.05,0.25,0.3,0.3,], size=(100))
print(skillset)

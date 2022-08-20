import numpy as np
from numpy import random
education = random.choice(["Masters",  "Graduate", "High School",], p=[0.6,0.35,0.05,], size=(100))
print(education)
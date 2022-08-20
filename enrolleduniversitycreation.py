import numpy as np
from numpy import random
enrolleduniversity = random.choice(["full time",  "part time", "not enrolled",], p=[0.6,0.35,0.05,], size=(100))
print(enrolleduniversity)

import numpy as np
import pandas as pd

ini = np.random.randint(60,101,5)
tempurature = pd.Series(ini)
print(tempurature.min())
print(tempurature.max())
print(tempurature.describe())




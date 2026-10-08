import pandas as pd
import numpy as np
s = pd.Series(np.random.rand(10))
print("Series:")
print(s)
print("Indexing:")
print(s[0])
print("Filtering:")
print(s[s > 0.5])
print("Mean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())

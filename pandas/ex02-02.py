# training Sum

import pandas as pd
import numpy as np

col=['col1','col2', 'col3']
row=['row1', 'row2', 'row3']

data=[[1,2,3],[4,5,6],[7,np.NAN, 9]]
df=pd.DataFrame(data, index=row, columns=col)

print("================= df ==================")
print(df)
print("================= sum of columns ==================")
print(df.sum(axis=0)) #axis=0, sum of columns
print("================= sum of rows ==================")
print(df.sum(axis=1)) #axis=1, sum of rows

print("================= sum of columns with skipna ==================")
print(df.sum(axis=0, skipna=False)) #axis=0, sum of columns
print("================= sum of rows with skip na==================")
print(df.sum(axis=1, skipna=False)) #axis=1, sum of rows

print("================= sum of rows with min_count ==================")
print(df.sum(axis=1, min_count=3)) #axis=1, sum of rows
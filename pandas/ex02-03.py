# training Product

import pandas as pd
import numpy as np

col=['col1','col2', 'col3']
row=['row1', 'row2', 'row3']

data=[[1,2,3],[4,5,6],[7,np.NAN, 9]]
df=pd.DataFrame(data, index=row, columns=col)

print("================= df ==================")
print(df)
print("================= product of columns ==================")
print(df.prod(axis=0)) #axis=0, product of columns
print("================= product of rows ==================")
print(df.prod(axis=1)) #axis=1, product of rows

print("================= product of columns with skipna ==================")
print(df.prod(axis=0, skipna=False)) #axis=0, product of columns
print("================= procut of rows with skip na==================")
print(df.prod(axis=1, skipna=False)) #axis=1, product of rows

print("================= sum of rows with min_count ==================")
print(df.prod(axis=1, min_count=3)) #axis=1, prod of rows
import pandas as pd
import numpy as np

"""
Multi Index의 경우에 사용하는 Indexing 기법을 알아보겠습니다.
"""

index_tuples=[('row1','val1'),('row1','val2'),('row2','val1'),('row2','val2'),('row2','val3'),('row3','val2'),('row3','val3')]
values=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]]
index=pd.MultiIndex.from_tuples(index_tuples)
df=pd.DataFrame(values, columns=['col1','col2','col3'], index=index)
print(df)

print(df.loc['row2'])
print(df.loc[('row2','val2')])
print(df.loc[('row2','val2'),'col3'])
print(df.loc[('row1','val2'):('row3','val2')])
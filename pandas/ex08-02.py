import pandas as pd
import numpy as np

"""
08-02. 다른 객체로 결측치 덮어쓰기 (combine_first)
DataFrame.combine_first(other)
개요
combine_first 메서드는 other의 값으로 self(df)의 NaN값을 덮어쓰는 메서드입니다.
사용법
self.combine_first(other)
other : self객체의 결측치를 덮어쓸 객체 입니다.
"""

n=np.NaN
col = ['col1','col2','col3']
row = ['row1','row2','row3']
data1 = [[n,n,1],
         [n,n,1],
         [1,1,1]]
data2 = [[2,2,2],
         [2,n,2],
         [2,1,2]]
df1 = pd.DataFrame(data1,row,col)
df2 = pd.DataFrame(data2,row,col)
print(df1)
print(df2)

print(df1.combine_first(df2))

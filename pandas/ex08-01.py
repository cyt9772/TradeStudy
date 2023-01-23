import pandas as pd
import numpy as np

"""
08-01. 함수를 이용한 열 단위 결합 (combine)
DataFrame.combine(other, func, fill_value=None, overwrite=True)
개요
combine 메서드는 두 pandas 객체를 func함수를 이용하여 결합하는 메서드입니다.
사용법
기본 사용법
self.combine(other, func, fill_value=None, overwrite=True)
other : 결합 할 DataFrame객체 입니다.
func : 결합에 이용할 함수 입니다.
fill_value : 결합하기전 Na의 값을 이 값으로 대체합니다.
overwrite : other에 존재하지 않는 self의 열의 값을 NaN으로 대체합니다.
"""

n=np.NaN
col = ['col1','col2','col3']
row = ['row1','row2','row3']
data1 = [[1,3,4],
         [n,8,2],
         [2,6,7]]
data2 = [[7,2,3],
         [2,4,2],
         [3,1,5]]
df1 = pd.DataFrame(data1,row,col)
df2 = pd.DataFrame(data2,row,col)
print(df1)
# print(df2)
#
# #print(df1.combine(df2,np.maximum))
# print(df1.combine(df2,np.maximum, fill_value=9))

col3 = ['col1','col2']
row3 = ['row1','row2']
data3 = [[1,2],
         [3,4]]
df3 = pd.DataFrame(data3, row3, col3)
print(df3)
print(df1.combine(df3,np.maximum, overwrite=False))
print(df1.combine(df3,np.maximum, overwrite=True))
import pandas as pd
import numpy as np

"""
05-01. 초과, 미만, 이상, 이하, 같음, 다름 (gt, lt, ge, le, eq, ne)
pandas.DataFrame.gt(other, axis='columns', level=None) >
pandas.DataFrame.lt(other, axis='columns', level=None) <
pandas.DataFrame.ge(other, axis='columns', level=None) >=
pandas.DataFrame.le(other, axis='columns', level=None) <=
pandas.DataFrame.eq(other, axis='columns', level=None) ==
pandas.DataFrame.ne(other, axis='columns', level=None) !=

개요
lt, gt, le, ge, eq, ne 메서드는 DataFrame의 크기 비교를 수행하는 메서드입니다.
각각 >, <, >=, <=, ==, !=와 용도가 같습니다. 그리고 각 메서드는 사용법이 동일합니다.
※각각 less than, grater than, less equal, grater equal, equal, not equal을 뜻합니다.

사용법
기본 사용법
df.eq(other, axis='columns', level=None)
other : 스칼라, 시퀀스, Series, DataFrame, list등이 올 수 있습니다. 비교하고자 하는 값입니다.
axis : {0 : index / 1 : columns} 비교할 레이블 입니다.
level : 멀티인덱스 사용시 비교할 레이블의 레벨입니다.
"""

col=['col1','col2','col3']
row=['A','B','C']
df=pd.DataFrame(data=[[10,20,10],[80,30,60],[20,10,70]], index=row, columns=col)
print(df)

# print(df.eq(10))
# print(df.ne(20))

# s1=pd.Series([10,30],index=['col1','col3'])
# print(df.gt(s1))
#
# s2=pd.Series([10],index=["col4"])
# print(df.lt(s2))

# print(df.le([10,20,30], axis='columns'))
# print(df.le([10,20,30], axis=1))

# df2=pd.DataFrame([[50],[50],[50]], index=row, columns=['col1'])
# print(df.ge(df2))

row_mul = [['U','U','U','D','D','D'],['A','B','C','A','B','C']]
df_mul = pd.DataFrame(data=[[10,20,10],
                            [80,30,60],
                            [20,10,70],
                            [30,70,60],
                            [10,90,40],
                            [50,30,80]],index=row_mul,columns=col)
print(df_mul)

print(df.ge(df_mul, level=1))
import pandas as pd
import numpy as np

"""
loc 함수는 at 함수와 같이 레이블 기반으로 인덱싱을 합니다. DataFrame이나 Series형식으로의 반환이 필요하면 loc를 사용합니다.
"""

df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], index=['row1','row2','row3'], columns=['col1','col2','col3'])
print(df)

print(df.loc['row1'])
print(df.loc[['row1','row2']])
print(df.loc['row1':'row3', 'col3'])

bool=[False, True, False]
print(df.loc[bool])

print(df.loc[df['col3']>5])
print(df.loc[df['col3']>5,['col2']])

print(df.loc[lambda df: df['col2']==5])

# value setting
df.loc[['row1','row3'],['col3']]='A'
df.loc['row1']='A'
print(df)

df.loc[:,['col3']]='B'
print(df)
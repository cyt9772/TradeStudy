import pandas as pd
import numpy as np

"""
06-02. 결측값 제거 (dropna)
DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
개요
dropna 메서드는 DataFramde내의 결측값이 포함된 레이블을 제거하는 메서드입니다.
사용법
기본 사용법
df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
axis : {0: index / 1: columns} 결측치 제거를 진행 할 레이블입니다.
how : {'any' : 존재하면 제거 / 'all' : 모두 결측치면 제거} 제거할 유형입니다. 포함만 시켜도 제거할지, 전무 NA여야 제거할지 정할 수 있습니다.
tresh : 결측값이 아닌 값이 몇 개 미만일 경우에만 적용시키는 인수 입니다.
예를들어, tresh값이 3이라면 결측값이 아닌 값이 3개 미만일 경우에만 dropna메서드를 수행합니다.
subset : dropna메서드를 수행할 레이블을 지정합니다.
inplace : 원본을 변경할지의 여부입니다.
"""

col  = ['col1','col2','col3','col4','col5']
row  = ['row1','row2','row3','row4']
data = [[1,2,3,pd.NA,5],[6,pd.NA,8,pd.NA,10],[11,12,13,14,15],[pd.NA,pd.NA,pd.NA,pd.NA,pd.NA]]
df = pd.DataFrame(data,row,col)
print(df)

# print(df.dropna(axis=0))
# print(df.dropna(axis=1))
# print('==================')
# print(df.dropna(how='any'))
# print(df.dropna(how='all'))
print('==================')
#print(df.dropna(thresh=4))
print(df.dropna(subset=['col1','col2']))
print(df.dropna(inplace=True))

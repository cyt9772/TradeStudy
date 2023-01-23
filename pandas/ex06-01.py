import pandas as pd
import numpy as np

"""
DataFrame.isna( )
※ isnull( )과 완전히 동일합니다.
DataFrame.notna( )
※ notnull( )과 완전히 동일합니다.
개요
isna 메서드와 notna 메서드는 DataFrame내의 결측값을 확인해서 bool형식으로 반환하는 메서드입니다.
isna의 경우 결측값이면 True 반환, 정상값이면 False반환이며,
notna의 경우 결측값이면False반환, 정상값이면 True를 반환합니다.

사용법
기본 사용법
df.isna( ) / df.notna( )
np.inf나 그냥 ' ' 의경우 결측값으로 판단하지 않습니다.
"""


col  = ['col1','col2','col3','col4']
row  = ['row1','row2','row3']
data = [[1,2,pd.NA,4],
        [np.nan,6,7,8],
        [9,10,11,None]]
df = pd.DataFrame(data,row,col)
print(df)

print(df.isna())
print(df.notna())
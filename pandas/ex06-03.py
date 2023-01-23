import pandas as pd
import numpy as np

"""
06-03. 결측값 없는 인덱스 확인 (first_valid_index / last_valid_index)
DataFrame.first_valid_index( )
DataFrame.last_valid_index( )
개요
first_valid_index메서드의 경우 처음으로 결측치가 아닌값이 나오는 행의 인덱스를 출력합니다.
last_valid_index메서드의 경우 마지막으로 결측치가 아닌값이 나오는 행의 인덱스를 출력합니다.
즉, 결측값만 있는 행은 무시한다고 생각하면 됩니다.

사용법
기본 사용법
df.first_valid_index( )
df.last_valid_index( )
"""

col  = ['col1','col2']
row  = ['row1','row2','row3','row4','row5']
data = [[np.nan,np.nan],[pd.NA,4],[pd.NA,pd.NaT],[5,6],[np.nan,pd.NA]]
df = pd.DataFrame(data,row,col)
print(df)

print(df.first_valid_index())
print(df.last_valid_index())
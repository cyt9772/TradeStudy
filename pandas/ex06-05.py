import pandas as pd
import numpy as np

"""
06-05. 결측값 없는 마지막 행 반환 (asof)
DataFrame.asof(where, subset=None)
개요
asof 메서드는 인덱스 기준으로 where이전에 결측치가 없는 마지막 행을 구합니다.

사용법
기본 사용법
df.asof(where, subset=None)
where : 기준이 되는 인덱스 값입니다.
subset : 기준이 되는 열 입니다.
"""

row = [10,20,30,40,50,60]
data = {'A':[1,pd.NA,pd.NA,4,5,6],'B':[7,8,9,10,pd.NA,12]}
df = pd.DataFrame(data=data, index = row)
print(df)

# print(df.asof(where=45))
print(df.asof(where=[10,35,60],subset='B'))
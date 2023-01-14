import pandas as pd
import numpy as np

"""
DataFrame.at
at 함수는 loc 함수와 같이 레이블 기반으로 인덱싱을 하지만,
DataFrame과 Series에 상관없이 하나의 스칼라값에 접근한다는 차이가 존재합니다.
"""

df=pd.DataFrame([[1,2],[3,4]], index=['row1','row2'], columns=['col1','col2'])
print(df)

df.at['row1','col1']=5
print(df)
print(df.loc['row2'].at['col1'])
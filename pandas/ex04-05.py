import pandas as pd
import numpy as np

"""
DataFrame.head(n=5)
개요
head함수는 Dataframe 객체를 위에서부터 n열 반환하는 함수입니다.
기본값은 5입니다.

사용법
기본 사용법
df.head(n=5)
"""

data=np.random.randint(10,size=(10,10))
df=pd.DataFrame(data)
print(df)

print(df.head(3))
print("================")
print(df.tail(3))
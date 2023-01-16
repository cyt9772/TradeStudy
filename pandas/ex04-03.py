import pandas as pd
import numpy as np

"""
DataFrame.iat
iat 함수는 iloc 함수와 같이 정수 기반으로 인덱싱을 합니다.
단일 스칼라값으로 반환하길 원한다면 iat함수를 사용합니다.

개요
정수기반 조회 메서드입니다. 행/열 한쌍에 대한 단일 값에 엑세스합니다.

사용법
기본 사용법
값 가져오기 : result = df.iat['행', '열']
값 설정하기 : df.iat['행', '열'] = value

"""

df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], index=['row1','row2','row3'], columns=['col1','col2','col3'])
print(df)

print(df.iat[1,2])
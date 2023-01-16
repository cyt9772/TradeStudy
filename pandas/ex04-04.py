import pandas as pd
import numpy as np

"""
DataFrame.iloc
iloc 함수는 iat 함수와 같이 정수 기반으로 인덱싱을 합니다.
DataFrame이나 Series형식으로의 반환이 필요하면 iloc를 사용합니다.

개요
정수기반 조회 메서드입니다.

사용법
기본 사용법
값 가져오기 : result = df.iloc['행', '열']
값 설정하기 : df.iloc['행', '열'] = value


가능한 Input
1. 단일 정수값 (예 : 5)
2. 정수로 이루어진 list (예 : [3, 5, 1])
3. 정수 슬라이스 객체 (예 : 2:5 )
4. bool 배열
"""

df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], index=['row1','row2','row3'], columns=['col1','col2','col3'])
print(df)

print(df.iloc[0])
print(df.iloc[[0,2]])
print(df.iloc[1:2])

#bool list
boot_list=[True, False, True]
result=df.iloc[boot_list]
print(result)
import pandas as pd
import numpy as np

"""
DataFrame.clip(lower=None, upper=None, axis=None, inplace=False, args, kwargs)
개요
clip 메서드는 Series나 DataFrame에 대해서 요소들의 범위를 제한하는 메서드입니다
즉, 상한선과 하한선을 임계값으로 정해서 임계값 밖의 값을 임계값으로 변경합니다.
NA의 경우 변경하지 않습니다.

사용법
기본 사용법
df.clip(lower=None, upper=None, axis=None, inplace=False, args, kwargs)
lower : 하한값입니다. 이 이하의 값은 이 값으로 변경됩니다.
upper : 상한값입니다. 이 이상의 값은 이 값으로 변경됩니다.
axis : 계산할 기준이되는 레이블입니다.
inplace : 제자리에서 계산할지 여부 입니다.

inplace의 개념은 간단합니다. 우리가 만약 print(df.dropna())로 df에서 NA를 제거한다고 가정해봅니다.
그럼 NA가 사라진 데이터가 출력되겠지만, 다시 print(df)할 경우 df는 변경되어있지 않을 것입니다.
이때 print(df.dropna(inplace=True))를 수행한다면 print(df) 실행 시 df에도 NA가 삭제되어있는것을
확인할 수 있습니다. 물론 dropna뿐만 아니라 clip처럼 inplace 인수를 가진 모든 함수에서 동일합니다.
즉, df.dropna(inplace=True)는 df = df.dropna( )와 같은 효과를 가집니다.
"""

col  = ['col1','col2','col3']
row  = ['row1','row2','row3']
data = [[-7,3,9],
        [6,-8,1],
        [-3,0,-7]]
df = pd.DataFrame(data,row,col)
print(df)

print(df.clip(-4,5))

s=pd.Series(data=[1,2,3],index=row)
print(df.clip(-s,s,axis=0))
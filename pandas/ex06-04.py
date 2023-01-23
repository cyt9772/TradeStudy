import pandas as pd
import numpy as np

"""
06-04. 결측값 변경 (fillna / backfill / bfill / pad / ffill)
DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)
DataFrame.backfill( ) / DataFrame.bfill : DataFrame.fillna(mathod='bfill')과 동일합니다.
DataFrame.pad / DataFrame.ffill : DataFrame.fillna(method='ffill')과 동일합니다.

개요
fillna 메서드는 DataFrame에서 결측값을 원하는 값으로 변경하는 메서드입니다.

사용법
기본 사용법
df.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)
value : 결측값을 대체할 값입니다. dict형태로도 가능합니다.
method : 결측값을 변경할 방식입니다. bfill로 할경우 결측값을 바로 아래 값과 동일하게 변경합니다.
ffill로 할 경우 결측값을 바로 위 값과 동일하게 변경합니다.
axis : {0 : index / 1 : columns} fillna 메서드를 적용할 레이블입니다.
inplace : 원본을 변경할지 여부입니다. True일 경우 원본을 변경하게 됩니다.
limit : 결측값을 변경할 횟수입니다. 위에서부터 limit로 지정된 갯수만큼만 변경합니다.
downcast : 다운캐스트할지 여부입니다. downcast='infer'일 경우 float64를 int64로 변경합니다.
"""

col  = ['col1','col2','col3','col4','col5']
row  = ['row1','row2','row3','row4','row5']
na = np.nan
data = [[na, 2,na, 4,na],
        [ 6, 7,na, 9,na],
        [11,na,na,14,15],
        [na,17,na,na,20],
        [na,22,na,na,25]]
df = pd.DataFrame(data,row,col)
print(df)

# print(df.fillna('A'))
dict={'col1':'A', 'col2':'B','col3':'C', 'col4':'D', 'col5':'E'}
# print(df.fillna(value=dict))
# print(df.fillna(method='bfill'))
# print(df.fillna(method='ffill'))
print(df.fillna(0,downcast='infer'))
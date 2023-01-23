import pandas as pd
import numpy as np

"""
07-01. 값 기준 정렬 (sort_values)
DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)
개요
sort_values 메서드는 값을 기준으로 레이블을 정렬하는 메서드입니다.
사용법
기본 사용법
df.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)
by : 정렬 기준이될 레이블입니다.
axis : {0 : index / 1: columns} 정렬할 레이블입니다. 0이면 행, 1이면 열을 기준으로 정렬합니다.
inplace : 원본을 대체할지 여부입니다. True일 경우 원본을 대체하게 됩니다.
kind : 알고리즘 모드 입니다. 모드는 총 4종으로 quicksort, mergesort, heapsort, stable이 있는데,
속도와 효율성의 차이를 갖습니다. 기본적으로 quicksort이며, 자세한건 numpy doc에서 확인 가능합니다.
na_position : {first / last} Na값의 위치입니다. 기본값은 last로 정렬시 맨 뒤에 위치합니다.
ignore_index : 인덱스의 무시 여부입니다. True일 경우 인덱스의 순서와 상관없이 0,1,2,... 로 정해집니다.
key : 이 인수를 통해 정렬방식으로 함수를 사용할 수 있습니다. lamba의 사용이 가능합니다.
"""

na = np.NaN
data = [[-3,'A',17],
        [na,'D',31],
        [ 7,'D',-8],
        [15,'Z', 3],
        [ 0, na,-7]]
col = ['col1','col2','col3']
row = ['row1','row2','row3','row4','row5']
df = pd.DataFrame(data = data, index = row, columns= col)
print(df)

#print(df.sort_values(by='col3'))
# print(df.sort_values(by=['col2','col3']))
# print(df.sort_values(by='col3',axis=0))
print(df.sort_values(by='row5',axis=1))
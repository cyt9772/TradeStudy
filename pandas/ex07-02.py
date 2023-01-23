import pandas as pd
import numpy as np

"""
07-02. 인덱스 기준 정렬 (sort_index)
DataFrame.sort_index(axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True, ignore_index=False, key=None)
개요
sort_index 메서드는 인덱스를 기준으로 레이블을 정렬하는 메서드입니다.
사용법
기본 사용법
df.sort_index(axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True, ignore_index=False, key=None)
axis : {0 : index / 1: columns} 정렬할 레이블입니다. 0이면 행, 1이면 열을 기준으로 정렬합니다.
level : multi index의 경우 정렬을 진행할 level입니다.
ascending : 오름차순으로할지 여부 입니다. 기본은 True로 오름차순입니다.
inplace : 원본을 대체할지 여부입니다. True일 경우 원본을 대체하게 됩니다.
kind : 알고리즘 모드 입니다. 모드는 총 4종으로 quicksort, mergesort, heapsort, stable이 있는데,
속도와 효율성의 차이를 갖습니다. 기본적으로 quicksort이며, 자세한건 numpy doc에서 확인 가능합니다.
na_position : {first / last} Na값의 위치입니다. 기본값은 last로 정렬시 맨 뒤에 위치합니다.
sort_remaining : multi index의 경우 다른 레벨에 대해서도 정렬을할지 여부입니다. True로 할 경우
한 레벨에 대한 정렬이 완료되면, 다른 레벨도 정렬합니다.
ignore_index : 인덱스의 무시 여부입니다. True일 경우 인덱스의 순서와 상관없이 0,1,2,... 로 정해집니다.
"""

na = np.NaN
index_tuples = [('row1', 'val1'), ('row1', 'val2'), ('row3', 'val3'), ('row3', 'val1'), ('row3', 'val2'), ('row2', 'val5'),('row2', 'val2')]
values = [ [1,2,3], [4,na,6], [7,8,9], [na,11,12], [13,14,15], [16,17,18], [19,20,21]]
index = pd.MultiIndex.from_tuples(index_tuples) # 인덱스 설정
df = pd.DataFrame(values, columns=['col4', 'col1', 'col2'], index = index)
print(df)

# print(df.sort_index(axis=0,level=0))
#print(df.sort_index(axis=0, level=1))
print(df.sort_index(axis=0, level=[1,0],ascending=[False,True]))
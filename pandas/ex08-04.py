import pandas as pd
import numpy as np

"""
08-04. 객체병합 (merge)
DataFrame.merge(right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
개요
merge메서드는 두 객체를 병합하는 메서드입니다. join과 비슷하지만 더 세부적인 설정이 가능한 메서드로,
인덱스-열 기준 병합도 가능하며, indicator인수를 통한 병합정보확인, validate를 통한 병합방식 확인등이 가능합니다.

사용법
left.merge(right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
right: left와 함께 병합할 객체입니다.
how : 병합시 기준이 될 인덱스를 정하는 방식입니다. left는 기존객체, right는 병합할 객체, inner은 두 객체의 인덱스의 교집합, outer은 두 객체의 인덱스의 합집합, cross는 행렬곱 입니다.
on : 열 기준 병합시 기준으로할 열의 이름이 양측이 동일하다면, on인수에 입력함으로써 기준 열을 정할 수 있습니다.
left_on / right_on : 열기준 병합 시 기준으로 할 열의 양측 이름이 다르다면, 각각 어떤 열을 기준으로 할지 정해줍니다.
열의 이름을 입력하면 됩니다.
left_index / right_index : 인덱스 기준 병합 시 True로 하면 해당 객체의 인덱스가 병합 기준이됩니다.

※ 즉 left_on을 입력하고 right_index를 True로 한다면 열-인덱스 기준 병합도 가능합니다.

sort : 병합 후 인덱스의 사전적 정렬 여부입니다. join메서드와 기능이 동일하므로 참고 바랍니다.
suffixes : 병합할 객체들간 이름이 중복되는 열이 있다면, 해당 열에 붙일 접미사를 정합니다.
기본적으로 join메서드의 lsuffix / rsuffix와 기능이 동일하지만, suffixes인수는 튜플로 두 값을
한번에 입력한다는 차이가 있습니다.
copy : 사본을 생성할지 여부입니다.
indicator : True로 할경우 병합이 완료된 객체에 추가로 열을 하나 생성하여 병합 정보를 출력합니다.
validate : {'1:1' / '1:m' / 'm:1' / 'm:m'} 병합 방식에 맞는지 확인할 수 있습니다. 만약 validate에 입력한 병합방식과, 실제 병합 방식이 다를경우 오류가 발생됩니다.
예를들어, validate="1:m"으로 입력하였는데, 실제로 m:1 병합방식일 경우 오류가 발생됩니다.
"""

df1=pd.DataFrame({'IDX1':['a','b','c','a'], 'VAL':[1,2,3,4]})
df2=pd.DataFrame({'IDX2':['a','c','d'], 'VAL':[5,6,7]})
print(df1)
print(df2)

print(df1.merge(df2, left_on='IDX1', right_on='IDX2'))
#공통으로 a,c가 idx에 존재하고, idx1에는 2개 a존재하므로 a,a,c가 공통, default='inner'

df3=pd.DataFrame({'VAL1':[1,2,3]},index=['row1','row2','row3'])
df4=pd.DataFrame({'VAL2':[4,5,6]},index=['row2','row3','row4'])
print(df3,'\n')
print(df4,'\n')

print(df3.merge(df4, left_index=True, right_index=True))

df5=pd.DataFrame({'VAL1':[1,2,3]},index=['row1','row2','row3'])
df6=pd.DataFrame({'IDX':['row2','row3','row4'], 'VAL2':[4,5,6]})
print(df5,'\n')
print(df6,'\n')

print(df5.merge(df6,left_index=True, right_on='IDX'))
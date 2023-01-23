import pandas as pd
import numpy as np

"""
08-03. 인덱스기준 병합 (join)
DataFrame.join(other, on=None, how='left', lsuffix='', rsuffix='', sort=False)
개요
join 메서드는 두 객체를 인덱스 기준으로 병합하는 메서드 입니다.

사용법
self.join(other, on=None, how='left', lsuffix='', rsuffix='', sort=False)
other : self와 합칠 객체 입니다.
on : self의 열이나 인덱스 중에서 other의 어떤 열을 기준으로 결합할지 입니다.
즉, other의 (인덱스 기준이 아닌) 열 기준으로 결합할 때 on인수를 사용합니다.
how : {left : self기준 / right : other기준 / inner : 교집합 / outer : 합집합} 출력할 인덱스의 기준입니다.
lsuffix / rsffix : 이름이 중복되는 열이 있을 때 그 열에 추가로 붙일 접미사입니다.
lsuffix는 self의 열에 붙을 접미사고, rsuffix는 other의 열에 붙을 접미사입니다.
sort : 출력되는 데이터의 index를 사전적으로 정렬할지 여부입니다.
"""

df1=pd.DataFrame({'col1':[1,2,3]}, index=['row3','row2','row1'])
df2=pd.DataFrame({'col2':[13,14]}, index=['row4','row3'])
df3=pd.DataFrame({'col1':[23,24]}, index=['row4','row3'])
print(df1)
print(df2)
print(df3)


# print(df1.join(df2,how='left', sort=True))
df4=pd.DataFrame({'IDX':['A','B','C'],'col1':[1,2,3]})
df5=pd.DataFrame({'IDX':['C','D'],'col2':[13,14]})
print(df4)
print(df5)

print(df4.set_index('IDX').join(df5.set_index('IDX')))
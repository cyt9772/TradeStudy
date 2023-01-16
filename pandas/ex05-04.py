import pandas as pd
import numpy as np

"""
DataFrame.filter(items=None, like=None, regex=None, axis=None)
개요
filter 메서드는 레이블에 대해서 조건에 맞는 레이블만 필터링하는 메서드입니다.
내용물이 아니라 레이블에 대해서만 필터링하는것을 유의하세요.
특정 레이블을 이름으로 필터링하거나, 포함된 문자열을 통해 필터링하거나, 정규표현식으로 필터링이 가능합니다.
정규표현식(regular expression)의 경우 regex라고도 하며 파이썬에서는 re 메서드가 지원하는 내용과 동일합니다.
※ 정규표현식의경우 웹상에 자료가 방대하므로 이 페이지에서는 설명하지 않겠습니다. 추후 별도 페이지로 생성 예정입니다.

사용법
기본 사용법
df.filter(items=None, like=None, regex=None, axis=None)
items : 이름으로 필터링하는 경우입니다. 리스트형태로 입력합니다.
like : str로 필터링합니다. 해당 문자열이 포함된 경우를 반환합니다.
regex : 정규표현식을 이용해 필터링합니다. re.search(regex, label) == True에서 사용되는 경우와 동일합니다.
axis : {0 : index / 1 : columns} 필터링할 레이블입니다. 0은 행, 1은 열 입니다.
"""

col  = ['alpha','beta','gamma','delta','epsilon']
row  = ['sigma','omega','lambda']
data = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
df = pd.DataFrame(data,row,col)
print(df)

print(df.filter(items=['alpha','beta']))
print(df.filter(items=['omega'], axis=0))

print(df.filter(like='ta'))
print(df.filter(regex='[mn]'))
print(df.filter(regex='^g'))
print(df.filter(regex='a$'))

import pandas as pd
import numpy as np

"""
07-03. 정렬후 추출 (nlargest, nsmallest)
DataFrame.nlargest(n, columns, keep='first')
DataFrame.nsmallest(n, columns, keep='first')
개요
nlargest메서드와 nsmallest메서드는 데이터를 오름차순/내림차순 정렬 후, 위에서 n개의 행을 출력하는 메서들입니다.
사실상 df.sort_values(columns, ascending=True/False).head(n)와 사용방식이 완전히 동일합니다.

사용법
기본 사용법
df.nlargest(n, columns, keep='first')
df.nsmallest(n, columns, keep='first')
n : 정렬 후 출력할 행의 수 입니다.
columns : 정렬의 기준이 될 열 입니다.
keep :{first, last, all} 동일한 값일경우 어느 행을 출력할지 정합니다. first면 위부터, last면 아래부터, all이면 모두 출력합니다.
"""

col = ['col1','col2','col3']
row = ['row3','row5','row1','row4','row2']
data = [[ 1, 21, 7],
        [ 2, 33, 3],
        [ 2,  7,97],
        [ 4, 56,31],
        [ 5, 18, 5]]
df = pd.DataFrame(data=data, index=row, columns=col)
print(df)

#print(df.nlargest(n=3,columns='col1', keep='first'))
#print(df.nlargest(n=3,columns='col1', keep='all'))
print(df.nlargest(n=3,columns=['col1','col3']))
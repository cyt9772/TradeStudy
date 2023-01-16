import pandas as pd
import numpy as np

"""
DataFrame.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None, ignore_index=False)
개요
sample 메서드는 DataFrame이나 Series에서 무작위로 몇개의 값(레이블)을 출력하는 메서드입니다.
사용법
기본 사용법
df.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None, ignore_index=False)
n : 추출할 갯수 입니다. replace가 False면 n의 최댓값은 레이블의 갯수를 넘을수 없습니다.
frac : 추출할 비율입니다. 1보다 작은값으로 설정하며(예 : 0.3 이면 30%), n과 동시에 사용할 수 없습니다.
replace : 중복추출의 허용 여부 입니다. True로 하면 중복추출이 가능하며 n의 최댓값이 레이블의 갯수보다 커도 됩니다.
weight : 가중치입니다. 즉 레이블마다 추출될 확률을 지정할 수 있습니다. 합계가 1(100%)이 아닐경우 자동으로 1로 연산합니다.
random_state : 랜덤 추출한 값에 시드를 설정할 수 있습니다. 원하는 값을 설정하면, 항상 같은 결과를 출력합니다.
axis : {0 : index / 1 : columns} 추출할 레이블입니다.
ignore_index : index의 무시 여부입니다. True일경우 출력시 index를 무시하고 숫자로 출력합니다.
"""

col  = ['col1','col2','col3']
row  = ['row1','row2','row3','row4','row5']
data = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
df = pd.DataFrame(data,row,col)
print(df)

print(df.sample(2))
print(df.sample(10,replace=True))

import pandas as pd
import numpy as np

"""
elect_dtypes 함수는 열에 포함된 데이터들을 type 기준으로 인덱싱 할 수 있도록 합니다.
select_dtypes(include=None, exclude=None) 형태를 가지며, include에 넣은값을 포함하고
exclude에 넣은 값을 제외한 columns(열)을 DaraFrame 형태로 반환합니다.

사용법
기본 사용법
df.dtypes
* include 및 exclude는 비어있거나 겹치면 안되며(에러발생), 스칼라나 list형태의 입력값이 가능합니다.
자료형
1. 숫자형(numeric)은 np.number 또는 'number'
2. 문자형(str)은 'object'
3. 날짜,시간(datetimes)을 선택하려면 np.datetime64, 'datetime' 또는 'datetime64'
4. timedeltas는 np.timedelta64, 'timedelta' or 'timedelta64'
5. Pandas의 categorical 타입은 'category'
"""

col1 = [1, 2, 3, 4, 5]
col2 = ['one', 'two', 'three', 'four', 'five']
col3 = [1.5, 2.5, 3.5, 4.5, 5.5]
col4 = [True, False, False, True, True]
df = pd.DataFrame({"col1": col1, "col2": col2, "col3": col3, "col4": col4})
print(df)

print(df.dtypes)
result=df.select_dtypes(include=[float, bool])
result=df.select_dtypes(exclude=['int64'])
result=df.select_dtypes(include=[float, object], exclude=['int64'])
print(result)
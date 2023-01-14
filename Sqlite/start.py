import pandas as pd
import yfinance as yf
import datetime
import sqlite3

start=datetime.datetime(2022,12,1)
end=datetime.datetime(2022,12,26)
df=yf.download("005930.KS",start=start, end=end)

con=sqlite3.connect("kospi.db")
df.to_sql('005930', con, if_exists='replace')

read_df=pd.read_sql("SELECT * From '005930'",con, index_col='Date')
print(read_df)
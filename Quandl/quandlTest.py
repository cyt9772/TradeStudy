import quandl

quandl.ApiConfig.api_key='Br23STx2dvxDvM-yQKYb'
data=quandl.get('BCHAIN/MKPRU', start_date='2023-01-01', end_date='2023-01-29')
print(data)
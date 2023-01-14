from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

pd.set_option('display.max_columns',None)

def get_dividend_yield(code):
    url="http://companyinfo.stock.naver.com/company/c1010001.aspx?cmp_cd="+code
    html=requests.get(url, verify=False).text

    soup=BeautifulSoup(html,'html.parser')
    dt_data=soup.select("div div:nth-of-type(2) div:nth-of-type(3) div div div:nth-of-type(14)")
    return dt_data

# 주식 종목 코드를 받아서 최근 5년 FS 데이터를 가져옴
def yearFS(code):
    name = code.split(',')[1]
    code = str(code.split(',')[0])

    YFS = 'http://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?cmp_cd=' + str(code) + '&fin_typ=0&freq_typ=Y'
    header = {'Accept-Encoding': 'gzip, deflate, sdch',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'}

    r = requests.get(YFS, headers=header)
    res = re.sub('[\t\n\r]', '', r.text)
    res = re.sub('<th class="bg r01c02 endLine line-bottom"colspan="8">연간</th>', '', res)
    res = re.sub('\(IFRS연결\)', '', res)
    res = re.sub('/12', '', res)
    df = pd.read_html(res, index_col='주요재무정보')[0]
    df['code'] = code
    df['name'] = name
    return df


# 주식 종목 코드를 받아서 최근 1년 분기별 FS 데이터를 가져옴
def quarterFS(code):
    name = code.split(',')[1]
    code = str(code.split(',')[0])

    QFS = 'http://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?cmp_cd=' + str(code) + '&fin_typ=0&freq_typ=Q'
    header = {'Accept-Encoding': 'gzip, deflate, sdch',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'}

    r = requests.get(QFS, headers=header)
    res = re.sub('[\t\n\r]', '', r.text)
    res = re.sub('<th class="bg r01c02 endLine  line-bottom"colspan="8">분기</th>', '', res)
    res = re.sub('\(IFRS연결\)', '', res)
    df = pd.read_html(res, index_col='주요재무정보')[0]
    df['code'] = code
    df['name'] = name
    return df


# 주식 종목 코드를 받아서 최근 3년의 주요 지표를 가져옴
def yearSummary(code):
    name = code.split(',')[1]
    code = str(code.split(',')[0])

    YSum = 'http://companyinfo.stock.naver.com/v1/company/cF1002.aspx?cmp_cd=' + str(code) + '&finGubun=MAIN&frq=0'
    header = {'Accept-Encoding': 'gzip, deflate, sdch',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'}

    r = requests.get(YSum, headers=header)
    res = re.sub('[\t\n\r]', '', r.text)
    res = re.sub('<th scope="col" colspan="2" class="line-bottom">매출액<span class="span-sub">\(억원, %\)</span></th>',
                 '<th scope="col" colspan="2" class="line-bottom">매출액<span class="span-sub">(억원, %)</span></th><th>YoY</th>',
                 res)
    res = re.sub('<th>금액</th><th>YoY</th>', '', res)
    df = pd.read_html(res, index_col='재무년월')[0]
    df['code'] = code
    df['name'] = name
    return df


# 주식 종목 코드를 받아서 최근 3년의 주요 지표를 가져옴
def quarterSummary(code):
    name = code.split(',')[1]
    code = str(code.split(',')[0])

    QSum = 'http://companyinfo.stock.naver.com/v1/company/cF1002.aspx?cmp_cd=' + str(code) + '&finGubun=MAIN&frq=1'
    header = {'Accept-Encoding': 'gzip, deflate, sdch',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'}

    r = requests.get(QSum, headers=header)
    res = re.sub('[\t\n\r]', '', r.text)
    res = re.sub('<th scope="col" colspan="2" class="line-bottom">매출액<span class="span-sub">\(억원, %\)</span></th>',
                 '<th scope="col" colspan="2" class="line-bottom">매출액<span class="span-sub">(억원, %)</span></th><th>YoY</th>',
                 res)
    res = re.sub('<th>금액</th><th>YoY</th>', '', res)
    df = pd.read_html(res)[0]
#    df = pd.read_html(res, index_col=['재무년월','재무년월'])[0]
    df['code'] = code
    df['name'] = name
    return df


f = open('./allstockcode.txt', 'r', encoding='utf-8')
for k in f.read().splitlines():
    yearFS(k).to_csv('./yearFS.csv', encoding='euc-kr', mode='a')  # csv 파일로 저장
    quarterFS(k).to_csv('./quarterFS.csv', encoding='euc-kr', mode='a')  # csv 파일로 저장
    yearSummary(k).to_csv('./yearSummary.csv', encoding='euc-kr', mode='a')  # csv 파일로 저장
    quarterSummary(k).to_csv('./quarterSummary.csv', encoding='euc-kr', mode='a')  # csv 파일로 저장

f.close()



if __name__ =="__main__":
    code='005930,삼성전자'

    #분기별 재무제표
    df=quarterSummary(code)
    print(df)



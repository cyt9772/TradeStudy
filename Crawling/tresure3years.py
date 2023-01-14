from bs4 import BeautifulSoup
import requests
import re

def get_3year_treasury():
    url="https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?stts_cd=107301&amp;idx_cd=1073&amp;freq=Y&amp;period=N"
    html=requests.get(url,verify=False).text

    #print(html)
    soup=BeautifulSoup(html, 'html5lib')
    td_data=soup.select("tbody tr td")

    #print(td_data)

    tresury_3year={}
    start_year=2014

    for x in td_data:
        tresury_3year[start_year]=x.text
        start_year +=1
        if start_year>2021:
            break

    print(tresury_3year)
    return tresury_3year



if __name__ =="__main__":
    get_3year_treasury()


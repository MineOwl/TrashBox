
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv


#Chromeを開く
driver = webdriver.Chrome('/Users/fenganling/Downloads/chromedriver')

#urlのページを開く
driver.get("http://www15.plala.or.jp/gcap/disney/realtime.htm")
html = driver.page_source
#ソースコードをダウンロード
bsObj = BeautifulSoup(html,"lxml")

#Chromeを閉じる
driver.close()


#tableに書き込み
table = []
for tr_tag in bsObj.findAll("tr")[54:70]:

    row = []
    for td_tag in tr_tag.findAll("td"):
        if td_tag.get_text() == "　":
            continue
        element = td_tag.get_text()
        row.append(element)

    table.append(row)

#この時点で
#tableに待ち時間の配列が入る

with open('desney.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(table)

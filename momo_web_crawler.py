import requests
import selenium
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

### 假設要查詢"DJI"
search_name = '伸縮 瀝水籃 '
web ='https://www.momoshop.com.tw/search/searchShop.jsp?keyword='+search_name+'&searchType=1&curPage=1&_isFuzzy=0&showType=chessboardType'


### requests伺服器資料
Chrome_driver_path = 'D:/chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"')
driver = webdriver.Chrome(executable_path=Chrome_driver_path,chrome_options=chrome_options)
driver.maximize_window() ###最大化視窗
#driver.set_page_load_timeout(10)  #等10秒
driver.get(web)

### BeautifulSoup 正式開始
soup = BeautifulSoup(driver.page_source, "html.parser")

product = soup.find_all('a',class_='goodsUrl') ### 找到目標區塊
print(product.find)
name_list = []
slogan_list = []
price_list = []
link=[]
for i in product:
    name_list.append( i.find('h3',class_="prdName").text)
    slogan_list.append( i.find('p',class_="sloganTitle").text)
    price_list.append( i.find('span',class_="price").text)
    #link.append(i.find('a','href').text)#有問題,有要連結,和前5頁


df1 = pd.DataFrame({'產品名稱':name_list,'副標題':slogan_list,'商品價格':price_list})
df1.to_excel("momo_web_crawler.xlsx")
#driver.quit()
print("爬蟲結束")
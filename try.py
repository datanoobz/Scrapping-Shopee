from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time


driver = webdriver.Chrome()
driver.get("https://shopee.co.id/search?keyword=pupuk%20kalsium")
driver.set_window_size(1300, 800)

rentang = 500
for i in range (1,9):
    akhir = rentang * i
    perintah = "window.scrollTo(0, "+str(akhir)+")"
    driver.execute_script(perintah)
    time.sleep(1)

time.sleep(5)

driver.save_screenshot("home.png")
content = driver.page_source
driver.close()

data = BeautifulSoup(content,'html.parser')
#print(data.encode("utf-8"))
list_nama, list_harga, list_terjual,list_kota,list_link = [],[],[],[],[]
base = "https://shopee.co.id"
for item in data.find_all('div', class_="col-xs-2-4 shopee-search-item-result__item"):
    print(i)
    nama = item.find('div', class_="ie3A+n bM+7UW Cve6sh").get_text()
    harga =item.find('div', class_="vioxXd rVLWG6").get_text() 
    terjual = item.find('div', class_="r6HknA uEPGHT")
    if terjual != None:
        terjual = terjual.get_text()
    kota = item.find('div', class_="zGGwiV").get_text() 
    link = base + item.find('a')['href']
    
    list_nama.append(nama)
    list_harga.append(harga)
    list_terjual.append(terjual)
    list_kota.append(kota)
    list_link.append(link)

df = pd.DataFrame({'Nama': list_nama, 'Harga':list_harga, 'Terjual':list_terjual, 'Kota':list_kota, 'Link':list_link})
df.to_csv('Pupuk Kalsium.csv', index=False)


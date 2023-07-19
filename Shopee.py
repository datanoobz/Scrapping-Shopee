from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome()
driver.set_window_size(1300, 800)

base_url = "https://shopee.co.id/search?keyword=organik%20cair&page="
all_data_nama, all_data_harga,all_data_terjual, all_data_kota,all_data_link =[],[],[],[],[]
for i in range (0,6):
    url = base_url + str(i)
    driver.get(url)
    rentang = 500
    time.sleep(3)
    for i in range (1,10):
        akhir = rentang * i
        perintah = "window.scrollTo(0, "+str(akhir)+")"
        driver.execute_script(perintah)
        time.sleep(0.5)
    time.sleep(10)

    content = driver.page_source
    data = BeautifulSoup(content,'html.parser')
    list_nama, list_harga, list_terjual,list_kota,list_link = [],[],[],[],[]
    base = "https://shopee.co.id"
    for item in data.find_all('div', class_="col-xs-2-4 shopee-search-item-result__item"):
            print(i)
            nama = item.find('div', class_="ie3A+n bM+7UW Cve6sh")
            if nama != None:
                nama = nama.get_text()
            harga =item.find('div', class_="vioxXd rVLWG6")
            if harga != None:
                harga = harga.get_text()
            terjual = item.find('div', class_="r6HknA uEPGHT")
            if terjual != None:
                terjual = terjual.get_text()

            kota = item.find('div', class_="zGGwiV") 
            if kota != None:
                kota = kota.get_text()
            link = base + item.find('a')['href']
            if link != None:
                link = link
            
            list_nama.append(nama)
            list_harga.append(harga)
            list_terjual.append(terjual)
            list_kota.append(kota)
            list_link.append(link)

    all_data_nama.extend(list_nama)
    all_data_harga.extend(list_harga)
    all_data_terjual.extend(list_terjual)
    all_data_kota.extend(list_kota)
    all_data_link.extend(list_link)

df = pd.DataFrame({'Nama': all_data_nama, 'Harga':all_data_harga, 'Terjual':all_data_terjual, 'Kota':all_data_kota, 'Link': all_data_link})
df.to_csv('Organik Cair.csv', index=False)

driver.close()

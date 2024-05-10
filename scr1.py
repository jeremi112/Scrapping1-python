from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

opsi = webdriver.ChromeOptions()
opsi.add_argument('--headless')
# opsi.add_argument('log-level=3')
servis = Service('chromedriver.exe')
driver = webdriver.Chrome(service=servis,options=opsi)

shopee_link='https://www.lazada.co.id/catalog/?q=redmi'
driver.set_window_size(1300,800)
driver.get(shopee_link)
time.sleep(10)

driver.save_screenshot('home.png')

content = driver.page_source


# driver.quit()



data = BeautifulSoup(content,'html.parser')
# print(data.encode('utf-8'))


list_nama,list_harga,list_sold,list_locations=[],[],[],[]
i=1
for area in data.find_all('div',class_='Bm3ON'):
    
    print(i)
    nama_barang= area.find('div',class_='RfADt').get_text()
    harga_barang= area.find('span',class_='ooOxS').get_text().replace('Rp','')
    area_span = area.find('span', class_='_1cEkb')  # Cari elemen span pertama
    if area_span is not None:
        sold_out = area_span.find('span').get_text().replace('sold', '')  # Cari elemen span di dalamnya
    # Lakukan operasi lanjutan dengan sold_out
    else:
        sold_out = None  # Atau lakukan sesuai kebutuhan jika objek tidak ditemukan
    tempat = area.find('span',class_='oa6ri').get_text()
    
    list_nama.append(nama_barang)
    list_harga.append(harga_barang)
    list_sold.append(sold_out)
    list_locations.append(tempat)
    print(nama_barang)
    print(harga_barang)
    print(sold_out)
    print(tempat)
    
    i+=1
    print('------------------------------')
 
print(list_nama)
print(list_harga)
print(list_sold)
print(list_locations)


 
# Membuat DataFrame
df = pd.DataFrame({'nama barang': list_nama, 'harga': list_harga, 'terjual': list_sold, 'lokasi': list_locations})

# Menyimpan ke file Excel
df.to_excel('ScrapHp2.xlsx', sheet_name='Sheet1', index=False)
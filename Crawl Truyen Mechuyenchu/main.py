import threading
import time
import requests
import Libary
import html5lib
from bs4 import BeautifulSoup as BS
url='https://metruyenchu.com/truyen/dinh-cap-khi-van-lang-le-tu-luyen-ngan-nam'
l=int(BS(requests.get(url).text,'html5lib').find('div',class_='font-weight-semibold h4 mb-1').text)
x1=int(l*0.25)
x2=int(l*0.5)
x3=int(l*0.75)
Libary.SaveFoder()
def Crawl(url,a,b):
    try:
        for j in range(a,b):
            soup=BS(requests.get(f'{url}/chuong-{j}').text,'html5lib')
            text=str(soup.find(id='js-read__content').text).replace('"' ,'\n')
            Libary.GhiFileCode(f'chuong{j}',text)
    except:
        return
def Runtime (i):
    print(f'THREAD {i} RUNING')
    try:
        if i%4==0:
            Crawl(url,1,x1)
        elif i%4==1 :
            Crawl(url,x1,x2)
        elif i%4==2 :
            Crawl(url,x2,x3)
        elif i%4==3 :
            Crawl(url,x3,l)
        time.sleep(1)
    except:
        print(f'TOO MANY REQUESTS IN THREAD {i}')
    print(f'THREAD {i} END')
    
soluorg =4
threats =[]
for i in range(soluorg):
    threats += [threading.Thread(target=Runtime,args={i})]
for t in threats:
    t.start()
for t in threats:
    t.join()
print('end')
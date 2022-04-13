import threading,time,requests,Libary, html5lib
from bs4 import BeautifulSoup as BS
def Chuong():
    try:
        l=int(BS(requests.get(url).text,'html5lib').find('div',class_='font-weight-semibold h4 mb-1').text)
        return int(l*0.25),int(l*0.5),int(l*0.75),l
    except:
        print('URL KHONG TON TAI')

def Crawl(url,a,b):
    ten=str(url).split("/")[4]
    try:
        for j in range(a,b):
            soup=BS(requests.get(f'{url}/chuong-{j}').text,'html5lib')
            text=str(soup.find(id='js-read__content').text)
            Libary.GhiFileCode(f'{ten}-chuong{j}',text)
    except:
        print('TOO MANY REQUESTS IN ')
def Runtime (i):
    print(f'THREAD {i} RUNING')
    try:
        if i%4==0:
            time.sleep(i)
            Crawl(url,1,x1)
        elif i%4==1 :
            time.sleep(i)
            Crawl(url,x1,x2)
        elif i%4==2 :
            time.sleep(i)
            Crawl(url,x2,x3)
        elif i%4==3 :
            time.sleep(i)
            Crawl(url,x3,l+1)
        time.sleep(1)
    except:
        print(f'TOO MANY REQUESTS IN THREAD {i}')
    print(f'THREAD {i} END')
def Thread3():   
    soluorg =4
    threats =[]
    for i in range(soluorg):
        threats += [threading.Thread(target=Runtime,args={i})]
    for t in threats:
        t.start()
    for t in threats:
        t.join()
    print('THREAD END')
def Thread1():
    for i in range(1,4):
        Runtime(i)
if __name__ == '__main__':
    Libary.SaveFoder()
    try:
        url=input('NHAP URL TRUYEN MECHUYENCHU.COM :')
        x1,x2,x3,l=Chuong() 
        Thread3()
    except:
        print(f'LOI : {url}')

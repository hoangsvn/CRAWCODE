import threading,time,requests,Libary, html5lib
from bs4 import BeautifulSoup as BS

def Chuong(th):
    try:
        li=[]
        l=int(BS(requests.get(url).text,'html5lib').find('div',class_='font-weight-semibold h4 mb-1').text)
        for i in range(th):
            li.append(int((l*i)/(th-1)))
        time.sleep(1)
        return li
    except:
        print('URL KHONG TON TAI')

def Crawl(url,i):
    ten=str(url).split("/")[4]
    try:
        for j in range(list[i-1],list[i]):
            try:
                soup=BS(requests.get(f'{url}/chuong-{j}').text,'html5lib')
                text=str(soup.find(id='js-read__content').text)
                Libary.GhiFileCode(f'{ten}-chuong-{j}',text)
            except:
                continue
    except:
        print(f'TOO MANY REQUESTS IN THREAD {i}')

def Runtime (i):
    # time.sleep(i)
    Crawl(url,i)


def Thread(th):   
    threats =[]
    for i in range(1,th):
        threats += [threading.Thread(target=Runtime,args={i})]
    for t in threats:
        t.start()
    for t in threats:
        t.join()
    print('THREAD END')

if __name__ == '__main__':
    Libary.SaveFoder()
    try:
        url=input('NHAP URL TRUYEN MECHUYENCHU.COM :') 
        th=int('NHAP SO LUONG CHAY  0 < : < 50 : ') or 25
        list=Chuong(th)
        Thread(th)
    except:
        print(f'ERROR : {url}')

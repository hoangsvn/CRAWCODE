from requests import Session
from bs4 import BeautifulSoup as BS
from threading import Thread
from time import sleep
from Libary import GhiFileCode, History, SaveFolder


def Login():
    log=False
    usname= input('NHAP TAI KHOAN CODEPTIT : ') or 'B19DCAT079'
    passwd= input('NHAP PASSWORD  CODEPTIT : ') or '02042001'
    try:
        with Session() as s:
            url = 'https://code.ptit.edu.vn/login'
            brower = s.get(url=url)
            conten = BS(brower.content, 'html.parser')
            token = conten.find('input', {'name': '_token'})['value']
            data = {'username': usname, 'password': passwd, '_token': token}
            a=s.post(url=url, data=data)
            if a.url=='https://code.ptit.edu.vn/student/question':
                log=True
    except:
        print('ERROR NO INTERNET CONNECTION')
    return log,s


def CrawlCode(x,a):
    try:
        s2 = a.get("https://code.ptit.edu.vn/student/question?page="+str(x))
        sleep(delay)
        list = []
        for i in BS(s2.content, 'html.parser').find_all('tr', {'class': 'bg--10th'}):
            url = BS(a.get(url=i.find('a')['href']).content, 'html.parser').find('td', {'class': 'text-center'}).find('a')['href']
            sleep(delay)
            editcode = BS(a.get(url=url).content, 'html.parser')
            loai=int(editcode.find('option',{'selected':'selected'})['value'])
            name=editcode.find('input',{'type':'hidden','name':'question'})['value']
            soure=editcode.find('input', {'id': 'source_code', 'name': 'source_code'})['value']
            History(editcode.find('a', {'class': 'link--red'}).text)
            GhiFileCode(name,soure.strip(),loai)
            sleep(delay)        
    except:
        print('TOO MANY REQUESTS ')

def Runtime(i,S):
    print(f'THREAD {i} RUNING')
    CrawlCode(i+1,S)
    print(f'THREAD {i} END')

def Thread3(S):
    soluorg = 3
    threats = []
    for i in range(soluorg):
        threats += [Thread(target=Runtime, args={i,S})]
    for t in threats:
        t.start()
    for t in threats:
        t.join()


def Thread1(S):
    for i in range(0, 4):
        Runtime(i)


if __name__ == '__main__':
    T,S=Login()
    if T :
        Folder=SaveFolder()
        print('LOGIN SUCCESSUFUL')
        A = input('SPEED 3X PRESS ANY OR 1X PRESS 0 : ')
        if A != '1':
            delay = 2.5
            print('SPEED 3X')
            Thread3(S)
        else:
            print('SPEED 1X')
            delay=1.5
            Thread1(S)
        print(f'DATACODE IN {Folder} ')
        sleep(10)
    else :
        print('LOGIN FAILED EXIT AFTER 5 SECONDS')
        sleep(5)
    


from requests import Session
from bs4 import BeautifulSoup as BS
from threading import Thread
from time import sleep
from Libary import GhiFileCode, History, SaveFolder

delay=2.5
def Login():
    log=False
    usname= input('NHAP TAI KHOAN CODEPTIT : ') 
    passwd= input('NHAP PASSWORD  CODEPTIT : ') 
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
                A=BS(s.get(a.url).content,'html.parser').find('p',{'class':'nav__profile__menu__name'}).text
                sleep(1)
                print(f'HELLO : {A.upper()}')
    except:
        print('ERROR NO INTERNET CONNECTION')
    return log,s


def CrawlCode(x,a):
    try:
        try:
            s2 = a.get("https://code.ptit.edu.vn/student/question?page="+str(x))
            listb=BS(s2.content, 'html.parser').find_all('tr', {'class': 'bg--10th'})
        except:
            return
        sleep(delay)
        if len(listb)>0:
            for i in listb:
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
    try:
        sleep(i)
        CrawlCode(i,S)
        CrawlCode(int(i+3),S)
    except:
        return
soluorg = 4

def Thread3(S):
    threats = []
    for i in range(1,soluorg):
        threats += [Thread(target=Runtime, args={i,S})]
    for t in threats:
        t.start()
    for t in threats:
        t.join()


if __name__ == '__main__':
    T,S=Login()
    if T :
        Folder=SaveFolder()
        print('LOGIN SUCCESSUFUL')
        print('RUNING ')
        Thread3(S)
        print(f'DATACODE IN {Folder} ')
        sleep(5)
    else :
        print('LOGIN FAILED EXIT AFTER 5 SECONDS')
        sleep(5)
    
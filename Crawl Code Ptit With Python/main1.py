from requests import Session
from bs4 import BeautifulSoup as BS
from threading import Thread
from time import sleep
from Libary import GhiFileCode, History, SaveFolder

delay = 3


def Login():
    loginsuccessful=False
    usname=input('NHAP TAI KHOAN CODEPTIT : ')
    passwd=input('NHAP PASSWORD  CODEPTIT : ')
    try:
        with Session() as s:
            url = 'https://code.ptit.edu.vn/login'
            brower = s.get(url=url)
            conten = BS(brower.content, 'html.parser')
            token = conten.find('input', {'name': '_token'})['value']
            data = {'username': usname, 'password': passwd, '_token': token}
            a=s.post(url=url, data=data)
            if a.url=='https://code.ptit.edu.vn/student/question':
                loginsuccessful=True
    except:
        print('ERROR')
    return loginsuccessful,s


def Listbai(x,a):
    try:
        s2 = a.get("https://code.ptit.edu.vn/student/question?page="+str(x))
        sleep(delay)
        list = []
        for i in BS(s2.content, 'html.parser').find_all('tr', {'class': 'bg--10th'}):
            list.append(str(i.text).split()[2])
        return list
    except:
        print('ERROR')


def Crawl(i,a):
    try:
        list = Listbai(i,a)
        for I in list:
            bai = BS(a.get("https://code.ptit.edu.vn/student/question/"+I).content,
                     'html.parser').find('td', {'class': 'text--middle'}).text
            sleep(delay)
            url1 = 'https://code.ptit.edu.vn/student/solution/'+bai+'/edit'
            bai = BS(a.get(url=url1).content, 'html.parser')
            History(bai.find('a', {'class': 'link--red'}).text)
            GhiFileCode(I, bai.find(
                'input', {'id': 'source_code', 'name': 'source_code'})['value'])
            sleep(delay)
    except:
        print('ERROR')


def Runtime(i,s):

    print(f'THREAD {i} RUNING')
    try:
        Crawl(i+1,s)
    except:
        print(f'TOO MANY REQUESTS IN THREAD {i}')
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


# def Checklogin():
#     b,a=Login()
#     print(b)
# if __name__ == '__main__':
#     usname=input('NHAP TAI KHOAN CODEPTIT : ')
#     passwd=input('NHAP PASSWORD  CODEPTIT : ')
#     Checklogin()

if __name__ == '__main__':
    T,S=Login()
    if T :
        Folder=SaveFolder()
        print('LOGIN SUCCESSUFUL')
        A = input('SPEED 3X PRESS ANY OR 1X PRESS 0 : ')
        if A != '1':
            print('SPEED 3X')
            Thread3(S)
        else:
            print('SPEED 1X')
            Thread1(S)
        print(f'DATACODE IN {Folder} ')
    else :
        print('LOGIN FAILED')

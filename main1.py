from warnings import catch_warnings
from requests import Session
from bs4 import BeautifulSoup as BS
from threading import Thread
from time import sleep 
from Libary import GhiFileCode,History,SaveFolder
from os import environ
from dotenv import load_dotenv
load_dotenv()

delay=3
def Login():
    try:
        with Session() as s:
            url='https://code.ptit.edu.vn/login'
            brower=s.get(url=url)
            conten=BS(brower.content,'html.parser')
            token=conten.find('input',{'name':'_token'})['value']
            data={'username': environ.get('login__user')  ,'password': environ.get('login__pw'),'_token':token}
            s.post(url=url,data=data)
    except:
        print('ERROR')
    return s
def Listbai(x):
    try:
        a=Login()
        s2=a.get("https://code.ptit.edu.vn/student/question?page="+str(x))
        sleep(delay)
        list=[]
        for i in BS(s2.content,'html.parser').find_all('tr',{'class':'bg--10th'}):
            list.append(str(i.text).split()[2])
        return a,list
    except:
        print('ERROR')
def Crawl(i):
    try:
        a,list=Listbai(i)
        for I in list:
            bai=BS(a.get("https://code.ptit.edu.vn/student/question/"+I).content,'html.parser').find('td',{'class':'text--middle'}).text
            sleep(delay)
            url1='https://code.ptit.edu.vn/student/solution/'+bai+'/edit'
            bai=BS(a.get(url=url1).content,'html.parser')
            History(bai.find('a',{'class':'link--red'}).text)
            GhiFileCode(I,bai.find('input',{'id':'source_code','name':'source_code'})['value'])
            sleep(delay)
    except:
        print('ERROR')


def Runtime (i):
    print(f'THREAD {i} RUNING')
    try:
        Crawl(i+1)
    except :
        print(f'TOO MANY REQUESTS IN THREAD {i}')
    print('END')
def Thread3():
    soluorg =3
    threats =[]
    for i in range(soluorg):
        threats += [Thread(target=Runtime,args={i})]
    for t in threats:
        t.start()
    for t in threats:
        t.join()
def Thread1():
    for i in range(0,4):
        Runtime(i)
if __name__ == '__main__':
    SaveFolder()
    A=input('Chay 3 luong hay 1 luong  yes=1/no=0 recommand = 0 :')
    if A=='1':
        Thread3()
    else :
        Thread1()
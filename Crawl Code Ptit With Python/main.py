from os import getenv,system
from time import sleep
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from Libary import History,GhiFileCode,Error,SaveFolder
load_dotenv(dotenv_path='.env')
def LoginPTIT(brower):
    try:
        brower.find_element_by_id("login__user").send_keys(getenv('login__user'))
        password = brower.find_element_by_id("login__pw")
        password.send_keys(getenv('login__pw'))
        system('cls')
        password.send_keys(Keys.ENTER)
    except:
        return
def Listbai(brower,x):
    try:
        List=[]
        brower.get("https://code.ptit.edu.vn/student/question?page="+str(x))
        crawl = brower.find_elements_by_class_name("bg--10th")
        for i in range(len(crawl)):
            List.append(crawl[i].find_element_by_xpath("td[3]/a").text)
        system('cls')
        return List
    except:
        return
def Crawl(brower,x,timedelay):
    try:
        m=0
        list=Listbai(brower,x)
        Len=len(list)
        for Bai in list:
            m+=1
            brower.get("https://code.ptit.edu.vn/student/question/"+Bai)
            sleep(timedelay)
            print(f'Thread {x} runing : {int(m*100/Len)} %')
            TAB = brower.find_elements_by_class_name("card-body")
            if len(TAB) > 0:
                if len(TAB[0].find_elements_by_class_name("text--middle")) > 0:
                    brower.get(TAB[0].find_element_by_xpath("div[1]/table/tbody/tr[1]/td[4]/a").get_attribute("href"))
                    sleep(timedelay)
                    source = brower.find_element_by_name("source_code")
                    GhiFileCode(Bai, source.get_attribute("value"))
                    system('cls')
                    History(brower.find_element_by_class_name("submit__nav").find_element_by_xpath("p/a").text)
                else:
                    Error(Bai)
        sleep(1)
    except:
        return
def Runtime (i):
    print(f'Thread {i} runing')
    if i==0:
        system('cls')
    else:
        Options=webdriver.ChromeOptions()
        driver = webdriver.Chrome(executable_path='D:\VEN\chromedriver.exe',options=Options)
        driver.set_window_size(60,300)
        driver.set_window_position(i*100,0)
        driver.get('https://code.ptit.edu.vn')
        LoginPTIT(driver)
        Crawl(driver,i,2)
        sleep(1)

def Thread3():
    soluorg =4
    threats =[]
    for i in range(soluorg):
        threats += [Thread(target=Runtime,args={i})]
    for t in threats:
        t.start()
    for t in threats:
        t.join()
def Thread1():
    for i in range(1,4):
        Runtime(i)

if __name__ == '__main__':
    SaveFolder()
    A = input('SPEED 3X PRESS ANY 1X PRESS 0 : ')
    if A != '1':
        print('SPEED 3X')
        Thread3()
    else:
        print('SPEED 1X')
        Thread1()
import os
import time
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from Libary import History,GhiFileCode,Error
load_dotenv(dotenv_path='.env')
def LoginPTIT(brower):
    brower.find_element_by_id("login__user").send_keys(os.environ.get('login__user'))
    password = brower.find_element_by_id("login__pw")
    password.send_keys(os.environ.get('login__pw'))
    os.system('cls')
    password.send_keys(Keys.ENTER)
def Listbai(brower,x):
    List=[]
    brower.get("https://code.ptit.edu.vn/student/question?page="+str(x))
    crawl = brower.find_elements_by_class_name("bg--10th")
    for i in range(len(crawl)):
        List.append(crawl[i].find_element_by_xpath("td[3]/a").text)
    os.system('cls')
    return List
def Crawl(brower,x,timedelay):
    m=0
    list=Listbai(brower,x)
    Len=len(list)
    for Bai in list:
        m+=1
        brower.get("https://code.ptit.edu.vn/student/question/"+Bai)
        time.sleep(timedelay)
        print(f'Thread {x} runing : {int(m*100/Len)} %')
        TAB = brower.find_elements_by_class_name("card-body")
        if len(TAB) > 0:
            if len(TAB[0].find_elements_by_class_name("text--middle")) > 0:
                brower.get(TAB[0].find_element_by_xpath("div[1]/table/tbody/tr[1]/td[4]/a").get_attribute("href"))
                time.sleep(timedelay)
                source = brower.find_element_by_name("source_code")
                GhiFileCode(Bai, source.get_attribute("value"))
                os.system('cls')
                History(brower.find_element_by_class_name("submit__nav").find_element_by_xpath("p/a").text)
            else:
                Error(Bai)
    time.sleep(1)
def Runtime (i):
    print(f'Thread {i} runing')
    if i==0:
        os.system('cls')
    else:
        Options=webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=Options)
        driver.set_window_size(60,300)
        driver.set_window_position(i*100,0)
        driver.get('https://code.ptit.edu.vn')
        LoginPTIT(driver)
        Crawl(driver,i,2)
        time.sleep(1)

def Thread3():
    soluorg =4
    threats =[]
    for i in range(soluorg):
        threats += [threading.Thread(target=Runtime,args={i})]
    for t in threats:
        t.start()
    for t in threats:
        t.join()
def Thread1():
    for i in range(1,4):
        Runtime(i)

if __name__ == '__main__':
    A=input('Chay 3 luong hay 1 luong  yes=1/no=0 recommand = 0 :')
    if A=='1':
        Thread3()
    else :
        Thread1()
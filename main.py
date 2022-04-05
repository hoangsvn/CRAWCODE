
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from Libary import *


# loadDrive
def LoadDrive():
    return webdriver.Chrome(executable_path="./chromedriver.exe")
# KhoiChay Chrome


def RunChrome():
    brower.set_window_position(0,0)
    brower.set_window_size(50,50)
    brower.get("https://code.ptit.edu.vn")
    SaveFolder()
# LoginPTITcode


def LoginPTIT():
    sleep(1)
    brower.find_element_by_id("login__user").send_keys("B19DCAT079")
    password = brower.find_element_by_id("login__pw")
    password.send_keys("02042001")
    password.send_keys(Keys.ENTER)
    sleep(1)
    if len(brower.find_elements_by_class_name("text--red")) == 1:
        Clearcmd()
        print("Tài khoản hoặc mật khẩu không hợp lệ.".upper())
        return False
    else:
        return True


def ListTenbai():
    List = []
    for i in range(1, 4):
        brower.get("https://code.ptit.edu.vn/student/question?page="+str(i))
        crawl = brower.find_elements_by_class_name("bg--10th")
        for i in range(len(crawl)):
            List.append(crawl[i].find_element_by_xpath("td[3]/a").text)
    return List


def CrawlCode():
    Count = 0
    ListName = ListTenbai()
    lenlist = len(ListName)
    for Bai in ListName:
        Count += 1
        brower.get("https://code.ptit.edu.vn/student/question/"+Bai)
        sleep(1)
        TAB = brower.find_elements_by_class_name("card-body")
        TrangThai(Count, lenlist)
        if len(TAB) > 0:
            if len(TAB[0].find_elements_by_class_name("text--middle")) > 0:
                brower.get(TAB[0].find_element_by_xpath("div[1]/table/tbody/tr[1]/td[4]/a").get_attribute("href"))
                sleep(1)
                source = brower.find_element_by_name("source_code")
                GhiFileCode(Bai, source.get_attribute("value"))
                History(brower.find_element_by_class_name("submit__nav").find_element_by_xpath("p/a").text)
            else:
                Error(Bai)
    sleep(1)
    return


if __name__ == '__main__':
    brower = LoadDrive()
    RunChrome()
    if LoginPTIT():
        CrawlCode()
    brower.close()

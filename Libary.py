from os import system
from datetime import datetime

profile='\n# Nguoi viet : Nguyen Xuan Hoang \n# Date : 05/04/2022\n# Email : hoangnxb19dcat079.gmail.com\n'
end ='\n# Oke nha\n'


Save_Code = 1
Save_History = 1


def Clearcmd():
    system('cls')


def SaveFolder():
    system("md Data")


def Delete():
    system("rmdir /q /s Data")


def GhiFileCode(name, string):
    if Save_Code == 1:
        path= "Data/"+name+".py"
        with open(path, 'w+', encoding='utf-8') as File:
            File.write(profile+string+end)



def History(string):
    if Save_History == 1:
        path = "Data/history.txt"
        with open(path, 'a+', encoding='UTF-8') as File:
            File.write(f'{string} LƯA VÀO NGÀY {datetime.now()}\n')


def Error(string):
    if Save_History == 1:
        path = "Data/history.txt"
        with open(path, 'a+', encoding='UTF-8') as File:
            File.write(f'{string} CHƯA LÀM HOẶC LÀM SAI LƯA VÀO NGÀY {datetime.now()}\n')


def TrangThai(a, b):
    Clearcmd()
    if a != b:
        print(f'<=================[RUNING {int((a/b)*100)} % ]=================>')
    else:
        print(f'<=================[SAVE FOlDER DATA]=================>')

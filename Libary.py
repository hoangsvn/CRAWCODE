from os import system, environ
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()
Save_Code = int(environ.get('Save_Code'))
Save_History = int(environ.get('Save_History'))
Folder_path = environ.get('Folder_path')
profile='\n# Nguoi viet : Nguyen Xuan Hoang \n# Date : 05/04/2022\n# Email : hoangnxb19dcat079.gmail.com\n'
endfile ='\n# Oke nha\n'

def Clearcmd():
    system('cls')


def SaveFolder():
    cmd = f'md {Folder_path}'
    system(cmd)


def Delete():
    cmd = f'rmdir /q /s {Folder_path}'
    system(cmd)


def GhiFileCode(name, string):
    if Save_Code == 1:
        path = f'{Folder_path}/{name}.py'
        with open(path, 'w+', encoding='utf-8') as File:
            File.write(profile+string+endfile)


def History(string):
    if Save_History == 1:
        path = f'{Folder_path}/history.txt'
        with open(path, 'a+', encoding='UTF-8') as File:
            File.write(f'{string} LƯA VÀO NGÀY {datetime.now()}\n')


def Error(string):
    if Save_History == 1:
        path = f'{Folder_path}/history.txt'
        with open(path, 'a+', encoding='UTF-8') as File:
            File.write(
                f'{string} CHƯA LÀM HOẶC LÀM SAI LƯA VÀO NGÀY {datetime.now()}\n')


def TrangThai(a, b):
    Clearcmd()
    if a != b:
        print(f'<=================[RUNING {int((a/b)*100)} % ]=================>')
    else:
        print(f'<=================[SAVE FOlDER DATA]=================>')

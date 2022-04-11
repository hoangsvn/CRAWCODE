from os import environ,mkdir
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()
Save_Code =environ.get('Save_Code')
Save_History = environ.get('Save_History')
Folder_path = environ.get('Folder_path')
profile='\n# Nguoi viet : Nguyen Xuan Hoang \n# Date : 05/04/2022\n# Email : hoangnxb19dcat079.gmail.com\n'
endfile ='\n# Oke nha\n'


def SaveFolder():
    try:
        mkdir(Folder_path)
    except:
        print(f'{Folder_path} Da ton tai')

def GhiFileCode(name, string):
    try:
        if Save_Code == '1':
            path = f'{Folder_path}/{name}.py'
            with open(path, 'w+', encoding='utf-8') as File:
                File.write(profile+string+endfile)
    except:
        return


def History(string):
    try:
        if Save_History == '1':
            path = f'{Folder_path}/history.txt'
            with open(path, 'a+', encoding='UTF-8') as File:
                File.write(f'{string} LƯA VÀO NGÀY {datetime.now()}\n')
    except:
        return


def Error(string):
    try:
        if Save_History == '1':
            path = f'{Folder_path}/history.txt'
            with open(path, 'a+', encoding='UTF-8') as File:
                File.write(
                    f'{string} CHƯA LÀM HOẶC LÀM SAI LƯA VÀO NGÀY {datetime.now()}\n')
    except:
        return

from os import mkdir
from datetime import datetime

Save_Code ='1'
Save_History = '1'
Folder_path = 'DATACODE'
profile='\n# Nguoi viet : Nguyen Xuan Hoang \n# Date : 05/04/2022\n# Email : hoangnxb19dcat079.gmail.com\n'
endfile ='\n# Oke nha\n'

def SaveFolder():
    try:
        mkdir(Folder_path)
    except:
        print(f'{Folder_path} DA TON TAI')
    return Folder_path

def GhiFileCode(name, string,loai):
    list=['.cpp','','','.java','.py']
    try:
        if Save_Code == '1':
            path = f'{Folder_path}/{name}{list[loai]}'
            with open(path, 'w+', encoding='utf-8') as File:
                if loai==4:
                    File.write(profile+string+endfile)
                else :
                    File.write(string)
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

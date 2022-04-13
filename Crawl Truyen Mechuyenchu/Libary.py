import os

Folder_path='DATA'
def SaveFoder():
    os.system('md DATA')
Save_Code=1
def GhiFileCode(name,string):
    if Save_Code == 1:
        path = f'{Folder_path}/{name}.docx'
        with open(path, 'w+', encoding='utf-8') as File:
            File.write(String(string))

def String(string):
    xau=''
    m=0
    for i in string.replace('"',' ').split():
        if m==15:
            xau+='\n'
            m=0
        xau=f'{xau} {i}'
        m+=1
    return str(xau)





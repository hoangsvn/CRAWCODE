from os import system
def piplist():
    list=system('pip list')
    return list
def Delete():
    piplist()
    A=input('Nhap ten can xoa :').lower()
    S=f'pip uninstall {A} -y'
    system(S)
Delete()

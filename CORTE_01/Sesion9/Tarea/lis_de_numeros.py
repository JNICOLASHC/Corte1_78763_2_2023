#lsita de numeros incluidos 
import random as r

def list():
    num=[]
    a=int(input('ingrese un numero a  la lista:\n'))
    while a>=0:
        num.append(a)
        a=int(input('Ingrece otro numero:\n'))
        print('la lista de numeros es:\n',num)

if __name__=='__main__':
    list()


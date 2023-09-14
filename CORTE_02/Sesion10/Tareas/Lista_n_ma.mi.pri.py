#lista de 10 numeros luego me muestra el menor y mayor 
from random import randint as r 
import numpy as np 
def inicio(lista):
    li(lista)
def li(lista):
    for i in range(10):
        lista.append(r(1,50))
    print(lista)
    return lista

def MaMe(lista):
    l=np.sort(lista,axis=None)
    Ma=l[0];Me=l[-1]
    print('El numero menor de la lista es:\n',Ma,);print('El numero mayor de la lista es:\n',Me)
if __name__=='__main__':
    lista=[]
    li(lista)
    MaMe(lista)
    inicio=()
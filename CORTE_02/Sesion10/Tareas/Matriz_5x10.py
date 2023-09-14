#matriz 5x10 con numeros aleatorios que se organiza los dijitos 
from random import randint as r 
import numpy as np

def Ma(filas,columnas):
    matriz=[]
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(r(0,100))
        print(matriz[i])
    return matriz
def mn(matriz):
    ma=matriz[0][0]
    me=matriz[0][0]
    for i in range(5):
        for j in range(10):
            if matriz[i][j]<me:
                me=matriz[i][j]
            if matriz[i][j]>ma:
                ma=matriz[i][j]
    print('El numero menor de la matriz es:\n',me)
    print('El numero mayor de la matriz es:\n',ma)

def orden(matriz):
        m=np.sort(matriz,axis=None)
        print('La matriz ordenada quedo asi:\n',m)

if __name__=='__main__':
    filas=5
    columnas=10
    matriz=Ma(filas,columnas)
    mn(matriz)
    orden(matriz)


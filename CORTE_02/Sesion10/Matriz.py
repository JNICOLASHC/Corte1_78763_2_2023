
from random import randint as r 

def main(filas,columnas):
    matriz=[]
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(r(1,10))
        print(matriz[i])
    return matriz
def escalar(matriz):
    escalar=int(input('ingrese el escalar:\n'))
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j]*=escalar
        print(matriz[i])
if __name__=='__main__':
    filas = int(input('ingrece el nuemero de filas:\n'))
    columnas= int(input('ingrece el nuemero de columnas:\n'))
    print('-----original-----')
    matriz=main(filas,columnas)
    print('-----matriz escalada-----')
    escalar(matriz)

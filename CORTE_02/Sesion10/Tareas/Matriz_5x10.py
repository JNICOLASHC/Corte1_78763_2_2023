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

# Define una función llamada Ma que toma dos argumentos, filas y columnas
# Crea una matriz vacía
# Agrega filas a la matriz
# Agrega columnas a cada fila con números aleatorios entre 0 y 100 utilizando la función randint del módulo random
# Imprime cada fila de la matriz
# Devuelve la matriz

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

# Define una función llamada mn que toma un argumento llamado matriz
# Inicializa las variables ma y me con el primer elemento de la matriz
# Recorre la matriz y actualiza ma y me si encuentra un número mayor o menor
# Imprime el número menor y el número mayor de la matriz

def orden(matriz):
        m=np.sort(matriz,axis=None)
        print('La matriz ordenada quedo asi:\n',m)

# Define una función llamada orden que toma un argumento llamado matriz
# Utiliza la función np.sort de numpy para ordenar la matriz en orden ascendente
# Imprime la matriz ordenada

if __name__=='__main__':
    filas=5
    columnas=10
    matriz=Ma(filas,columnas)
    mn(matriz)
    orden(matriz)

# Si el script se ejecuta directamente (no se importa como un módulo), se ejecutan las siguientes líneas:
# Asigna los valores 5 y 10 a las variables filas y columnas, respectivamente
# Llama a la función Ma con filas y columnas como argumentos y asigna el resultado a la variable matriz
# Llama a la función mn con matriz como argumento
# Llama a la función orden con matriz como argumento


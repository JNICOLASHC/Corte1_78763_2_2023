
from random import randint as r

# Importa la función randint del módulo random y la renombra como r

def main(filas,columnas):
    matriz=[]
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(r(1,10))
        print(matriz[i])
    return matriz

# Define una función llamada main que toma dos argumentos, filas y columnas
# Crea una matriz vacía
# Agrega filas a la matriz
# Agrega columnas a cada fila con números aleatorios entre 1 y 10 utilizando la función randint del módulo random
# Imprime cada fila de la matriz
# Devuelve la matriz

def escalar(matriz):
    escalar=int(input('ingrese el escalar:\n'))
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j]*=escalar
        print(matriz[i])

# Define una función llamada escalar que toma un argumento llamado matriz
# Pide al usuario que ingrese un escalar
# Recorre la matriz y multiplica cada elemento por el escalar
# Imprime cada fila de la matriz actualizada

if __name__=='__main__':
    filas = int(input('ingrece el nuemero de filas:\n'))
    columnas= int(input('ingrece el nuemero de columnas:\n'))
    print('-----original-----')
    matriz=main(filas,columnas)
    print('-----matriz escalada-----')
    escalar(matriz)

# Si el script se ejecuta directamente (no se importa como un módulo), se ejecutan las siguientes líneas:
# Pide al usuario que ingrese el número de filas y columnas
# Imprime la cadena '-----original-----'
# Llama a la función main con filas y columnas como argumentos y asigna el resultado a la variable matriz
# Imprime la cadena '-----matriz escalada-----'
# Llama a la función escalar con matriz como argumento

#lista de 10 numeros luego me muestra el menor y mayor 
from random import randint as r
import numpy as np

# Importa la función randint del módulo random y la renombra como r
# Importa el módulo numpy y lo renombra como np

def inicio(lista):
    li(lista)

# Define una función llamada inicio que toma un argumento llamado lista
# Llama a la función li con el argumento lista

def li(lista):
    for i in range(10):
        lista.append(r(1,50))
    print(lista)
    return lista

# Define una función llamada li que toma un argumento llamado lista
# Agrega 10 números aleatorios entre 1 y 50 a la lista
# Imprime la lista
# Devuelve la lista

def MaMe(lista):
    l=np.sort(lista,axis=None)
    Ma=l[0];Me=l[-1]
    print('El numero menor de la lista es:\n',Ma,);print('El numero mayor de la lista es:\n',Me)

# Define una función llamada MaMe que toma un argumento llamado lista
# Utiliza la función np.sort de numpy para ordenar la lista en orden ascendente
# Asigna el primer elemento de la lista ordenada a la variable Ma y el último elemento a la variable Me
# Imprime el número menor y el número mayor de la lista

if __name__=='__main__':
    lista=[]
    li(lista)
    MaMe(lista)
    inicio=()

# Si el script se ejecuta directamente (no se importa como un módulo), se ejecutan las siguientes líneas:
# Crea una lista vacía llamada lista
# Llama a la función li con la lista como argumento
# Llama a la función MaMe con la lista como argumento
# Asigna un valor vacío a la variable inicio (esto no tiene ningún efecto en el código)

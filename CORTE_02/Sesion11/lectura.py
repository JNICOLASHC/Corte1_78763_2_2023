#codigo para leer un archivo 
def main_read():
    f=open('matrizAsignacion.txt','rt')
    documento=f.read()
    f.close()
    print(documento)

# Define una función llamada main_read
# Abre el archivo matrizAsignacion.txt en modo de lectura de texto y lo asigna a la variable f
# Lee todo el contenido del archivo y lo asigna a la variable documento
# Cierra el archivo
# Imprime el contenido del documento

def main_read2():
    f=open('matrizAsignacion.txt','rt')
    documento=f.readline().rstrip('\n').split(',')
    while documento !=[""]:
        print(documento)
        documento=f.readline().rstrip('\n').split(',')
    f.close()

# Define una función llamada main_read2
# Abre el archivo matrizAsignacion.txt en modo de lectura de texto y lo asigna a la variable f
# Lee la primera línea del archivo, elimina el carácter de nueva línea y divide la línea en una lista de elementos separados por comas
# Mientras la línea leída no sea una lista vacía, imprime la línea y lee la siguiente línea del archivo
# Cierra el archivo

def suma(lista):
    for dato in lista:
        resultado=int(dato[0])+int(dato[1])+int(dato[3])
        print(resultado)

# Define una función llamada suma que toma un argumento llamado lista
# Recorre cada elemento de la lista
# Convierte los elementos en las posiciones 0, 1 y 3 de cada sublista en enteros y los suma
# Imprime el resultado de la suma

def main_read3():
    f=open('matrizAsignacion.txt','rt')
    documento=f.readlines()
    f.close()
    lista=[]
    for dato in documento:
        lista.append(dato.rstrip('\n').split(','))
    print(lista)
    suma(lista)

# Define una función llamada main_read3
# Abre el archivo matrizAsignacion.txt en modo de lectura de texto y lo asigna a la variable f
# Lee todas las líneas del archivo y las asigna a la variable documento como una lista de cadenas
# Cierra el archivo
# Crea una lista vacía llamada lista
# Para cada cadena en el documento, elimina el carácter de nueva línea y divide la cadena en una lista de elementos separados por comas
# Agrega la lista resultante a la lista principal
# Imprime la lista principal
# Llama a la función suma con la lista principal como argumento

if __name__=='__main__':
    # main_read()
    # main_read2()
    main_read3()

# Si el script se ejecuta directamente (no se importa como un módulo), se ejecutan las siguientes líneas:
# Comenta las líneas main_read() y main_read2()
# Llama a la función main_read3()
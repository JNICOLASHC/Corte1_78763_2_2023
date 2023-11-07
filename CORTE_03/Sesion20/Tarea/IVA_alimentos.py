def selp():
    f=open("Alimentos.txt","rt")
    a = f.readlines()
    f.close
    lista = []
    for dato in a:
        lista.append(dato.rstrip("\n").split(","))
    print(lista)

# Define una función llamada selp
# Abre el archivo Alimentos.txt en modo de lectura de texto y lo asigna a la variable f
# Lee todas las líneas del archivo y las asigna a la variable a como una lista de cadenas
# Cierra el archivo
# Crea una lista vacía llamada lista
# Para cada cadena en la lista a, elimina el carácter de nueva línea y divide la cadena en una lista de elementos separados por comas
# Agrega la lista resultante a la lista principal
# Imprime la lista principal

def metodo():
    l = []

    with open('Alimentos.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split(',')
            l.append(parts[1].lower())

    while True:
        a = input("Ingrese el nombre del producto que compró o escriba 'salir' para terminar:\n").lower()

        if a == 'salir':
            break

        if a in l:
            pc = float(input(f"Ingrese el valor que le cobraron por el producto '{a}':\n"))
            index = l.index(a)
            iva = float(lines[index].split(',')[2])
            vsi = pc / (1 + iva)
            vaiva = pc - vsi
            print(f'El costo del alimento {a} es: {vsi}')
            print(f'El valor del IVA es: {vaiva}')
        else:
            print('El alimento ingresado no está en el menú o catálogo de alimentos.')

# Define una función llamada metodo
# Crea una lista vacía llamada l
# Abre el archivo Alimentos.txt en modo de lectura de texto y lo asigna a la variable f utilizando la declaración with para asegurarse de que el archivo se cierre correctamente
# Lee todas las líneas del archivo y las asigna a la variable lines como una lista de cadenas
# Para cada cadena en la lista lines, elimina los espacios en blanco al principio y al final de la cadena y divide la cadena en una lista de elementos separados por comas
# Agrega el segundo elemento de cada lista (el nombre del producto) en minúsculas a la lista l
# Mientras sea verdadero:
#   Solicita al usuario que ingrese el nombre de un producto o escriba 'salir' para terminar y lo convierte a minúsculas
#   Si el nombre del producto ingresado está en la lista l:
#     Solicita al usuario que ingrese el precio del producto y lo convierte a un número de punto flotante
#     Encuentra el índice del nombre del producto en la lista l
#     Obtiene el valor del IVA para el producto correspondiente en la lista lines
#     Calcula el valor sin IVA (vsi) dividiendo el precio del producto entre (1 + IVA)
#     Calcula el valor del IVA (vaiva) restando el valor sin IVA del precio del producto
#     Imprime el costo del alimento y el valor del IVA
#   De lo contrario:
#     Imprime un mensaje indicando que el alimento ingresado no está en el menú o catálogo de alimentos

if __name__ == '__main__':
    selp()
    metodo()

# Si el script se ejecuta directamente (no se importa como un módulo), se ejecutan las siguientes líneas:
# Llama a la función selp
# Llama a la función metodo
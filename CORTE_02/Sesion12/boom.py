#funcion recursiva 
def boom(x):
    if x > 0:
        print(x)
        boom(x - 1)
    else:
        print('booooommmm!!!!')
    print(f'finalizo{x}')

# Define una función llamada boom que toma un argumento x
# Si x es mayor que 0, imprime el valor de x y luego llama a la función boom con el argumento x-1
# Si x es menor o igual a 0, imprime "booooommmm!!!!"
# Imprime "finalizo" seguido del valor de x

def main():
    boom(5)

# Define una función llamada main que no toma argumentos
# Llama a la función boom con el argumento 5

if __name__ == '__main__':
    main()

# Si este archivo se está ejecutando como un programa principal (no se está importando como un módulo),
# llama a la función main
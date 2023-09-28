class Pokemon():
    def __init__(self):
        self.nombre=None  # Define una variable "nombre" en la instancia de la clase "Pokemon"
        self.color=None   # Define una variable "color" en la instancia de la clase "Pokemon"
        self.categoria=None  # Define una variable "categoria" en la instancia de la clase "Pokemon"
        self.tipo=None    # Define una variable "tipo" en la instancia de la clase "Pokemon"
        self.codigo=None  # Define una variable "codigo" en la instancia de la clase "Pokemon"
    
    def ataquePokemon(self):
        return 'estoy atacando'  # Define una función "ataquePokemon" que devuelve un mensaje de ataque

def main():
    pokemones=[]  # Crea una lista vacía llamada "pokemones"
    opc='n'  # Define una variable "opc" con el valor "n"
    while 1:  # Inicia un bucle infinito
        pokemon=Pokemon()  # Crea una instancia de la clase "Pokemon" llamada "pokemon"
        pokemon.nombre=input('Nombre del pokemon: ')  # Pide al usuario que ingrese el nombre del pokemon y lo asigna a la variable "nombre" de la instancia "pokemon"
        pokemon.categoria=input('Categoria del pokemon: ')  # Pide al usuario que ingrese la categoría del pokemon y lo asigna a la variable "categoria" de la instancia "pokemon"
        pokemon.color=input('Color del pokemon: ')  # Pide al usuario que ingrese el color del pokemon y lo asigna a la variable "color" de la instancia "pokemon"
        pokemon.tipo=input('tipo del pokemon: ')  # Pide al usuario que ingrese el tipo del pokemon y lo asigna a la variable "tipo" de la instancia "pokemon"
        pokemon.codigo=input('Codigo del pokemon: ')  # Pide al usuario que ingrese el código del pokemon y lo asigna a la variable "codigo" de la instancia "pokemon"
        pokemones.append(pokemon)  # Agrega la instancia "pokemon" a la lista "pokemones"

        opc=input('Desea inscribir otro pokemon (y/n): ')  # Pide al usuario que ingrese "y" o "n" y lo asigna a la variable "opc"
        if opc=='n':  # Si el usuario ingresa "n", sale del bucle
            break
        elif opc!='y':  # Si el usuario ingresa algo diferente de "y" o "n", muestra un mensaje de error
            print('Opcion invalida')
    
    print('\n---------Pokedex----------')  # Muestra un encabezado para la lista de pokemones
    for i in pokemones:  # Inicia un bucle que recorre la lista "pokemones"
        print(f'Nombre: {i.nombre}\n'
            f'Tipo: {i.tipo}\n'
            f'Codigo: {i.codigo}\n'
            f'Ataca! ... {i.ataquePokemon()}\n'
            '--------------------------')  # Muestra el nombre, tipo, código y mensaje de ataque de cada pokemon en la lista

if __name__=="__main__":
    main()  # Llama a la función "main" si el programa se ejecuta directamente (no se importa como módulo)
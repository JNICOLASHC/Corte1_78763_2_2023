#¿Es mayor de edad o no?

class Ciudadano():
    def _init_(self):
        self.__nombre = None
        self.__cedula = None
        self.__edad = None

    def setNombre(self, nombre: str):
        self.__nombre = nombre

    def setCedula(self, cedula):
        if 8 <= len(str(cedula)) <= 10:
            self.__cedula = cedula
        else:
            print("La cédula debe tener entre 8 y 10 dígitos.")

    def setEdad(self, edad: int):
        if edad > 0:
            self.__edad = edad
        else:
            print('La edad debe ser un número mayor a 0 y positivo.')

    def getNombre(self):
        return self.__nombre

    def getCedula(self):
        return self.__cedula

    def getEdad(self):
        return self.__edad

    def esMayorDeEdad(self):
        if self.__edad >= 18:
            print('Usted es mayor de edad')
        else:
            print('Usted es menor de edad')

def mostrar():
    usuarios = []
    while True:
        u = Ciudadano()
        u.setNombre(input('Ingrese su nombre:\n'))
        u.setCedula(int(input('Ingrese su número de cédula:\n')))
        u.setEdad(int(input('Ingrese su edad:\n')))
        u.esMayorDeEdad()
        usuarios.append(u)

        print(f'Nombre: {u.getNombre()}\n'
              f'Cédula: {u.getCedula()}\n'
              f'Edad: {u.getEdad()}\n')

if __name__ == '__main__':
    mostrar()



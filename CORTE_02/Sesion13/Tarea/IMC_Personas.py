#IMC indice de masa corporal 
class Personas():
    def __init__(self):
        self.nombre =None
        self.altura = None
        self.peso = None

    def Indice (self):
        IMC = self.peso/((self.altura/100)**2)
        if IMC < 18.5:
            return str('Por debajo')
        elif IMC <=24.9:
            return str('Saludadble')
        elif IMC <= 29.9:
            return str('Sobrepeso')
        elif IMC <= 34.9:
            return str('Obesidad')
        elif IMC <= 40:
            return str('Obesidad II')
        else:
            return str('Obesidad III')  

def main():
    p = Personas()
    p.nombre='Pedro Caceres'
    p.peso=97
    p.altura=188
    print(f'su nombre es: {p.nombre}')
    print(f'su peso es: {p.peso}')
    print(f'su estatura es: {p.altura}')
    print(f'Su IMC es:{p.Indice()}\n')

    p = Personas()
    p.nombre='Maria Perez'
    p.peso=47
    p.altura=160
    print(f'su nombre es: {p.nombre}')
    print(f'su peso es: {p.peso}')
    print(f'su estatura es: {p.altura}')
    print(f'Su IMC es:{p.Indice()}\n')

    p = Personas()
    p.nombre='Julian Dominguez'
    p.peso=58
    p.altura=158
    print(f'su nombre es: {p.nombre}')
    print(f'su peso es: {p.peso}')
    print(f'su estatura es: {p.altura}')
    print(f'Su IMC es:{p.Indice()}\n')

    p = Personas()
    p.nombre='Jessica Fuentes'
    p.peso=73
    p.altura=170
    print(f'su nombre es: {p.nombre}')
    print(f'su peso es: {p.peso}')
    print(f'su estatura es: {p.altura}')
    print(f'Su IMC es:{p.Indice()}\n')

    

if __name__=='__main__':
    main()
class Personas:
    def __init__(self):
        self.nombre=None
        self.altura=None
        self.peso=None
#------------Setters-------------
    def setNombre(self,nombre:str):
        self.nombre=nombre
    def setAltura(self,altura:int):
        self.altura=altura
    def setPeso(self,peso:int):
        if peso>0:
            self.peso=peso
        else:
            self.peso=peso

#----------- Getters-------
    def getNombre(self):
        return self.nombre
    def getAltura(self):
        return self.altura
    def getPeso(self):
        if type(self.peso)==None:
            return 0
        return self.peso

#-----------metodo imc---------

    def imc(self):
        altura=self.getAltura
        peso=self.getPeso
        print(altura,peso)
        valor_imc=(self.peso)/(self.altura/100)**2
        if valor_imc<18.5:
            return f'IMC:{valor_imc:.2f} Por debajo.'
        elif valor_imc<24.9:
            return f'IMc:{valor_imc:.2f} Peso saludable'
        elif valor_imc<29.9:
            return f'IMc:{valor_imc:.2f} Peso Sobrepeso'
        elif valor_imc<34.9:
            return f'IMc:{valor_imc:.2f} Peso Obesidad I'
        elif valor_imc<39.9:
            return f'IMc:{valor_imc:.2f} Peso Obesidad II'
        return f'IMc:{valor_imc:.2f} Peso Obesidad III'
                
def main():
    pacientes=[]
    while 1:
        usuario=Personas()
        usuario.setNombre=input('Ingrese su nombre:')
        usuario.setAltura=int(input('Ingrese su altura en cm:'))
        usuario.setPeso=int(input('Ingrese su peso en kg:'))

        pacientes.append(usuario)

        print(f'Nombre:{usuario.setNombre}\n'
              f'altura:{usuario.setAltura}cm \n'
              f'peso:{usuario.setPeso}kg\n')
        print(usuario.imc())
          



if __name__=='__main__':
    main() 
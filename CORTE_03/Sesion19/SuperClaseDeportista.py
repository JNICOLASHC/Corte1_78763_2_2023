#herencias y jerarquias super clases 

class Deportistas():
    def __init__(self, nombre:str, documento:str, edad:int):
        self.__nombre=nombre
        self.__documento=documento
        self.__edad=edad

#-------setters-------
    def setNombre(self,nombre:str):
        self.__nombre=nombre
    def setDocumento(self,documento:str):
        self.__documento=documento
    def setEdad(self,edad:int):
        self.__edad=edad
#---------getters-------
    def getNombre(self):
        return self.__nombre
    def getDocumento(self):
        return self.__documento
    def getEdad(self):
        return self.__edad

class Futbolista(Deportistas):
    def __init__(self, nombre: str, documento: str, edad: int, goles:int, equipo:str):
        super().__init__(nombre, documento, edad)
        self.__goles=goles
        self.equipo=equipo

        #----setters------
    def setGoles(self,goles:int):
        self.__goles=goles
    def setEquipo(self,equipo:str):
        self.equipo=equipo

        #------getters-----
    def getGoles(self):
        return self.__goles
    def getEquipo(self):
        return self.equipo
    
    #-------Metodo-------
    def anotar(self):
        return f'el jugador {self.getNombre()} ha anotado {self.getGoles()} goles'
    
    
def main():
    inscrito=Futbolista('Nicolas','1234567',24,34,'seleccion colombia')
    print(f'Nombre:{inscrito.getNombre()}\n'\
          f'Documento:{inscrito.getDocumento()}\n'\
            f'Edad:{inscrito.getEdad()}\n'\
                f'#Goles:{inscrito.getGoles()}\n'\
                f'Equipo:{inscrito.getEquipo()}')
    print(inscrito.anotar())




if __name__=='__main__':
    main()
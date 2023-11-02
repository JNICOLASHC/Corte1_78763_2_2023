
class Ciudadano():
    def __init__(self, idioma:str, nombre:str):
        self.__idioma=idioma
        self.__nombre=nombre


#---------Setters---------------
    def setIdioma(self,idioma:str):
        self.__idioma=idioma
    def setNombre(self,nombre:str):
        self.__nombre=nombre

#----------getters-----------------
    def getIdioma(self):
        return self.__idioma
    def getNombre(self):
        return self.__nombre
    
   #---------sobreCarga---------
    def saludo(self):
        return f'Quoi de beau!'
    
class Colombiano(Ciudadano):
    def __init__(self, idioma: str, nombre: str, cc:str):
        super().__init__(idioma, nombre)
        self.__cc=cc

    def setCC(self,cc:str):
        self.__cc=cc

    def getCC(self):
        return self.__cc
    
    #--------Sobrecarga--------
    def saludo(self):
        return f'Que se dice Socio !!!! '
    
class Ingles(Ciudadano):
    def __init__(self, idioma: str, nombre: str , id:str):
        super().__init__(idioma, nombre)
        self.__id=id

    def setId(self,id:str):
        self.__id=id
    def getId(self,id:str):
        return self.__id
    #-----Sobrecarga-------
    def saludo(self):
        return f'Hello my friend!'
    
class Chino(Ciudadano):
    def __init__(self, idioma: str, nombre: str, sfz:str):
        super().__init__(idioma, nombre)
        self.__sfz=sfz

    def setSfz(self,sfz:str):
        self.__sfz=sfz
    def getSfz(self):
        return self.__sfz
    
    #------sobrecarga------
    def saludo(self):
        return f'chinfanchin'

def darSaludo(objeto):
    return object.saludo()

def main():
    ciudadano1=Ciudadano( 'Frances ','Carla Bruni')
    ciudadano2=Colombiano('Español','Nicolas herrera','123456789')
    ciudadano3=Ingles('Ingles','David Beckham','123456765432')
    ciudadano4=Chino('Mandarin','bruz li','1987654321')

    ciudadanos={ciudadano1,ciudadano2,ciudadano3,ciudadano4}
    
    print('-------Presentacion---------')
    for persona in ciudadanos:
        print(f'Ciudadano :{persona.getNombre()},idioma:{persona.getIdioma()}')
        print(f'{persona.getNombre()} dice:'+ darSaludo(persona)+'\n')

if __name__=='__main__':
    main()
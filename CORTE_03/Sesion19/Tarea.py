class Ciudadano:

    def _init_(self,nombre:str,documento:int,edad:int):
            self.__Nombre = nombre
            self.__documento = documento
            self.__edad = edad
        
#-----------------Geters------------------------------

    def getNombre(self):
        return self.__Nombre
        
    def getDocumento(self):
        return self.__documento
        
    def getEdad(self):
        return self.__edad
        
 #----------------Setters---------------------------------

    def setNombre(self,nombre:str):
        self.__Nombre = nombre

    def setDocumento(self,documento:int):
        self.__documento = documento

    def setEdad(self,edad:int):
        self.__edad = edad

    #--------sobre carga de metodo--------

    def futbol(self):
        return ("juega futbol en racing")

# Ciudadano #1 ( abogado ):


class __Abogado(Ciudadano):
    def __init__(self, nombre: str, documento: int, edad: int, casos: int, sueldo: int):
        super().__init__(nombre, documento, edad, casos, sueldo)

        self.__Casos = casos
        self.__Sueldo = sueldo

    # ---------------Getters--------------------
    def getCasos(self):
        return self.__Casos

    def getSueldo(self):
        return self.__Sueldo

    # ---------------Setters--------------------
    def setCasos(self, casos: int):
        self.__Casos = casos

    def setSueldo(self, sueldo: int):
        self.__Sueldo = sueldo

    def futbol(self):
        return ("juega futbol en boca")

# Ciudadano #2 ( Entrenador)

class __Entrenador(Ciudadano):
    def __init__(self, nombre: str, documento: int, edad: int,clientes:int,equipo:str):
        super().__init__(nombre, documento, edad)

        self.__Clientes = clientes
        self.__Equipo = equipo

#-------------------Getters------------------

    def getClientes(self):
        return self.__Clientes
    
    def getEquipo(self):
        return self.__Equipo
    
#-----------------Setters---------------------------

    def setClientes(self,clientes:int):
        self.__Clientes = clientes

    def setEquipo(self,equipo:str):
        self.__Equipo = equipo

#-------------------sobrecarga-------------

    def futbol(self):
        return ("juega futbol en santa fe ")

# ciudadano #3 ( Alcalde )

class __Alcalde(Ciudadano):
    def _init_(self, nombre: str, documento: int, edad: int,ciudadanos:str,municipio:str):
        super().__init__(nombre, documento, edad)

        self.__Ciudadanos = ciudadanos
        self.__Ciudad = municipio

#------------------Getters-------------------

    def getCiudadanos(self):
        return self.__Ciudadanos
    def getCiudad(self):
        return self.__Ciudad
    
#---------------Setters----------------------
        
    def setCiudadanos(self,ciudadanos):
        self.__Ciudadanos = ciudadanos
    def setMunicipio(self,municipio):
        self.__Ciudad = municipio

    def futbol(self):
        return ("juega futbol en mineiro")




def main():
   
   abogado = __Abogado("daniel", 15429, 37,26,1500000)

   print("")
   print("Abogado:") 
   print("")
   print(f"Nombre: {abogado.getNombre()}")
   print(f"ID: {abogado.getDocumento()}")
   print(f"Edad: {abogado.getEdad()}")
   print(f"Casos: {abogado.getCasos()}")
   print(f"Sueldo: {abogado.getSueldo()}")
   print("")

   entrenador = __Entrenador("Juan",25374,28,12,"huitaca")

   print("Entrenador")
   print("")
   print(f"Nombre: {entrenador.getNombre()}")
   print(f"ID: {entrenador.getDocumento()}")
   print(f"Edad: {entrenador.getEdad()}")
   print(f"Clientes: {entrenador.getClientes()}")
   print(f"Nombre del equipo: {entrenador.getEquipo()}")
   print()

   alcalde = __Alcalde("Claudia",15263,53,"7.181 millones","Bogota")

   print("Alcalde")
   print("")
   print(f"Nombre: {alcalde.getNombre()}")
   print(f"ID: {alcalde.getDocumento()}")
   print(f"Edad: {alcalde.getEdad()}")
   print(f"Ciudad: {alcalde.getCiudad()} ")
   print(f"Poblacion: {alcalde.getCiudadanos()}")
   print("")


if __name__ == '_main__':
    print(main())
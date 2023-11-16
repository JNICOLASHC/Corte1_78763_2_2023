import serial, time 

class Producto():
        def __init__(self,nombre:str,precio:float,cantidad_disponible:int):
            self.__nombre=nombre
            self.__precio=precio
            self.__cantidad_disponible=cantidad_disponible


        def setNombre(self,nombre:str):
            self.__nombre=nombre
        def setPrecio(self,precio:float):
            self.__precio=precio
        def setCantidad_disponible(self,cantidad_disponible:float):
            self.__cantidad_disponible=cantidad_disponible

        def getNombre(self):
            return self.__nombre
        def getPrecio(self):
            return self.__precio
        def getCantidad_disponible(self):
            return self.__cantidad_disponible
        
        def info_producto(self):
            return f"{self.__nombre},{self.__precio}"


        def restar_cantidad(self, cantidad: int ):
            if self.__cantidad_disponible >= cantidad:
                self.__cantidad_disponible -= cantidad
                return True
            else:
                return False

        def verificar_disponibilidad(self):
            return self.__cantidad_disponible > 0


class Snack(Producto):
    def __init__(self, nombre:str, precio:float, __cantidad_disponible: int, tipo:str):
        super().__init__(nombre, precio, __cantidad_disponible)
        self.tipo = tipo

        def setNombre(self,nombre):
            self.__nombre=nombre
        def setPrecio(self,precio):
            self.__precio=precio
        def setCantidad_disponible(self,cantidad_disponible):
            self.__cantidad_disponible=cantidad_disponible
        def setTipo(self,tipo):
            self.tipo=tipo

        def getNombre(self):
            return self.__nombre
        def getPrecio(self):
            return self.__precio
        def getCantidad_disponible(self):
            return self.__cantidad_disponible
        def getTipo(self):
            return self.tipo


class Bebida(Producto):
    def __init__(self, nombre:str, precio:float, cantidad_disponible:int, clase:str, tamaño:str):
        super().__init__(nombre, precio, cantidad_disponible)
        self.clase = clase
        self.tamaño = tamaño

        def setNombre(self,nombre):
            self.__nombre=nombre
        def setPrecio(self,precio):
            self.__precio=precio
        def setCantidad_disponible(self,cantidad_disponible):
            self.__cantidad_disponible=cantidad_disponible
        def setClase(self,clase):
            self.clase=clase
        def setTamaño(self,tamaño):
            self.tamaño=tamaño

        def getNombre(self):
            return self.__nombre
        def getPrecio(self):
            return self.__precio
        def getCantidad_disponible(self):
            return self.__cantidad_disponible
        def getTipo(self):
            return self.tipo
        def getClase(self):
            return self.clase
        def getTamaño(self):
            return self.tamaño


class Dispensadora(Producto):
    def __init__(self,):
        self.__producto = []
        self.__total_ventas = 0

    def agregar_producto(self, producto:str, cantidad_disponible:int, precio:float, tipo=None, tamaño=None):
        print(input('Ingrese el tipo de producto'))
        tipo=self.__producto

        if tipo == "Snack":
           precio= print(input('Ingrese el presio del producto '))
           cantidad_disponible=print(input('Ingrese la cantidad disponible de producto '))
           tipo=print(input('Ingrese el tipo de producto '))
           p = Snack.__producto['producto', 'precio', 'cantidad_disponible', 'tipo']

        elif tipo == "bebida":
            precio= print(input('Ingrese el presio del producto '))
            cantidad_disponible=print(input('Ingrese la cantidad disponible de producto '))
            tipo=print(input('Ingrese el tipo de producto '))
            tamaño=print(input('Ingrese el tamaño del producto'))
            p = Bebida.__producto['producto', 'precio', 'cantidad_disponible', 'tipo', 'tamaño']
        else:
            p = Producto[producto, precio, cantidad_disponible,tipo,tamaño]
            self.__producto[producto] = p

    def realizar_venta(self, producto, cantidad):
        if producto in self.producto and self.__producto[producto].verificar_disponibilidad():
            if self.producto[producto].restar_cantidad(cantidad):
                self.__total_ventas += self.producto[producto].precio * cantidad

            arduino = serial.Serial('COM8', 9600)  
            while True:
                arduino.write(b'H') 
                time.sleep(1)
                arduino.write(b'L') 
                time.sleep(1)
            else:
                return "Producto agotado"
        
        else:
                return "Producto no disponible"

    def obtener_total_venta(self):
        return f"Total de ventas:\n {self.__total_ventas}"

def agregar_producto(self, producto:str, cantidad_disponible:int, precio:float, tipo=None, tamaño=None):
        print(input('Ingrese el tipo de producto'))
        tipo=self.__producto

        if tipo == "snack":
           precio= print(input('Ingrese el presio del producto '))
           cantidad_disponible=print(input('Ingrese la cantidad disponible de producto '))
           tipo=print(input('Ingrese el tipo de producto '))
           p = Snack.__producto['producto', 'precio', 'cantidad_disponible', 'tipo']

        elif tipo == "bebida":
            precio= print(input('Ingrese el presio del producto '))
            cantidad_disponible=print(input('Ingrese la cantidad disponible de producto '))
            tipo=print(input('Ingrese el tipo de producto '))
            tamaño=print(input('Ingrese el tamaño del producto'))
            p = Bebida.__producto['producto', 'precio', 'cantidad_disponible', 'tipo', 'tamaño']
        else:
            p = Producto[producto, precio, cantidad_disponible,tipo,tamaño]
            self.__producto[producto] = p


if __name__=='__main__':
    Dispensadora()
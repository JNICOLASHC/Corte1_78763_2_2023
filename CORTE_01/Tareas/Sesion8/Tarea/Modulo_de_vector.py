 #módulo de un vector, junto con sus componentes rectangulares.

import math as M

def proc():
    cx1=float(input('Ingrese la coordenada de origen X del vector:\n'))
    cy1=float(input('Ingrese la coordenada de origen Y del vector:\n'))
    cx2=float(input('Ingrese la coordenada final X del vector:\n'))
    cy2=float(input('Ingrese la coordenada final Y del vector:\n'))
    Ax=cx2-cx1
    Ay=cy2-cy1
    modulo=M.sqrt((Ax)**2+(Ay)**2)
    print(f'Las componentes rectangulares de su vector son:\n En X son: {Ax}\n Y en Y son:{Ay}')
    print('El modulo de su vector es:\n',modulo)


if __name__=='__main__':
    proc()
    
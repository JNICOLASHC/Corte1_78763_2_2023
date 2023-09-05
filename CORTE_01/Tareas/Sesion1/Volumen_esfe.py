#hallar el volumen de agua en una esfera 

# r=float(input('ingrese el radio: '))
# v= ((4/3)*((3.1416)*(r**3)))
# c= v*1000
# print('El volumen en litros es:',round(c,3))
      

# ejemplo de solucion de funciones cuadraticas 

import math as m 

a=float(input('ingrese a:'))
b=float(input('ingrese b:'))
c=float(input('ingrese c:'))
x1=(-b+m.sqrt(b**2-4*a*c))/(2*a)
x2=(-b-m.sqrt(b**2-4*a*c))/(2*a)
print('Las soluciones',x1, 'y' ,x2)







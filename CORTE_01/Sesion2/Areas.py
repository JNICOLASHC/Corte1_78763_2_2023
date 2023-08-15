#Area de circulo, rectangulo,triangulo 

print('Seleccione una opcion:\n',\
      '1. calcula el area de un circulo \n',\
        '2. calcula el area de un rectangulo \n',\
            '3. calcula el area de un triangulo')
a='nan'
fig=input('Ingrese una figura para calcular su area:')
if (fig.lower()=='circulo'):
    r=int(input('ingrese el valor del radio'))
    a=3.1416*r**2
elif(fig.lower()=='rectangulo'):
    b=int(input('ingrese el valor de la base:'))
    h=int(input('ingrese el valor de la altura:'))
    a=b*h
elif(fig.lower()=='triangulo'):
    b=int(input('ingrese el valor de la base:'))
    h=int(input('ingrese el valor de la altura:'))
    a=b*h/2
else:
    print('ingreso una opcioninvalida')
print('el valor del area es',a)
#lower es para que me vuelva todo minuscula en los caracteres 
#upper es para que me vuelva todo mayuscula en los caracteres 

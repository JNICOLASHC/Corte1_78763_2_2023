#para saber si con las longitudes entradas se puede formar un triangulo o no 

co=float(input('Ingrese la primera longitud:\n'))
ca=float(input('ingrese la segunda longitud:\n'))
h=float(input('Ingrese la tercera longitud:\n'))
dl=co+ca
if dl >= h:
    if co == ca == h:
        print('Su triangulo es Equilatero')
    elif co == ca or co == h or ca == h:
        print('Su triangulo es Isosceles')
    elif co != ca and co != h and ca != h:
        print('Su triangulo es Escaleno')
else:
    print('Los valores ingresados no pueden formar un triangulo')


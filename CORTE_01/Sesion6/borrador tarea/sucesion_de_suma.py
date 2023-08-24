#producto entre dos numeros enteros (sumas sucesivas)

n1=int(input('Ingrese el primer numero:\n'))
n2=int(input('Ingrese el segundo numero:\n'))
p=0
for i in range(abs(n1)):
    p=p+n2
if n1<0:
    p=-p
print('el producto es:\n',p)


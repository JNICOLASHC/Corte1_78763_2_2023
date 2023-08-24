#se pide un numero y me muestra los numeros divisibles 

n=int(input('Ingrese un numero:\n'))
if n % 2==0:
    for i in range(1,n+1):
        if n % i ==0:
            print('los numeos divisores son:\n',i)
else:
    print('Todos los numeros son divicibles entre 0')

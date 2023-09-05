#menu de codigos 

def menu():
    print('Menu de inicio:\n')
    print('1.Numeros divicibles:')
    print('2.Sucesion de sumas:')
    print('3.Serie de Fibbonacci:')
    print('4.Salir del menu:\n')

while True:
    opc=int(input(menu()))

    if opc ==1:
        n=int(input('Ingrese un numero:\n'))
        if n % 2==0:
            for i in range(1,n+1):
                if n % i ==0:
                    print('los numeos divisores son:\n',i)
        else:
            print('Todos los numeros son divicibles entre 0')

    elif opc==2:
        n1=int(input('Ingrese el primer numero:\n'))
        n2=int(input('Ingrese el segundo numero:\n'))
        p=0
        for i in range(abs(n1)):
            p=p+n2
        if n1<0:
            p=-p
        print('el producto es:\n',p)

    elif opc==3:
        n=int(input('Ingrese un numero:\n'))
        a,b=0,1
        print(a,'\n',b)
        for i in range(n-2):
            c=a+b
            a = b
            b = c
            print(c)

    elif opc==4:
        print('usted a salido del menu:\n')
    


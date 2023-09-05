n=int(input('Ingrese un numero:\n'))
c=int(input('ingrese la cantidad de numeros perfectos que quiere ver (max:10):\n'))

def proc():
    con=0
    while con <=c :
        for i in range(1,n+1):
            sm=1
            for s in range(1,i):
                if i % s ==0:
                        sm += s
            if sm ==i:
                print(f'los numeos perfectos de su numero son:\n ,{sm}')
                con +=1
    if c>10:
        print('Su numero tiene mas de 10 numeros perfectos ')
    return 0


if __name__=='__main__':
    proc()


def main_read():
    f=open('matrizAsignacion.txt','rt')
    documento=f.read()
    f.close()
    print(documento)

def main_read2():
    f=open('matrizAsignacion.txt','rt')
    documento=f.readline().rstrip('\n').split(',')
    while documento !=[""]:
        print(documento)
        documento=f.readline().rstrip('\n').split(',')
    f.close()
def suma(lista):
    for dato in lista:
        resultado=int(dato[0])+int(dato[1])+int(dato[3])
        print(resultado)

def main_read3():
    f=open('matrizAsignacion.txt','rt')
    documento=f.readlines()
    f.close()
    lista=[]
    for dato in documento:
        lista.append(dato.rstrip('\n').split(','))
    print(lista)
    suma(lista)

if __name__=='__main__':
    # main_read()
    # main_read2()
    main_read3()
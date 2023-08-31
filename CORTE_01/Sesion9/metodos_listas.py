
def agregar(ml):
    num=int(input('Que numero desea agregar:'))
    ml.append(num)
    print(ml)
def insertar(ml):
    var=int(input('Que numero desea agregar:'))
    idx=int(input('En que posicion:'))
    ml.insert(idx,var)
    print(ml )
def borrar(ml):
    ml.clear()
    print(ml)
def remover(ml):
    print(ml)
    var=int(input('Que numero quiere remover:'))
    ml.remove(var)
    print(ml)

def menu():
    ml=[2,4,7,8]
    opc=''
    while opc!='exit':
        print('seleccione una de las siguientes opciones:\n',\
            '1.Agregar \n 2.Insertar \n 3.borrar')
        
        opc=input('=>')

        if opc=='1':
            agregar(ml)
        elif opc=='2':
            insertar(ml)
        elif opc=='3':
            borrar(ml)
        elif opc=='4':
            remover(ml)








if __name__=='__main__':
    menu()
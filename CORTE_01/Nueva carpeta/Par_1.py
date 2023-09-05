#juego de BlackJack
import random as r 

def main():
        A=11
        j=10
        Q=10
        k=10
        y='si'
        n='no'
        cart=''
        cart=['A',2,3,4,5,6,7,8,9,'j','Q','k']
        while cart<cart:
            var=r.choice(cart)
            print(var)

        def repartir():
            v=''
            v.index(cart,A,j,Q,k)
            print(var)

        def suma(v):
            var.sum(v)
            print('Usted tiene una varaja de:\n',v)
        
        def insertar(v):
            var.appent(var)
            print(var)
            var.sum(v)

            while opc !='exit':
                opc=''
                print('Seleccione una de las siguientes opciones:\n',\
                    '1.y si quiere una carta \n 2.n si no quiere mas cartas \n o exit si quiere salir')
                if opc =='y':
                    y(var)
                elif opc == 'n':
                    print(var)


if __name__=="__main__":
        main()
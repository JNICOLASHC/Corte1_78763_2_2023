#blackjack
from random import choice as c

def repartir():
    deck = 'A23456789jQk'
    return c(deck)

def valor(card):
    jack = ['j', 'Q', 'k']
    if card in jack:
        card = 10
    elif card == 'A':
        card = 11
    else:
        card = int(card)
    return card

def conteo(mano):
    cartas = []
    for i in range(len(mano)):
        cartas.append(valor(mano[i]))
    print(cartas)
    suma = sum(cartas)
    print(f'conteo: {suma}')
    return suma

def main(): 
    mano = []
    mano.append(repartir())
    mano.append(repartir())
    print(mano)
    suma = conteo(mano)

    opc = 'y'
    while opc == 'y':
        opc = input('Quiere otra carta? (y/n)\n')
        if opc == 'y':
            mano.append(repartir())
            print(mano)
            suma = conteo(mano)
            if suma > 21:
                print("---- busted ----")
                break
        elif opc == 'n':
            print("fin de la apuesta")
            break
        else:
            print('Opcion invalida')
            opc = 'y'

if __name__ == "__main__":
    main()
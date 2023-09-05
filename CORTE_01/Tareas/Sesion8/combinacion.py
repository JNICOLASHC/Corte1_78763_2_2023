from factorial import factorial as f

def combinacion():
    n=int(input('ingrese el numero de elementos:\n'))
    m=int(input('ingrese el numero de grupos:\n'))
    cmb=(f(n)/(f(m)*f(n-m)))
    print(f'el numero de combianciones posibles es: {cmb}')


if __name__=="__main__":
    combinacion()

import funcion_externa

def main():
    a=int(input('Ingrese un numero:\n'))
    b=int(input('Ingrese otro numero:\n'))
    r=funcion_externa.suma(a,b)
    print(r)
    print(f'ejecutado desde{__name__}')


if __name__=="__main__":
    main()
import random as r

def app():
    pal=''
    nombre='Nicolas'
    while pal != 'exit':
        #X=r.randint(100,180)
        #x=r.uniform(100,180)
        x=r.choice(nombre)
        print(x)
        pal=input('para salir escriba exit:\n')



if __name__=="__main__":
    app()

#randint=numeros enteros 
#uniform=numeros decimales 
#choice = solo letras o espacios dentro de un mensaje o variable aleatoriamnete las va escogiendo 
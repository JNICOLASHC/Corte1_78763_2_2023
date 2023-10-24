#codigo de resistencias 

def resistencia():
    co1=str(input('Ingrese el primer color:\n'))
    co2=str(input('Ingrese el segundo color:\n'))
    co3=str(input('Ingrese el tercer color:\n'))
    banda1=co1
    banda2=co2
    banda3=co3
    colores=[banda1,banda2,banda3]
    if banda1=='negro' or banda2=='negro'or banda3=='negro':
        c1= banda1.colores[0]=0
        c2=banda2.colores[1]=0
        c3=banda3.colores[2]=1
        r=c1+c2*c3
    elif banda1=='cafe'or banda2=='cafe'or banda3=='cafe':
        c1=banda1.colores[0]=1
        c2=banda2.colores[1]=1
        c3=banda3.colores[2]=10
        r=c1+c2*c3
    elif banda1=='rojo'or banda2=='rojo'or banda3=='rojo':
        c1=banda1.colores[0]=2
        c2=banda2.colores[1]=2
        c3=banda3.colores[2]=100
        r=c1+c2*c3
    elif banda1=='naranja'or banda2=='naranja'or banda3=='naranja':
        c1=banda1.colores[0]=3
        c2=banda2.colores[1]=3
        c3=banda3.colores[2]=1000
        r=c1+c2*c3
    elif banda1=='amarillo'or banda2=='amarillo'or banda3=='amarillo':
        c1=banda1.colores[0]=4
        c2=banda2.colores[1]=4
        c3=banda3.colores[2]=10000
        r=c1+c2*c3
    elif banda1=='verde'or banda2=='verde'or banda3=='verde':
        c1=banda1.colores[0]=5
        c2=banda1.colores[1]=5
        c3=banda3.colores[2]=100000
        r=c1+c2*c3
    elif banda1=='azul'or banda2=='azul'or banda3=='azul':
        c1=banda1.colores[0]=6
        c2=banda2.colores[1]=6
        c3=banda3.colores[2]=1000000
        r=c1+c2*c3
    elif banda1=='morado'or banda2=='morado'or banda3=='morado':
        c1=banda1.colores[0]=7
        c2=banda2.colores[1]=7
        c3=banda3.colores[2]=10000000
        r=c1+c2*c3
    elif banda1=='gris'or banda2=='gris'or banda3=='gris':
        c1=banda1.colores[0]=8
        c2=banda2.colores[1]=8
        c3=banda3.colores[2]=100000000
        r=c1+c2*c3
    elif banda1=='blanco'or banda2=='blanco'or banda3=='blanco':
        c1=banda1.colores[0]=9
        c2=banda2.colores[1]=9
        c3=banda3.colores[2]=1000000000
        r=c1+c2*c3
    
    print('El valor de la resistencia es:\n',r)
        

if __name__=='__main__':
    resistencia()

    # ban1=['negro',0,'cafe',1,'rojo',2,'naranja',3,'amarillo',4,'verde',5,'azul',6,'morado',7,'gris',8,'blanco',9]
    # ban2=['negro',0,'cafe',1,'rojo',2,'naranja',3,'amarillo',4,'verde',5,'azul',6,'morado',7,'gris',8,'blanco',9]
    # ban3=['negro',1,'cafe',10,'rojo',100,'naranja',1000,'amarillo',10000,'verde',100000,'azul',1000000,'morado',10000000,'gris',100000000,'blanco',1000000000]
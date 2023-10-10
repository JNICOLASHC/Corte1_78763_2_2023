#taller 2 

def lectura():
    documento = []
    f = open('wcm.csv', 'r', encoding="utf8")
    documento=f.readlines()
    f.close()
    lista=[]
    for dato in documento:
        lista.append(dato.rstrip('\n').split(','))
    print(lista)


def enfrentamiento(lectura):
    ep1=str(input('Digite el primer equipo:\n'))
    ep2=str(input('Digite el segundo equipo:\n'))
    cp=int(input('Digite la cantidad de partidos:\n'))
    f=(lectura)

    while documento != [""]:
        ep1 = documento[0]
        ep2 = documento[1]
        cp= documento[2]
        documento = f.readline().rstrip('\n').split(',')

        if ep1 not in documento:
            documento[ep1] = {}
        if ep2 not in documento[ep1]:
            documento[ep1][ep2] = {"victorias": 0, "empates": 0, "derrotas": 0}

        if cp == "victoria":
            documento[ep1][ep2]["victorias"] += 1
        elif cp == "empate":
            documento[ep1][ep2]["empates"] += 1
        else:
            documento[ep1][ep2]["derrotas"] += 1
    f.close()
    if ep1 in documento and ep2 in documento[ep1]:
        enfrentamientos = documento[ep1][ep2]
        print(f"Enfrentamientos entre {ep1} y {ep2}:")
        print(f"Victorias: {enfrentamientos['victorias']}")
        print(f"Empates: {enfrentamientos['empates']}")
        print(f"Derrotas: {enfrentamientos['derrotas']}")
    else:
        print("No se encontraron enfrentamientos entre los equipos especificados.")

def goleada(lectura):
         while True:
            print("a. Ver lista completa de las mayores goleadas en mundiales")
            print("b. Búsqueda por fecha de mundial")
            opcion = input("Seleccione una opción:\n")
            if opcion == "a":
                goleadas = goleada()
                for goleada in goleadas:
                    print(f"{goleada[0]} vs {goleada[1]} - Dg: {goleada[2]}")
            elif opcion == "b":
                fecha = input("Ingrese el año del mundial:\n")
                goleadas = goleada()
                encontradas = []
                for goleada in goleadas:
                    if fecha in goleada[0] or fecha in goleada[1]:
                        encontradas.append(goleada)
                if len(encontradas) > 0:
                    for goleada in encontradas:
                        print(f"{goleada[0]} vs {goleada[1]} - Dg: {goleada[2]}")
                else:
                    print("No se encontraron goleadas para la fecha ingresada")

                lista = lectura()
            goleadas = []
            for partido in lista:
                glocal = int(partido[2])
                gvisitante = int(partido[3])
                if glocal > gvisitante:
                    dgoles = glocal - gvisitante
                    goleadas.append((partido[0], partido[1], dgoles))
                elif gvisitante > glocal:
                    dgoles = gvisitante - glocal
                    goleadas.append((partido[1], partido[0], dgoles))
            goleadas.sort(key=lambda x: x[2], reverse=True)
            return goleadas

def salir():
    return 0 

def main(lectura):
    while True:
        print('Que estadistica quiere saber:\n')
        print('Escriba "enfrentamiento": si quiere conocer cuantas veces se han enfrentado 2 equipos en los mundiales:\n')
        print('Escriba "goleada": si quiere conocer cuáles fueron las mayores goleadas de los mundiales:\n ')
        print('Escriba Salir si quiere terminar el programa:\n')
        opc=input('Ingrese su opcion:\n')
        
        if opc=='enfrentamiento':
            enfrentamiento(lectura)
        elif opc=='goleada':
            goleada(lectura)
        elif opc=='salir':
            salir()

if __name__=="__main__":
    main(lectura)

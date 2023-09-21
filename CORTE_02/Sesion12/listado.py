#diccionarios 

def inscripcion():
    estudiantes={}
    datos={}
    while 1:
        opc=input('desea inscribir un estudiante (y/n):')

        if opc=='y':
            nombre=input('Nombre:\n')
            edad=input('Edad:\n')
            codigo=input('Codigo:\n')
            genero=input('Genero:\n')
            datos['edad']=edad
            datos['codigo']=codigo
            datos['genero']=codigo
            estudiantes[nombre]=datos
            print(estudiantes)
        elif opc=='n':
            for key, value in estudiantes.items():
                print(f'Estudiantes:{key}')
                print(estudiantes[key]['edad'])
            break
        else:
            print('opcion invalida')

def main():
    inscripcion()

if __name__=='__main__':
    main()
def calendario(mes):
    dim = {
        'enero': 31,
        'febrero': 28,
        'marzo': 31,
        'abril': 30,
        'mayo': 31,
        'junio': 30,
        'julio': 31,
        'agosto': 31,
        'septiembre': 30,
        'octubre': 31,
        'noviembre': 30,
        'diciembre': 31
    }
    fest = {
        'enero': 'Año Nuevo',
        'febrero': 'Día de San Valentín',
        'marzo': 'Día de San José',
        'abril': 'Semana Santa',
        'mayo': 'Día del Trabajo',
        'junio': 'Día del Padre',
        'julio': 'Día de la Independencia',
        'agosto': 'A volar cometas',
        'septiembre': 'Día de la Independencia',
        'octubre': 'Día de las Brujas',
        'noviembre': 'Día de los Muertos',
        'diciembre': 'Navidad'
    }
    d = dim.get(mes.lower(), None)
    if d is None:
        print('El mes ingresado no es existe.')
    else:
        print('El mes de:\n', mes, 'tiene:\n', d, 'días y el siguientes festivos:\n', fest[mes.lower()])

if __name__ == '__main__':
    mes = input('Ingrese el nombre de un mes del año:\n ')
    calendario(mes)
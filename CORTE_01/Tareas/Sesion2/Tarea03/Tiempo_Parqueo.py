#cobro de tiempo de parqueo 

import math

m=float(input('ingrese el tiempo de parqueo en minutos:\n'))
Pm=139
Ptt=m*Pm
Pr=math.ceil(Ptt / 50 )*50
print('El valor a pagar de parqueadero es:\n $',Pr, ('Pesitos'))



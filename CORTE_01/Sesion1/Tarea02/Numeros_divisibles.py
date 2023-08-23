#Numeros divisibles 

n=int(input('ingrese un numero:\n'))
print('los numeros divisibles por',n,'son:\n')
for i in range(1,n+1):
    if n % i==0:
        print(i)
        

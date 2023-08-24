#se realiza una serie de fibbonacci

n=int(input('Ingrese un numero:\n'))
a,b=0,1
print(a,'\n',b)
for i in range(n-2):
    c=a+b
    a = b
    b = c
    print(c)


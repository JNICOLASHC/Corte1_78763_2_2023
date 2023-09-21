


def impar(n):
#     if n==0:
#         return 1
#     else:
#         num=(2*n+1)+impar(n-1)
#         return num 
    #una manera para hacerlo lo mismo 
    if n>0:
        num=(2*n+1)+impar(n-1)
        return num
    else:
        return 1
    #otra manera de hacerlo lo mismo 

def main():
    num=int(input('Ingrese un  numero:'))
    resultado=impar(num)
    print(f'El resultado es:\n {resultado}')


if __name__=='__main__':
    main()
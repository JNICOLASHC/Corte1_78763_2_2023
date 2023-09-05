#15 numeros aleatorios 
import random as r

def aleatorios(n):
    num = []
    i = 0
    while i < n:
        num.append(r.randint(1, 100))
        i += 1
    print("Sus 15 numeros son:\n", num)
    num.sort()
    print('Sus numeros organizados son:\n',num)
    return num

if __name__ == '__main__':
    aleatorios(15)
  
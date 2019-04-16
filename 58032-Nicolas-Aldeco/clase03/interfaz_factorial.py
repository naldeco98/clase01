from factorial import factorial
import os

def main():   
    os.system('clear')
    print('Ingrese un valor para calcular su factorial')
    res = menu(input('>>'))
    print(res)


def menu(number):
    if number.isdigit() == False:
        if number[0] == '-' :
            return ('Error-No puede ingresar un numero negativo')
        else:  
            return ('Error-No es un numero')
    else:
        return factorial(int(number))

main()
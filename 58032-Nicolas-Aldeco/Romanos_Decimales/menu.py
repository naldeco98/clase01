from decimal_roman import decimal_to_roman
from ronam_numbers import roman_to_decimal
import os

#Menu selector
def menu():

    os.system('clear')
    print ('|CONVERTIDOR DE NUMEROS ROMANOS A DECIMAL O ALREVES|')
    print ('\t 1 - Decimal >> Romano')
    print ('\t 2 - Romano >> Decimal')
    print ('\t 3 - Salir')
    
while True:

    menu()


    op_menu = input('\nIngrese un valor >> ')
    
    if op_menu == '1':

        os.system('clear')
        print('Ingrese un numero entre 1 y 3999')
        decimal_number = int(input('\n\n>> '))

        result = ''

        result = decimal_to_roman(decimal_number)
            
        os.system('clear')
        print(f'El numero {decimal_number} es {result} en romano')
        input('Presione una tecla para volver...')
        menu()
    
    if op_menu == '2':

        os.system('clear')
        print('Ingrese un numero entre I y MMMCMXCIX')
        roman_number = input('\n\n>> ').upper()

        result = roman_to_decimal(roman_number)

        os.system('clear')
        if result != 0 :
            print(f'El numero {roman_number} es {result} en decimal')
            input('Presione una tecla para volver...')
            menu()
        else:
            print('El valor ingresado es invalido')
            input('Presione una tecla para volver...')
            menu()
    
    if op_menu == '3':
        os.system('clear')
        print('Adios!')
        break
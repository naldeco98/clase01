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


    op_menu = input('\nIngrese un valor >>')
    
    if op_menu == '1':

        os.system('clear')
        print('Ingrese un numero entre 1 y 3999')
        decimal_number = int(input('\n\n>> '))
        result = ''
        ct = bool
        while ct == False:
            result = ''
            if decimal_number < 1 and decimal_number > 4000:
                print ('El numero esta fuera del rango')
                ct = False
            else:
                result = decimal_to_roman(decimal_number)
                ct = True
            
        os.system('clear')
        print(f'El numero {decimal_number} es {result} en romano')
    
    break

            
        

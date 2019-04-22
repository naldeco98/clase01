from cifrado_vigenere import encode,decode
import sys
import os

class SpaceInString(Exception):
    pass
class KeyLargerThanString(Exception):
    pass
class NumberInTheString(Exception):
    pass
class EmptyData(Exception):
    pass
 
def main():
    os.system('clear')
    print('\tCODIGO VIGENERE ENCRIPTADOR Y DECRIPTADOR')
    print('\nRecuerda que los mensajes no pueden tener espacios o numeros\n')
    print('1 - ENCODE')
    print('2 - DECODE')
    print('3 - Salir')

    ch = int(input('\n>>> '))
    
    if ch == 1 :
        os.system('clear')
        word = input('Mensaje > ')
        key = input('Palabra Clave > ')
        os.system('clear')
        codex = coder(key.upper(), word.upper(),ch)
        print('Mensaje Enciptado:', codex,'\nPalabra Clave:',key.upper())
        input('Presione una tecla para volver al menu...')
        main()
    if ch == 2 :
        os.system('clear')
        word = input('Codigo > ')
        key = input('Palabra Clave > ')
        os.system('clear')
        codex = coder(key.upper(), word.upper(),ch)
        print('Mensaje Desinciptado:', codex,'\nPalabra Clave:',key.upper())
        input('Presione una tecla para volver al menu...')
        main()
    if ch == 3:
        os.system('clear')
        print('Chau! \n-Nico Aldeco')
        sys.exit()

def coder(key,text,chose):
    if not text or not key:
        raise EmptyData('ERROR - Campos vacios')
    space = int(text.find(' '))
    if space != -1:
        raise SpaceInString('ERROR - No puede haber espacios.')
    if text.isalpha() == False:
        raise NumberInTheString('ERROR - No puede contener numeros el mensaje')
    if len(text) < len(key) :
        raise KeyLargerThanString('ERROR - La clave no puede ser mas grande que el mensaje.')
    else:
        if chose == 1:
            return encode(key,text)
        if chose == 2:
            return decode(text,key)


main()
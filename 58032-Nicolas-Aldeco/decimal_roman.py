def decimal_to_roman(decimal_number):

    r_dec = ''
    r_uni = ''
    r_udm = ''
    r_cent = ''
    roman_number = ''
    decimal_string = str(decimal_number) [::-1]
    nd = len(decimal_string)

    #Unidad#
    if decimal_string[0] == '1':
        r_uni = 'I'
    if decimal_string[0] == '2':
        r_uni = 'II'
    if decimal_string[0] == '3':
        r_uni = 'III'
    if decimal_string[0] == '4':
        r_uni = 'IV'
    if decimal_string[0] == '5':
        r_uni = 'V'
    if decimal_string[0] == '6':
        r_uni = 'VI'
    if decimal_string[0] == '7':
        r_uni = 'VII'
    if decimal_string[0] == '8':
        r_uni = 'VIII'
    if decimal_string[0] == '9':
        r_uni = 'IX'
    #Decenas#
    if nd >= 2:
        if decimal_string [1] == '0':
            r_dec = ''
        if decimal_string[1] == '1' :
            r_dec = 'X'
        if decimal_string[1] == '2' :
            r_dec = 'XX'
        if decimal_string[1] == '3' :
            r_dec = 'XXX'
        if decimal_string[1] == '4' :
            r_dec = 'XL'
        if decimal_string[1] == '5' :
            r_dec = 'L'
        if decimal_string[1] == '6' :
            r_dec = 'LX'
        if decimal_string[1] == '7' :
            r_dec = 'LXX'
        if decimal_string[1] == '8' :
            r_dec = 'LXXX'
        if decimal_string[1] == '9' :
            r_dec = 'XC'
    #Centenas#
    if nd >= 3:
        if decimal_string[2] == '0':
            r_cent = ''
        if decimal_string[2] == '1': 
            r_cent = 'C'
        if decimal_string[2] == '2':
            r_cent = 'CC'
        if decimal_string[2] == '3':
            r_cent = 'CCC'
        if decimal_string[2] == '4':
            r_cent = 'CD'
        if decimal_string[2] == '5':
            r_cent = 'D'
        if decimal_string[2] == '6':
            r_cent = 'DC'
        if decimal_string[2] == '7':
            r_cent = 'DCC'
        if decimal_string[2] == '8':
            r_cent = 'DCCC'
        if decimal_string[2] == '9':
            r_cent = 'CM'
    #Unidades de mil#
    if nd >= 4:
        if decimal_string[3] == '0':
            r_udm = ''
        if decimal_string[3] == '1':
            r_udm = 'M'
        if decimal_string[3] == '2':
            r_udm = 'MM'
        if decimal_string[3] == '3':
            r_udm = 'MMM'
     
    roman_number = r_udm + r_cent + r_dec + r_uni
      
    return (roman_number)

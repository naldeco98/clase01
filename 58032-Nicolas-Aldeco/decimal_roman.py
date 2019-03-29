def decimal_to_roman(decimal_number):
    r_dec = ''
    r_uni = ''
    r_udm = ''
    r_cent = ''
    roman_number = ''
    num_uni = int(decimal_number/10)           
    number_r_dec = int(round(decimal_number/10,1))      #Operacion para saber la decena
    number_r_uni = round((decimal_number/5)-(num_uni*2),2)   #Operacion para saber la unidad
    #Unidad#
    if number_r_uni == 0.2:
        r_uni = 'I'
    if number_r_uni == 0.4:
        r_uni = 'II'
    if number_r_uni == 0.6:
        r_uni = 'III'
    if number_r_uni == 0.8:
        r_uni = 'IV'
    if number_r_uni == 1.0:
        r_uni = 'V'
    if number_r_uni == 1.2:
        r_uni = 'VI'
    if number_r_uni == 1.4:
        r_uni = 'VII'
    if number_r_uni == 1.6:
        r_uni = 'VIII'
    if number_r_uni == 1.8:
        r_uni = 'IX'
    #Decenas#
    if number_r_dec == 1 :
        r_dec = 'X'
    if number_r_dec == 2 :
        r_dec = 'XX'
    if number_r_dec == 3 :
        r_dec = 'XXX'
    if number_r_dec == 4 :
        r_dec = 'LX'
    if number_r_dec == 5 :
        r_dec = 'L'
    if number_r_dec == 6 :
        r_dec = 'LX'
    if number_r_dec == 7 :
        r_dec = 'LXX'
    if number_r_dec == 8 :
        r_dec = 'LXXX'
    if number_r_dec == 9 :
        r_dec = 'XC'
    #Centenas#
    if number_r_cent == 1: 
    roman_number = r_udm + r_cent + r_dec + r_uni  
    return (roman_number)

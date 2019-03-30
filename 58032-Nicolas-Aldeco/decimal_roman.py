def decimal_to_roman(decimal_number):

    r_dec = ''
    r_uni = ''
    r_udm = ''
    r_cent = ''
    roman_number = ''
    number_r_udm = decimal_number/1000
    float(number_r_udm)
    if number_r_udm == 0.999:
        number_r_udm = 0
    else:
        number_r_udm = int(round(number_r_udm,2))

    number_r_cent = decimal_number/100    #Operacion para saber la centena 
    float(number_r_cent)
    if number_r_cent == 0.99 :
        number_r_cent = 0
    else:
        number_r_cent = int(round(number_r_cent,2)) 
    
    aux_dec = int(round(decimal_number/10,1)) * 0.1 - number_r_cent
    number_r_dec = int(round(aux_dec,1)*10)    #Operacion para saber la decena      
    num_uni = int(decimal_number/10)           #Auxiliar op de unidad
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
        r_cent = 'C'
    if number_r_cent == 2:
        r_cent = 'CC'
    if number_r_cent == 3:
        r_cent = 'CCC'
    if number_r_cent == 4:
        r_cent = 'CD'
    if number_r_cent == 5:
        r_cent = 'D'
    if number_r_cent == 6:
        r_cent = 'DC'
    if number_r_cent == 7:
        r_cent = 'DCC'
    if number_r_cent == 8:
        r_cent = 'DCCC'
    if number_r_cent == 9:
        r_cent = 'CM'
    #Unidades de mil#
    if number_r_udm == 1:
        r_udm = 'M'
    if number_r_udm == 2:
        r_udm = 'MM'
    if number_r_udm == 3:
        r_udm = 'MMM'
     
    roman_number = r_udm + r_cent + r_dec + r_uni
      
    return (roman_number)

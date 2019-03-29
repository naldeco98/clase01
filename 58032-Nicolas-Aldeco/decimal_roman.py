def decimal_to_roman(decimal_number):
    r_dec = ''
    r_uni = ''
    roman_number = ''

    num_uni = int(decimal_number/10)                
    number_r_uni = ((decimal_number/5)-(num_uni*2))*10   #primera letra de numero romano
    if num_uni >= 0:
        if number_r_uni == 2:
            r_uni = 'I'
        if number_r_uni == 4:
            r_uni = 'II'
        if number_r_uni == 6:
            r_uni = 'III'
        if number_r_uni == 8:
            r_uni = 'IV'
        if number_r_uni == 10:
            r_uni = 'V'
        if number_r_uni == 12:
            r_uni = 'VI'
        if number_r_uni == 14:
            r_uni = 'VII'
        if number_r_uni == 16:
            r_uni = 'VIII'
        if number_r_uni == 18:
            r_uni = 'IX'

    if num_uni < 10 :
        if num_uni == 1:
            r_dec = 'X'
        if num_uni == 2:
            r_dec = 'XX'
        if num_uni == 3:
            r_dec = 'XXX'
        if num_uni == 4:
            r_dec = 'XL'
        if num_uni == 5:
            r_dec = 'L'
        if num_uni == 6:
            r_dec = 'LX'
        if num_uni == 7:
            r_dec = 'LXX'
        if num_uni == 8:
            r_dec = 'LXXX'
        if num_uni == 9:
            r_dec = 'XC'
        if num_uni == 10:
            r_dec = 'C'
    roman_number = r_dec
    roman_number += r_uni
    return (roman_number)

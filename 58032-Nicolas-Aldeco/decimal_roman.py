def decimal_to_roman(decimal_number):
    r_dec = ''
    r_uni = ''
    roman_number = ''
    letra = str(decimal_number)
    num_uni = int(decimal_number/10)           
    number_r_dec = int(round(decimal_number/10,1))
    number_r_uni = (decimal_number/5)-(num_uni*2)   #primera letra de numero romano
    for letter in (letra):
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
        if decimal_number > 10 :
            if number_r_dec == 1 :
                r_dec = 'X'
            if number_r_dec == 2 :
                r_dec = 'XX'
            if number_r_dec == 3 :
                r_dec = 'XXX'
        
    roman_number = r_dec + r_uni
    print(roman_number)
    return (roman_number)

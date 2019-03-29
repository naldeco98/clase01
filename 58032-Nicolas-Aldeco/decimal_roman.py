def decimal_to_roman(decimal_number):

    aux_dec = int(decimal_number/10)
    number_x = (decimal_number/5)-(aux_dec*2)

    if number_x == 0.2:
        roman_number = 'I'
    if number_x == 0.4:
        roman_number = 'II'

    return (roman_number)

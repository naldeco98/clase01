def decimal_to_roman(decimal_number):
    roman_number = ''
    decimal_string = str(decimal_number)
    number_dic = {}
    number_dic [1] = ['I','X','C','M']
    number_dic [2] = ['II','XX','CC','MM']
    number_dic [3] = ['III','XXX','CCC','MMM']
    number_dic [4] = ['IV','XL','CD']
    number_dic [5] = ['V','L','D']
    number_dic [6] = ['VI','LX','DC']
    number_dic [7] = ['VII','LXX','DCC']
    number_dic [8] = ['VIII','LXXX','DCCC']
    number_dic [9] = ['IX','XC','CM']

    umil = decimal_number / 1000
    tmp = decimal_number % 1000
    umil = int(umil)
    centenas = tmp / 100
    tmp = tmp % 100
    centenas = int(centenas)
    decenas = tmp / 10
    decenas = int(decenas)
    unidades = tmp % 10
    if umil > 3:
        roman_number = 'NumberOutOfLimit'
    else:
        if umil != 0:
            roman_number += number_dic[umil][3]
        if centenas != 0:
            roman_number += number_dic[centenas][2]
        if decenas != 0:
            roman_number += number_dic[decenas][1]
        if unidades != 0:
            roman_number += number_dic[unidades][0]
    return (roman_number)
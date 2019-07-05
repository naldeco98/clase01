def roman_to_decimal(roman_number):
   decimal_number = 0
   ant = ''
   dic_roman = {'': 0, 'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
   for letter in roman_number:
      decimal_number += dic_roman[letter]
      if letter != ant and dic_roman[ant] < dic_roman[letter]:
         if ant == 'I':
            decimal_number -= 2
         if ant == 'X':
            decimal_number -= 20
         if ant == 'C':
            decimal_number -= 200
         if ant == 'D':
            decimal_number -= 1000
      ant = letter
   return(decimal_number)
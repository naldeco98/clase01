def cifrado(key,word):
    abcd = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for i in range(len(word)):
        x = abcd.find(word[i])
        y = abcd.find(key[i])
        suma = x+y
        mod = suma%len(abcd)
        code += abcd[mod]
    return code
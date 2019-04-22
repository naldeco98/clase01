def encode(key,word):
    abcd = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    if len(word) > len(key):
        new_key = ''
        for i in range(int(len(word)/len(key))):
           	new_key += key								
        new_key += key[:len(word)%len(key)] 
        key = new_key
    for i in range(len(word)):
        x = abcd.find(word[i])
        y = abcd.find(key[i])
        suma = x+y
        mod = suma%len(abcd)
        code += abcd[mod]
    return code

def decode(code,key):
    abcd = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    word = ''
    if len(code) > len(key):
        new_key = ''
        for i in range(int(len(code)/len(key))):
           	new_key += key								
        new_key += key[:len(code)%len(key)] 
        key = new_key
    for n in range(len(code)):
        x = abcd.find(code[n])
        y = abcd.find(key[n])
        resta = x-y
        mod = resta%len(abcd)
        word += abcd[mod]
    return word
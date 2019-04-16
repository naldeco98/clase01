def count_letters(frase):
    dic_mio = {}
    let = ''
    for let in range(frase):
        if let in frase == dic_mio[let]:
            dic_mio[let] =+ 1
    return dic_mio

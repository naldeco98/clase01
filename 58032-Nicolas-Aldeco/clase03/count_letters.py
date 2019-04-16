def count_letters(frase):
    dic_mio = {}
    for let in frase:
        if let in dic_mio:
            dic_mio[let] += 1
        else:
                dic_mio[let] = 1
    return dic_mio

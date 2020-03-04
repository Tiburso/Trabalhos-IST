def codifica(word):
    pares = '' 
    impares = ''
    for i in range(len(word)):
        if i % 2 == 0:
            pares += word[i]
        else:
            impares += word[i]
    return pares + impares

def descodifica(word):
    word_f = '' 
    if len(word) % 2 == 0:
        half1 = word[:len(word)//2]
        half2 = word[len(word)//2:]
    else:
        half1 = word[:len(word)//2]
        half2 = word[len(word)//2+1:]
    i = 0
    while i < len(word)//2:
        word_f += half1[i]
        word_f += half2[i]
        i += 1
    if len(word) % 2 != 0:
        word_f += word[round(len(word)/2)]
    return word_f
    
        
        
def verifica_primo(nro):
    es_primo = True
    for i in range(2, nro):
        if nro % i == 0:
            es_primo = False
            break
    return es_primo

    

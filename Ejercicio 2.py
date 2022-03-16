def ajustar(frase):
    frase = frase.lower()

    acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for acen in acentos:
        if acen in frase:
            frase = frase.replace(acen, acentos[acen])

    caracteres_sobrantes = ' ,.'
    for i in range(len(caracteres_sobrantes)):
        frase = frase.replace(caracteres_sobrantes[i], '')

    return frase

def palindromo(frase, i = 0, j = -1, a = True):
    if i != len(frase):
        if a == True:
            if frase[i] != frase[j]:
                a = False
        i += 1
        j -= 1
        palindromo(frase, i, j, a)

    return a

frase = input('Introduce una frase:')
frase = ajustar(frase)
if palindromo(frase):
    print('Se trata de un palidromo')
else:
    print('No es un palindromo')

# Manipulação de strings
# Escreva uma função que receba um texto e:
# Conte quantas vogais existem.
# Retorne o texto invertido.
# Verifique se o texto é um palíndromo.

vogais ='aeiou'
quant = []
def ver_palavra(palavra):
    #quantas vogais?
    for i in palavra:
        if i in vogais:        
            quant.append(i)
    return print(f'A palavra {palavra} tem:\n',len(quant),'vogais')

def inverter(palavra):
    palavra_invertida = palavra[::-1]
    return print(f"A palavra: {palavra} invertida:",palavra_invertida)

def palindromo(texto):
    if texto.replace(" ", "") == texto.replace(" ", "")[::-1]:
        return print("O texto é um palíndromo ")
    else:
        return print("O texto não é um palíndromo. ")

ver_palavra('aprendizado')
inverter('Breno')
palindromo('subi no onibus') 



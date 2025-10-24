'''Dicionários e compreensão de listas
Dada a lista de nomes ["Ana", "Bruno", "Carlos", "Ana", "Bruno", "Ana"], 
crie um dicionário que mostre quantas vezes cada nome aparece.
Extra: transforme em uma list comprehension que retorna apenas 
os nomes que aparecem mais de uma vez.'''


nomes = ["Ana", "Bruno", "Carlos", "Ana", "Bruno", 'Ana']

dicionario = {
    nome: nomes.count(nome) for nome in nomes
}
print('Quantidade que se repetem os nomes:\n',dicionario)

repetidos = [
    nome for nome, contagem in dicionario.items() if contagem > 1
]

print('Nomes que se repetem:\n',repetidos)
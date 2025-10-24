# Tipos e estruturas de dados
# Crie uma lista com 10 números inteiros.
# Escreva uma função que receba essa lista e retorne:
# O maior valor.
# O menor valor.
# A média dos valores.


l1 = list(range(15))

def v_lista(lista):
  maior_n = max(lista)
  menor_n = min(lista)

  soma = sum(lista)
  media = soma/len(lista)

  return f'''maior número:{maior_n}, menor número:{menor_n}, media: {media}'''

saida = v_lista(l1)
print(saida)
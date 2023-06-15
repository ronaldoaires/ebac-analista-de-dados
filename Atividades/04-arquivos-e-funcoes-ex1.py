# Módulo | Python: Arquivos e funções

# 1. Extraia os valores valor_venda e armazene em uma lista.

valor_vendas = []

with open(file='./arquivos/04/carros.csv', mode='r', encoding='utf8') as arquivo:
  linha = arquivo.readline()
  linha = arquivo.readline()

  while linha:
    separar = linha.split(sep=',')
    valor_venda = separar[1]
    valor_venda = str(valor_venda)
    valor_vendas.append(valor_venda)

    linha = arquivo.readline()

for vendas in valor_vendas:
  print(vendas)
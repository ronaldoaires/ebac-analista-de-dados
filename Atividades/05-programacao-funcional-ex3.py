# Módulo | Python: Programação funcional

# 3. Função reduce - Com a lista de valores de empréstimo pronta, extraia algumas métrica
from functools import reduce

emprestimos = []

with open(file='./arquivos/05/credito.csv', mode='r', encoding='utf8') as fp: 
  fp.readline()
  linha = fp.readline()

  while linha:
    linha_emprestimo = {}
    linha_elementos = linha.strip().split(sep=',')
    linha_emprestimo['id_vendedor'] = linha_elementos[0]
    linha_emprestimo['valor_emprestimos'] = linha_elementos[1]
    linha_emprestimo['quantidade_emprestimos'] = linha_elementos[2] 
    linha_emprestimo['data'] = linha_elementos[3]
    emprestimos.append(linha_emprestimo)
    linha = fp.readline()

valor_emprestimos_lista = list(map(lambda valor: float(valor['valor_emprestimos']), emprestimos))

valor_emprestimos_lista_filtrada = list(filter(lambda valor: valor > 0, valor_emprestimos_lista))

# 1ª Parte: Aplique a função reduce para somar os elementos da lista valor_emprestimos_lista_filtrada na variavel soma_valor_emprestimos.
soma_valor_emprestimos = reduce(lambda soma, valor: soma + valor, valor_emprestimos_lista_filtrada)

print(f'Soma: R${soma_valor_emprestimos:.2f}')

# 2ª Parte: Aplique a função reduce para extrair a média aritmética dos elementos da lista valor_emprestimos_lista_filtrada na variavel media_valor_emprestimos.
media_valor_emprestimos = reduce(lambda soma, valor: soma + valor, valor_emprestimos_lista_filtrada) / len(valor_emprestimos_lista_filtrada)

print(f'Média: R${media_valor_emprestimos:.2f}')

# 3ª Parte: Aplique a função reduce para extrair a média aritmética dos elementos da lista valor_emprestimos_lista_filtrada na variavel desvio_padrao_valor_emprestimos.
quadrado = list(map(lambda v: (v - media_valor_emprestimos) **2, valor_emprestimos_lista_filtrada))
soma = reduce(lambda soma, valor: soma + valor, quadrado)
desvio = (soma / (len(valor_emprestimos_lista_filtrada) -1)) ** 0.5 

print(f'Desvio: R${desvio:.2f}')


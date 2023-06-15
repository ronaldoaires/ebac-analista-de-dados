# Módulo | Python: Programação funcional

# 2. Função filter - Aplique a função filter na lista de valor_emprestimos_lista para filtrar apenas os valores maiores que zero (os valores negativos são erros na base de dados). Salve os valores na lista valor_emprestimos_lista_filtrada.

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

print(valor_emprestimos_lista)

valor_emprestimos_lista_filtrada = list(filter(lambda valor: valor > 0, valor_emprestimos_lista))

print(valor_emprestimos_lista_filtrada)
# Módulo | Python: Programação funcional

# 1. Função map - Aplique a função map na lista de empréstimos para extrair os valores da chave valor_emprestimos na lista valor_emprestimos_lista. Faça também a conversão de str para float

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
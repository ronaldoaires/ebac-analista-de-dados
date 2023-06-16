# Módulo | Python: Tratamento de erros

# 2. Erros em tempo de execução - Neste exercício vamos trabalhar com o arquivo csv com dados de crédito

# O código abaixo deve calcular o total emprestado por cada vendedor mas está "estourando" a exceção ValueError devido a um erro no conjunto de dados. Utilize a estrutura try-catch para garantir que o código seja executado com sucesso.

# Atenção: Você não deve alterar o arquivo de dados.

def valor_total_emprestimo(valor: float, quantidade: int) -> float:
 return valor * quantidade
 
emprestimos = []

with open(file='./arquivos/07/credito.csv', mode='r', encoding='utf8') as fp:
  fp.readline() # cabeçalho
  linha = fp.readline()
  
  while linha:
    try:
      linha_emprestimo = {}
      linha_elementos = linha.strip().split(',')
      linha_emprestimo['id_vendedor'] = linha_elementos[0]
      linha_emprestimo['valor_emprestimos'] = float(linha_elementos[1].replace('"', ''))
      linha_emprestimo['quantidade_emprestimos'] = int(linha_elementos[2])
      linha_emprestimo['data'] = linha_elementos[3]
    except ValueError:
      print('Falha ao processar os dados! ' + 'Abortando o processamento.')
      break
    else:
      emprestimos.append(linha_emprestimo)
      linha = fp.readline()

emprestimos_total = []

for e in emprestimos:
  valor_total = valor_total_emprestimo(e['valor_emprestimos'], e['quantidade_emprestimos'])
  emprestimos_total.append({e['id_vendedor']: valor_total})

for emprestimo_total in emprestimos_total:
  print(emprestimo_total)
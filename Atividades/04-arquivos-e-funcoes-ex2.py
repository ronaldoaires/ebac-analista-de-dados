# Módulo | Python: Arquivos e funções

# 2. Crie uma função para extrair uma coluna de um arquivo csv em uma lista.

def extrair_coluna(arquivo: str, indice: int) -> list:
  colunas = []

  with open(file=arquivo, mode='r', encoding='utf8') as arquivo:
      linha = arquivo.readline()
      linha = arquivo.readline()
      while linha:
        separar = linha.split(sep:=',')
        coluna = separar[indice]
        colunas.append(coluna)

        linha = arquivo.readline()
      
      return colunas

valor_manutencao = extrair_coluna('./arquivos/04/carros.csv', 2)
print(valor_manutencao) 

porta_malas = extrair_coluna('./arquivos/04/carros.csv', 5)
print(porta_malas) 
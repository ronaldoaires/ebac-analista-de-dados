# Módulo | Análise de dados: Data Wrangling I

# 1. Fortune 500 - Utilize o pacote Python  beautifulsoup4  para extrair todas as 100 empresas do arquivo fortune.html. Salve os dados extraidos no arquivo  fortune.csv separado por ;

import csv
from bs4 import BeautifulSoup

# Cria um objeto BeautifulSoup com o conteúdo do arquivo HTML
pagina = BeautifulSoup(open('./arquivos/12/fortune.txt'), 'html.parser')

# Encontra a tabela com a classe 'rt-table'
tabela = pagina.find('div', {'class': 'rt-table'})

# Encontra as linhas da tabela
linhas = tabela.find('div', {'class': 'rt-tbody'})

# Lista para armazenar o conteúdo extraído da tabela
conteudo_extraido = []

# Cabeçalho da tabela
cabecalho = ['rank', 'name', 'revenues', 'revenues-percent-change', 'profits', 'profits-percent-change',
             'assets', 'market-value', 'employees']

# Percorre as linhas da tabela
for linha in linhas:
    # Encontra as colunas da linha
    colunas = linha.find('div', {'role': 'row'})

    # Obtém o texto das colunas, separando por ponto e vírgula
    texto_coluna = colunas.get_text(';').split(';')

    # Adiciona o texto das colunas à lista de conteúdo extraído
    conteudo_extraido.append(texto_coluna)

# Abre o arquivo CSV no modo de escrita
with open(file='./arquivos/12/fortune.csv', mode='w', newline='', encoding='utf-8') as arquivo:
    # Cria um objeto writer do módulo csv
    escrever = csv.writer(arquivo, delimiter=';')

    # Escreve o cabeçalho e o conteúdo extraído no arquivo CSV
    escrever.writerows([cabecalho] + conteudo_extraido)

print('Arquivo CSV gerado com sucesso!')

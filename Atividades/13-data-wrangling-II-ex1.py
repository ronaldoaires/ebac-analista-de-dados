# Módulo | Análise de dados: Data Wrangling II

# 1. Estados - O arquivo estados-bruto.xml contém informações sobre estados (nome, sigla e região). Utilize o pacote Python BeautifulSoup para extrair os dados do arquivo e salve os dados extraidos no arquivo estados-limpo.csv separado por ;

import csv
from bs4 import BeautifulSoup

# Cria um objeto BeautifulSoup com o conteúdo do arquivo XML
xml = BeautifulSoup(open('./arquivos/13/estados-bruto.xml'), 'html.parser')

# Encontra o elemento 'estados' no XML
estados = xml.find('estados')

# Lista para armazenar o conteúdo extraído
conteudo_extraido = []

# Percorre todos os elementos 'estado' dentro do elemento 'estados'
for dados in estados.find_all('estado'):
    # Obtém o texto do elemento 'estado' e divide em linhas separadas
    dado = dados.get_text().split('\n')
    
    # Extrai as informações de UF, sigla e região
    uf = dado[2]
    sigla = dado[4]
    regiao = dado[5]
    
    # Adiciona as informações à lista de conteúdo extraído
    conteudo_extraido.append([uf, sigla, regiao])

# Abre o arquivo CSV no modo de escrita
with open(file='./arquivos/13/estados-limpo.csv', mode='w', newline='', encoding='utf-8') as arquivo:
    # Cria um objeto writer do módulo csv
    escrever = csv.writer(arquivo, delimiter=';')
    
    # Escreve o cabeçalho e o conteúdo extraído no arquivo CSV
    escrever.writerows([['estado', 'sigla', 'regiao']] + conteudo_extraido)

# Mensagem de sucesso
print('Arquivo CSV gerado com sucesso!')

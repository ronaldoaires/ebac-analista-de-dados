# Módulo | Análise de dados: Coleta de Dados II

''' 2. Crawling & Scraping - Utilize os pacotes Python requests e beautifulsoup4 para extrair os 10 filmes mais populares do IMDB (titulo, ano e nota). Escreva os dados extraídos no arquivo csv imdb.csv separado por ; no seguinte formato:

ranking;titulo;ano;nota
1;The Shawshank Redemption;1994;9.2
2;The Godfather;1972;9.1
3;The Godfather: Part II;1974;9.0
'''

import csv
import re
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

conteudo = None
url = 'https://www.imdb.com/chart/top/'

try:
    # Faz a requisição GET para a URL especificada
    resposta = requests.get(url)
    
    # Verifica se ocorreu um erro na requisição
    resposta.raise_for_status()
except HTTPError as exc:
    # Se ocorrer um erro HTTP, exibe a mensagem de erro
    print(exc)
else:
    # Se a requisição for bem-sucedida, armazena o conteúdo da resposta
    conteudo = resposta.text

# Cria um objeto BeautifulSoup com o conteúdo da página
pagina = BeautifulSoup(conteudo, 'html.parser')

# Lista para armazenar o conteúdo extraído da tabela
conteudo_extraido = []

# Encontra a tabela com a classe 'chart'
tabela = pagina.find('table', {'class': 'chart'})

# Percorre todas as linhas da tabela
for linha in tabela.find_all('tr'):
    textos_coluna = []
    
    # Percorre todas as colunas da linha
    for coluna in linha.find_all('td'):
        # Obtém o texto da coluna, remove espaços em branco no início e no fim e divide em linhas separadas
        texto_coluna = coluna.get_text().strip().split('\n')
        textos_coluna += texto_coluna
        
    # Adiciona as linhas de texto da coluna à lista de conteúdo extraído
    conteudo_extraido.append(textos_coluna)

# Lista para armazenar os dados dos filmes
filmes = []

# Extrai os dados dos 10 primeiros filmes (ignorando a primeira linha que contém os cabeçalhos)
for top in conteudo_extraido[1:11]:
    r, titulo, a, nota = [top[1], top[2], top[3], top[4]]
    
    # Extrai o número de classificação, título, ano e nota do filme
    ranking = ''.join(re.findall("\d+", r))
    ano = ''.join(re.findall("\d+", a))
    
    # Adiciona os dados do filme à lista de filmes
    filmes.append([ranking, titulo, ano, nota])

    # Abre o arquivo CSV no modo de escrita
    with open(file='./arquivos/11/imdb.csv', mode='w', newline='', encoding='latin-1') as arquivo:
        # Cria um objeto writer do módulo csv
        escrever = csv.writer(arquivo, delimiter=';')
        
        # Escreve os dados no arquivo CSV
        escrever.writerows([['ranking', 'titulo', 'ano', 'nota']] + filmes)

print('Ranking de filmes gerado com sucesso!')
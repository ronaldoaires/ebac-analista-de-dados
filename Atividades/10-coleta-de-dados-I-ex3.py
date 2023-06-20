# Módulo | Análise de dados: Coleta de Dados I

# 3. Texto para CSV - Extraia os números de contato do arquivo texto ebac.txt e salve-os no arquivo csv contato_ebac.csv com o separador ;

import re
import csv

contatos = []

# Abre o arquivo de texto no modo de leitura
with open(file='./arquivos/10/ebac.txt', mode='r', encoding='utf8') as arquivo:
    # Lê todas as linhas do arquivo
    linhas = arquivo.readlines()
    
    # Filtra as linhas vazias
    linhas = filter(lambda linha: linha != '\n', linhas)
    
    # Remove espaços em branco no início e no fim de cada linha
    linhas = map(lambda linha: linha.strip(), linhas)
    
    # Converte as linhas filtradas e formatadas em uma lista
    linhas = list(linhas)

    # Filtra as linhas que contêm 'WhatsApp'
    whatsapps = list(filter(lambda linha: 'WhatsApp' in linha, linhas))
    
    # Filtra as linhas que contêm 'Telefone'
    telefones = list(filter(lambda linha: 'Telefone' in linha, linhas))

    # Processa as linhas de WhatsApps
    for linha in whatsapps:
        # Separa o tipo ('WhatsApp') do número
        separar = linha.split('+')
        tipo = separar[0]
        
        # Limpa o número, removendo caracteres não numéricos
        limpar_numero = re.findall("[0-9]", separar[1])
        numero = ''.join(limpar_numero)
        
        # Adiciona o tipo e número à lista de contatos
        contatos.append([tipo, numero])

    # Processa as linhas de telefones
    for linha in telefones:
        # Separa o tipo ('Telefone') do número
        separar = linha.split('+')
        tipo = separar[0]
        
        # Limpa o número, removendo caracteres não numéricos
        limpar_numero = re.findall("[0-9]", separar[1])
        numero = ''.join(limpar_numero)
        
        # Adiciona o tipo e número à lista de contatos
        contatos.append([tipo, numero])

    # Abre o arquivo CSV no modo de escrita
    with open(file='./arquivos/10/contato_ebac.csv', mode='w', newline='', encoding='utf8') as arquivo:
        # Cria um objeto writer do módulo csv
        escrever = csv.writer(arquivo, delimiter=';')
        
        # Escreve os dados no arquivo CSV
        escrever.writerows([['tipo','numero']] + contatos)

# Exibe uma mensagem indicando que o arquivo CSV foi gerado com sucesso
print('Arquivo CSV gerado com sucesso!')


# Módulo | Python: Variáveis & Tipos de Dados
# Caderno de Exercícios

# 1. Google Colab
# Escreva o texto "Olá mundo!", utilize o comando print

print('Olá mundo!')

# 2. Números
# Preencha as células de código para preencher os valores de (A), (B) e (C) na tabela de
# ticket médio

a = 3 * 320.52
print(a)

b = 834.47 / 119.21
print(b)

c = 15378.12 / 5
print(c)

# 3. Strings
# Aplique três métodos distintos na string abaixo

cancao = 'Roda mundo, roda gigante, roda moinho, roda pião.'

cancao = 'Roda mundo, roda gigante, roda moinho, roda pião.'
print(cancao.upper())
cancao = 'Roda mundo, roda gigante, roda moinho, roda pião.'
print(cancao.lower())
cancao = 'Roda mundo, roda gigante, roda moinho, roda pião.'
print(cancao.title())

# Extraia da string abaixo o valor da taxa selic na variável selic e o valor do ano na variavel ano . Imprima os valores na tela.

noticia = '''
Selic vai a 2,75% e supera expectativas;
é a primeira alta em 6 anos.
'''
selic = noticia[13:17]
print(selic)
ano = noticia[-8:-7]
print(ano)

##### 4. Booleanos #####
# Utilize a tabela da verdade para responder: qual o valor da variável x?
a = False
b = True
x = not a & b
print(x)

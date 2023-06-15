# Desafio Arquivos e funções 

# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para cada um.

cds = input('Quantidade de CDs?')

valores = []

for cd in range(int(cds)):
    valor = input(f'Qual o valor do CD? {cd + 1}')
    valores.append(float(valor))

total = sum(valor for valor in valores)
media = total / int(cds)

print(f"Total: R${total:.2f}")
print(f"Média: R${media:.2f}")
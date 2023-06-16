# Desafio:

# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada.

def tabuada(numero: int):
    if numero < 1 or numero > 10:
        print("O número deve estar entre 1 e 10.")
        return
    
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

while True:
    numero_str = input('Informe o número: ')
    try:
        numero = int(numero_str)
        tabuada(numero)
        break
    except ValueError:
        print("Digite um número válido.")


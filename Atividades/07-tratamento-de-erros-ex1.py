# Módulo | Python: Tratamento de erros

# 1. Erros de sintaxe - Identifique o erro de sintaxe nos trechos de código abaixo e corrija-os para que o trecho de código funcione.

credito = {'123': 750, '456': 812, '789': 980}

for chave, valor in credito.items():
    print(f'Para o documento {chave}, o valor do ' + 'escore de crédito é {valor}.'
)

# Funções
def pi()-> float:
    return 3.14159265359
pi = pi()
print(pi)

# Programação Funcional
emails = [
    'ronaldoaires@gmail.com',
    'ronaldoaires@live.com',
    'ronaldoaires@yahoo.com'
]
provedor_da_google = lambda email: 'gmail in email'
emails_google = filter(provedor_da_google, emails)
print(list(emails_google))

# Programação orientação a objetos
class Pessoa(object):
    def __init__(self, nome: str, idade: int, documento: str):
        self.nome = nome
        self.idade = idade
        self.documento = documento

ronaldo = Pessoa(nome="Ronaldo Aires", idade=108, documento="123")


# Módulo | Python: Estruturas de Dados

# 1. Listas

# Criei uma lista chamada filmes com o nome dos 10 primeiros filmes mais bem avaliados no site no IMDB. Imprima o resultado.
filmes = ['Um Sonho de Liberdade','O Poderoso Chefão','Batman: O Cavaleiro das Trevas','O Poderoso Chefão II','12 Homens e uma Sentença','A Lista de Schindler','O Senhor dos Anéis: O Retorno do Rei','Pulp Fiction: Tempo de Violência','O Senhor dos Anéis: A Sociedade do Anel','Três Homens em Conflito']

print(filmes)
print(len(filmes))

# Simule a movimentação do ranking. Utilize os métodos insert e pop para trocar a posição do primeiro e do segundo filme da lista. Imprima o resultado.

segundoFilme = filmes.pop(1)
filmes.insert(0, segundoFilme)
print(filmes)
print(len(filmes))
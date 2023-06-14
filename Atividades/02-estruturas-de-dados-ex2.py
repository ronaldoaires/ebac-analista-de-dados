# Módulo | Python: Estruturas de Dados

# 2. Conjuntos

# Aconteceu um erro no seu ranking. Simule a duplicação dos três últimos filmes da lista. Imprima o resultado.

filmes = ['Um Sonho de Liberdade','O Poderoso Chefão','Batman: O Cavaleiro das Trevas','O Poderoso Chefão II','12 Homens e uma Sentença','A Lista de Schindler','O Senhor dos Anéis: O Retorno do Rei','Pulp Fiction: Tempo de Violência','O Senhor dos Anéis: A Sociedade do Anel','Três Homens em Conflito']

filmes.append('Pulp Fiction: Tempo de Violência')
filmes.append('O Senhor dos Anéis: A Sociedade do Anel')
filmes.append('Três Homens em Conflito')

print(filmes)
print(len(filmes))

# Utiliza a conversão set e list para remover os valores duplicados. Imprima o resultado.

filmesUnicos = list(set(filmes))
print(filmesUnicos)
print(len(filmesUnicos))
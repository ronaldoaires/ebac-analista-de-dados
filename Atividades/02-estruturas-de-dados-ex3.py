# Módulo | Python: Estruturas de Dados

# 3. Dicionários

# Repita os exercícios da parte 1 (listas). Os elementos da lista filmes devem ser dicionários no seguinte formato: {'nome': <nome-do-filme>, 'ano': <ano do filme>}, 'sinopse': <sinopse do filme>}

filmes = [{'nome':'Um Sonho de Liberdade','ano': 1994, 'sinopse':'Dois homens presos se reúnem ao longo de vários anos, encontrando consolo e eventual redenção através de atos de decência comum.'},
          {'nome':'O Poderoso Chefão','ano': 1972, 'sinopse':'O patriarca idoso de uma dinastia do crime organizado transfere o controle de seu império clandestino para seu filho relutante.'},
          {'nome':'Batman: O Cavaleiro das Trevas','ano': 2008, 'sinopse':'Quando a ameaça conhecida como O Coringa surge de seu passado, causa estragos e caos nas pessoas de Gotham. O Cavaleiro das Trevas deve aceitar um dos maiores testes para combater a injustiça.'},
          {'nome':'O Poderoso Chefão II','ano': 1974, 'sinopse':'Em 1950, Michael Corleone, agora à frente da família, tenta expandir o negócio do crime a Las Vegas, Los Angeles e Cuba. Paralelamente, é revelada a história de Vito Corleone, e de como saiu da Sicília e chegou a Nova Iorque.'},
          {'nome':'12 Homens e uma Sentença','ano': 1957, 'sinopse':'Um jurado que se aposenta tenta evitar um erro judicial forçando seus colegas a reconsiderarem as evidências.'},
          {'nome':'A Lista de Schindler','ano': 1993, 'sinopse':'Depois de testemunhar a perseguição dos judaicos na Polônia ocupada pelos alemães durante a Segunda Guerra Mundial, o industrial Oskar Schindler se começa a preocupar com sua força de trabalho judaica.'},
          {'nome':'O Senhor dos Anéis: O Retorno do Rei','ano': 2003, 'sinopse':'Gandalf e Aragorn lideram o Mundo dos Homens contra o exército de Sauron para desviar o olhar de Frodo e Sam quando eles se aproximam á Montanha da Perdição com o Um Anel.'},
          {'nome':'Pulp Fiction: Tempo de Violência','ano': 1994, 'sinopse':'As vidas de dois assassinos da máfia, um boxeador, um gângster e sua esposa, e um par de bandidos se entrelaçam em quatro histórias de violência e redenção.'},
          {'nome':'O Senhor dos Anéis: A Sociedade do Anel','ano': 2001, 'sinopse':'Um manso hobbit do Condado e oito companheiros partem em uma jornada para destruir o poderoso Um Anel e salvar a Terra-média das Trevas.'},
          {'nome':'Três Homens em Conflito','ano': 1966, 'sinopse':'Um impostor se junta com dois homens para encontrar fortuna num remoto cemitério.'},
          ]

print(filmes)
segundoFilme = filmes.pop(1)
filmes.insert(0, segundoFilme)
print(filmes)


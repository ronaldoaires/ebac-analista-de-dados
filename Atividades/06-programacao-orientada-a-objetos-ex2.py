# Módulo | Python: Programação orientada a objetos

from classes.ArquivoCSV import ArquivoCSV

arquivo = ArquivoCSV('./arquivos/04/carros.csv')
print(arquivo.extrair_linha(0))
print(arquivo.colunas)
print(arquivo.extrair_linha(9))
print(arquivo.extrair_coluna_da_linha(10,1))

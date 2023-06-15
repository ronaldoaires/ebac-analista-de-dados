# Módulo | Python: Programação orientada a objetos

from classes.ArquivoTexto import ArquivoTexto

arquivo = ArquivoTexto('./arquivos/04/musica.txt')
print(arquivo.extrair_linha(8))
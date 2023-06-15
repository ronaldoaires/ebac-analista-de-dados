# Módulo | Python: Arquivos e funções

# 4. Crie uma função para extrair as palavras de uma linha de um arquivo txt em uma lista.

def extrair_linha(arquivo: str, linha: int) -> str:
    """
    Extrai uma linha específica de um arquivo e retorna uma string com as palavras da linha.

    Args:
        arquivo (str): O caminho do arquivo a ser lido.
        linha (int): O número da linha a ser extraída.

    Returns:
        str: Uma string contendo as palavras da linha extraída.

    Raises:
        OSError: Se ocorrer um erro ao abrir o arquivo especificado.
        IndexError: Se o número da linha estiver fora do intervalo válido.
        Exception: Se ocorrer algum erro desconhecido durante a leitura do arquivo.

    Example:
        >>> arquivo = 'texto.txt'
        >>> linha = extrair_linha(arquivo, 3)
        >>> print(linha)
        'Esta é a terceira linha.'

    """
    try:
        with open(file=arquivo, mode='r', encoding='utf8') as arquivo:
            linhas = arquivo.readlines()

            if linha >= len(linhas):
                raise IndexError(f'Linha {linha} não existe')

            palavras = linhas[linha].split()

        return ' '.join(palavras)

    except OSError:
        print(f'Impossível abrir o arquivo {arquivo}')
    except IndexError as e:
        print(str(e))
    except Exception:
        print('Erro ao fazer leitura')


linha = extrair_linha('./arquivos/04/musica.txt', 9)
print(linha)

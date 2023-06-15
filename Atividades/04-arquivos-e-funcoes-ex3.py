# Módulo | Python: Arquivos e funções

# 3. Crie uma função para extrair uma coluna do arquivo csv em uma lista. Os elementos devem ter o tipo de dado correto.

def extrair_coluna(arquivo: str, indice: int, tipo: str) -> list:
    """
    Extrai uma coluna específica de um arquivo e retorna uma lista dos valores.

    Args:
        arquivo (str): O caminho do arquivo a ser lido.
        indice (int): O índice da coluna a ser extraída.
        tipo (str): O tipo de dado esperado na coluna. Pode ser 'str', 'int', 'float' ou 'bool'.

    Returns:
        list: Uma lista dos valores da coluna extraída.

    Raises:
        OSError: Se ocorrer um erro ao abrir o arquivo especificado.
        IndexError: Se o índice da coluna estiver fora do intervalo válido.
        ValueError: Se o tipo especificado não corresponder ao tipo real dos valores na coluna.
        Exception: Se ocorrer algum erro desconhecido durante a leitura do arquivo.

    Notes:
        - O arquivo deve estar no formato CSV (valores separados por vírgula).
        - A primeira linha do arquivo é ignorada, assumindo que seja um cabeçalho.

    Example:
        >>> arquivo = 'dados.csv'
        >>> coluna = extrair_coluna(arquivo, 2, 'float')
        >>> print(coluna)
        [1.5, 2.7, 3.9, 4.2, 5.0]

    """
    try:
        colunas = []

        with open(file=arquivo, mode='r', encoding='utf8') as arquivo:
            linha = arquivo.readline()
            linha = arquivo.readline()

            while linha:
                separar = linha.split(sep=',')
                coluna = separar[indice]

                if tipo == 'str':
                    str(coluna)
                elif tipo == 'int':
                    int(coluna)
                elif tipo == 'float':
                    float(coluna)
                else:
                    bool(coluna)

                colunas.append(coluna)
                linha = arquivo.readline()

        return colunas

    except OSError:
        print(f'Impossível abrir o arquivo {arquivo}')
    except IndexError:
        print(f'O índice {indice} não existe')
    except ValueError:
        print(f'Tipo da coluna {tipo} inválido')
    except Exception:
        print('Erro ao fazer leitura')


valor_venda = extrair_coluna('./arquivos/04/carros.csv', 1, 'str')
print(valor_venda)

pessoas = extrair_coluna('./arquivos/04/carros.csv', 4, 'int')
print(pessoas) 
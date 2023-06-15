# 2. Crie uma classe para ler arquivos de csv

# Ela deve extender (herdar) a classe ArquivoTexto para reaproveitar os seus atributos ( self.arquivo e self.conteudo ) e método ( self.extrair_linha ). Além disso, adicione o seguinte atributo: self.colunas : Atributo do tipo list onde os elementos são os nome das colunas; A classe também deve conter o seguinte método: self.extrair_coluna_da_linha : Método que recebe como parâmetro o numero da linha e o indice da coluna e retorna o valor em questão.

from classes.ArquivoTexto import ArquivoTexto

class ArquivoCSV(ArquivoTexto):
    """
    Classe para leitura de arquivos CSV.

    Attributes:
        arquivo (str): O caminho do arquivo CSV.
        conteudo (list): Uma lista onde cada elemento representa uma linha do arquivo.
        colunas (list): Uma lista contendo os nomes das colunas do arquivo CSV.
    Methods:
        _nome_colunas(): Obtém os nomes das colunas do arquivo CSV.
        extrair_coluna_da_linha(linha: int, coluna: int) -> str: Extrai o valor de uma coluna específica em uma linha.
    """

    def __init__(self, arquivo: str):
        """
        Inicializa a classe ArquivoCSV.
        Args:
            arquivo (str): O caminho do arquivo CSV.
        """
        super().__init__(arquivo)
        self.colunas = self._nome_colunas()

    def _nome_colunas(self):
        """
        Obtém os nomes das colunas do arquivo CSV.
        Returns:
            list: Uma lista contendo os nomes das colunas.
        """
        try:
            return self.conteudo[0].strip().split(',')

        except IndexError:
            print(f'O arquivo {self.arquivo} está vazio')
            return []
        except Exception as e:
            print(f'Erro desconhecido ao obter os nomes das colunas: {str(e)}')
            return []

    def extrair_coluna_da_linha(self, linha: int, coluna: int) -> str:
        """
        Extrai o valor de uma coluna específica em uma linha.
        Args:
            linha (int): O número da linha.
            coluna (int): O índice da coluna.
        Returns:
            str: O valor da coluna na linha especificada.
        Raises:
            IndexError: Se o número da linha ou o índice da coluna estiverem fora do intervalo válido.
        """
        try:
            if linha < 0 or linha >= len(self.conteudo):
                raise IndexError(f'Linha {linha} não existe')
            if coluna < 0 or coluna >= len(self.colunas):
                raise IndexError(f'Coluna {coluna} não existe')

            colunas = []

            for linha_csv in self.conteudo:
                separar = linha_csv.strip().split(',')
                colunas.append(separar)

            return colunas[linha][coluna]

        except IndexError as e:
            print(str(e))
            return ''
        except Exception as e:
            print(f'Erro desconhecido ao extrair valor da coluna: {str(e)}')
            return ''

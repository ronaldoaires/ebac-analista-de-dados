# 1. Crie uma classe para ler arquivos de texto

# Ela deve conter os seguintes atributos: self.arquivo : Atributo do tipo str com o nome do arquivo; self.conteudo : Atributo do tipo list onde cada elemento é uma linha do arquivo; A classe também deve conter o seguinte método: self.extrair_linha : Método que recebe como parâmetro o número da linha e retorna o seu conteúdo.

class ArquivoTexto(object):
    """
    Classe para manipulação de arquivos de texto.
    Attributes:
        arquivo (str): O caminho do arquivo de texto.
        conteudo (list): Uma lista onde cada elemento representa uma linha do arquivo.
    Methods:
        _conteudo(): Obtém o conteúdo do arquivo e armazena em uma lista.
        extrair_linha(linha: int) -> str: Extrai uma linha específica do arquivo.
    """

    def __init__(self, arquivo: str):
        """
        Inicializa a classe ArquivoTexto.
        Args:
            arquivo (str): O caminho do arquivo de texto.
        """
        self.arquivo = arquivo
        self.conteudo = self._conteudo()

    def _conteudo(self):
        """
        Obtém o conteúdo do arquivo e armazena em uma lista.
        Returns:
            list: Uma lista onde cada elemento representa uma linha do arquivo.
        """
        try:
            with open(file=self.arquivo, mode='r', encoding='utf8') as arquivo:
                conteudo = arquivo.readlines()
                return conteudo

        except FileNotFoundError:
            print(f'Arquivo {self.arquivo} não encontrado')
            return []
        except OSError:
            print(f'Erro ao abrir o arquivo {self.arquivo}')
            return []
        except Exception as e:
            print(f'Erro desconhecido ao ler o arquivo: {str(e)}')
            return []

    def extrair_linha(self, linha: int) -> str:
        """
        Extrai uma linha específica do arquivo.
        Args:
            linha (int): O número da linha a ser extraída.
        Returns:
            str: A linha extraída do arquivo.
        Raises:
            IndexError: Se o número da linha estiver fora do intervalo válido.
        """
        try:
            if linha < 0 or linha >= len(self.conteudo):
                raise IndexError(f'Linha {linha} não existe')

            return self.conteudo[linha].rstrip('\n')

        except IndexError as e:
            print(str(e))
            return ''
        except Exception as e:
            print(f'Erro desconhecido ao extrair linha: {str(e)}')
            return ''
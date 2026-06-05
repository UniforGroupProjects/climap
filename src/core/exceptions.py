class AppException(Exception):

    def __init__(
        self,
        message: str
    ):
        self.message = message

        super().__init__(message)

class CidadeNaoEncontrada(AppException):

    def __init__(self):
        super().__init__(
            "Cidade não encontrada"
        )


class ServicoExternoIndisponivel(AppException):

    def __init__(self):
        super().__init__(
            "Serviço externo indisponível"
        )


class UFInvalida(AppException):

    def __init__(self):
        super().__init__(
            "UF inválida ou inexistente"
        )

class NomeInvalido(Exception):

    def __init__(self, nome: str):
        self.nome = nome
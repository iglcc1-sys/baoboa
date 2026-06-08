import re


def _validar_nome(nome: str) -> bool:
    return bool(nome and isinstance(nome, str) and len(nome.strip()) >= 5)


def _validar_cpf(cpf: str) -> bool:
    if not cpf or not isinstance(cpf, str):
        return False
    digitos = re.sub(r"\D", "", cpf)
    return len(digitos) == 11 and digitos.isdigit()


def _validar_telefone(telefone: str) -> bool:
    if telefone is None:
        return True
    if not isinstance(telefone, str):
        return False
    digitos = re.sub(r"\D", "", telefone)
    return 10 <= len(digitos) <= 11 and digitos.isdigit()


def _validar_email(email: str) -> bool:
    if email is None:
        return True
    return isinstance(email, str) and "@" in email


class Cliente:
    def __init__(self, nome: str, cpf: str, telefone: str = None, email: str = None):
        self._nome = nome.strip() if _validar_nome(nome) else None
        self._cpf = re.sub(r"\D", "", cpf) if _validar_cpf(cpf) else None
        self._telefone = re.sub(r"\D", "", telefone) if telefone and _validar_telefone(telefone) else None
        self._email = email if email and _validar_email(email) else None

    def getNome(self) -> str:
        return self._nome

    def getCpf(self) -> str:
        return self._cpf

    def getTelefone(self) -> str:
        return self._telefone

    def getEmail(self) -> str:
        return self._email

    def alterarTelefone(self, telefone: str) -> None:
        if _validar_telefone(telefone):
            self._telefone = re.sub(r"\D", "", telefone) if telefone else None

    def alterarEmail(self, email: str) -> None:
        if _validar_email(email):
            self._email = email if email else None

    def __str__(self) -> str:
        return f"Cliente(nome={self._nome}, cpf={self._cpf}, telefone={self._telefone}, email={self._email})"

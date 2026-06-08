from typing import List, Optional

from conta import ContaBancaria


class Banco:
    def __init__(self, nome: str, codigo: int):
        if not self._validar_nome(nome):
            raise ValueError("Nome do banco deve ter pelo menos 3 caracteres")
        if not self._validar_codigo(codigo):
            raise ValueError("Código do banco deve ser maior que zero")

        self._nome = nome.strip()
        self._codigo = codigo
        self._contas: List[ContaBancaria] = []

    @staticmethod
    def _validar_nome(nome: str) -> bool:
        return isinstance(nome, str) and len(nome.strip()) >= 3

    @staticmethod
    def _validar_codigo(codigo: int) -> bool:
        return isinstance(codigo, int) and codigo > 0

    def adicionarConta(self, conta: ContaBancaria) -> bool:
        if conta is None:
            return False
        if conta.getBanco() is not self:
            return False
        if self.buscarConta(conta.getNumero()) is not None:
            return False
        self._contas.append(conta)
        return True

    def removerConta(self, numero: int) -> bool:
        conta = self.buscarConta(numero)
        if conta is None:
            return False
        self._contas.remove(conta)
        return True

    def buscarConta(self, numero: int) -> Optional[ContaBancaria]:
        for conta in self._contas:
            if conta.getNumero() == numero:
                return conta
        return None

    def quantidadeContas(self) -> int:
        return len(self._contas)

    def listarContas(self) -> List[ContaBancaria]:
        return list(self._contas)

    def getNome(self) -> str:
        return self._nome

    def getCodigo(self) -> int:
        return self._codigo

    def __str__(self) -> str:
        return f"Banco(nome={self._nome}, codigo={self._codigo}, contas={len(self._contas)})"

class ContaBancaria:
    def __init__(self, numero: int, titular, banco, saldo_inicial: float = 0.0):
        if not self._validar_numero(numero):
            raise ValueError("Número da conta deve ser maior que zero")
        if titular is None:
            raise ValueError("Titular é obrigatório")
        if banco is None:
            raise ValueError("Banco é obrigatório")

        self._numero = numero
        self._titular = titular
        self._banco = banco
        self._saldo = saldo_inicial if saldo_inicial >= 0 else 0.0

    @staticmethod
    def _validar_numero(numero: int) -> bool:
        return isinstance(numero, int) and numero > 0

    def depositar(self, valor: float) -> None:
        if isinstance(valor, (int, float)) and valor > 0:
            self._saldo += float(valor)

    def sacar(self, valor: float) -> bool:
        if not isinstance(valor, (int, float)) or valor <= 0:
            return False
        if valor > self._saldo:
            return False
        self._saldo -= float(valor)
        return True

    def consultarSaldo(self) -> float:
        return self._saldo

    def getNumero(self) -> int:
        return self._numero

    def getTitular(self):
        return self._titular

    def getBanco(self):
        return self._banco

    def estaAtiva(self) -> bool:
        return self._saldo > 0

    def __str__(self) -> str:
        return f"ContaBancaria(numero={self._numero}, saldo={self._saldo:.2f}, titular={self._titular.getNome()})"

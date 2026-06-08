from banco import Banco
from cliente import Cliente
from conta import ContaBancaria


def main() -> None:
    banco = Banco("Banco do Futuro", 42)

    cliente1 = Cliente("Alice Pereira", "123.456.789-01", "11987654321", "alice@email.com")
    cliente2 = Cliente("Bruno Silva", "98765432100", "21912345678", "bruno@exemplo.com")
    cliente3 = Cliente("Carla Souza", "11122233344", None, "carla@teste.com")

    conta1 = ContaBancaria(1001, cliente1, banco, 500.0)
    conta2 = ContaBancaria(1002, cliente2, banco, 250.0)
    conta3 = ContaBancaria(1003, cliente2, banco, 0.0)
    conta4 = ContaBancaria(1004, cliente3, banco, 100.0)

    for conta in [conta1, conta2, conta3, conta4]:
        banco.adicionarConta(conta)

    conta1.depositar(150.0)
    conta2.sacar(100.0)
    conta3.depositar(300.0)
    conta4.sacar(50.0)
    conta3.sacar(50.0)

    total_banco = sum(conta.consultarSaldo() for conta in banco.listarContas())

    print("Dados do banco")
    print("--------------")
    print(f"Nome: {banco.getNome()}")
    print(f"Código: {banco.getCodigo()}")
    print(f"Quantidade de contas cadastradas: {banco.quantidadeContas()}")
    print()

    print("Dados dos clientes e contas")
    print("---------------------------")
    clientes_vistos = set()
    for conta in banco.listarContas():
        titular = conta.getTitular()
        if titular.getCpf() not in clientes_vistos:
            clientes_vistos.add(titular.getCpf())
            print(titular)
        print(f"  Conta número: {conta.getNumero()}")
        print(f"  Saldo: R$ {conta.consultarSaldo():.2f}")
        print(f"  Ativa: {conta.estaAtiva()}")
        print()

    print("Resumo final")
    print("-------------")
    print(f"Saldo total armazenado pelo banco: R$ {total_banco:.2f}")


if __name__ == "__main__":
    main()

# Sistema Bancário - TADs em Python

Este projeto implementa um pequeno sistema bancário em Python usando os conceitos de Tipos Abstratos de Dados (TADs), encapsulamento, composição, agregação e regras de negócio.

## Estrutura de arquivos
- `cliente.py`: implementação do TAD `Cliente`
- `banco.py`: implementação do TAD `Banco`
- `conta.py`: implementação do TAD `ContaBancaria`
- `main.py`: programa de demonstração que cria clientes, contas e um banco

## Subprogramas criados
A solução foi dividida em funções pequenas e reutilizáveis para manter o código organizado e evitar duplicação. As principais funções de validação são:
- `_validar_nome(nome)`: garante que o nome exista, não esteja vazio e tenha pelo menos 5 caracteres
- `_validar_cpf(cpf)`: normaliza o CPF removendo pontuação e exige exatamente 11 dígitos numéricos
- `_validar_telefone(telefone)`: verifica que o telefone, quando informado, tenha 10 ou 11 dígitos válidos
- `_validar_email(email)`: garante que o e-mail contenha o caractere `@`

Além disso, cada TAD define seus próprios métodos de acesso e operação:
- `Cliente.getNome`, `Cliente.getCpf`, `Cliente.getTelefone`, `Cliente.getEmail`
- `Cliente.alterarTelefone`, `Cliente.alterarEmail`
- `Banco.adicionarConta`, `Banco.removerConta`, `Banco.buscarConta`, `Banco.quantidadeContas`, `Banco.listarContas`
- `ContaBancaria.depositar`, `ContaBancaria.sacar`, `ContaBancaria.consultarSaldo`, `ContaBancaria.estaAtiva`

Esses subprogramas foram criados para encapsular regras de negócio e tornar o sistema fácil de manter.

## Relacionamentos entre as classes
Os relacionamentos foram implementados de forma direta e natural:
- `ContaBancaria` mantém uma referência para um objeto `Cliente` como seu titular.
- `ContaBancaria` também mantém uma referência para um objeto `Banco` ao qual pertence.
- `Banco` mantém uma coleção de objetos `ContaBancaria` para representar todas as contas registradas.

Dessa forma a composição e a agregação aparecem claramente:
- `Banco` agrega várias contas bancárias.
- `ContaBancaria` é composta por um cliente e uma referência ao banco.
- Um cliente pode aparecer em várias contas sem que o cliente precise armazenar diretamente a lista de contas.

## Regras de negócio com maior esforço
As regras de negócio mais exigentes foram as validações de entrada, principalmente:
- CPF: aceitar valores com ou sem pontuação e normalizar para apenas dígitos.
- Telefone: permitir entrada opcional, mas exigir formato correto quando informado.
- E-mail: manter a informação opcional e validar apenas se existe.

Também foi importante garantir que o banco não aceitasse duas contas com o mesmo número e que uma conta só fosse adicionada se já estivesse associada ao mesmo banco.

## Encapsulamento e abstração
O encapsulamento foi usado ao manter atributos internos privados (`_nome`, `_cpf`, `_telefone`, `_email`, `_contas`, `_saldo`) e oferecer acesso somente por meio de métodos públicos. Isso protege o estado interno e assegura que regras de negócio sejam sempre verificadas antes de aceitar valores.

A abstração aparece na forma de TADs: cada classe define um contrato claro de operações e oculta detalhes internos. Por exemplo, um cliente pode alterar seu e-mail através de `alterarEmail`, mas a validação fica escondida dentro da classe.

## Como executar
No terminal, execute:

```bash
python main.py
```

O programa exibirá os dados do banco, os clientes, as contas, saldos individuais e o saldo total armazenado pelo banco.

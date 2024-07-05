class ContaBancaria:
    usuarios_cadastrados = {}

    def __init__(self, titular, cpf, senha, saldo=0):
        self.titular = titular
        self.cpf = cpf
        self.senha = senha.lower()  # Converte a senha para minúsculas
        self.saldo = saldo

    def titular_conta(self):
        return self.titular

    def verificar_saldo(self):
        print(f'Saldo atual da conta de {self.titular}: R${self.saldo:.2f}')

    def depositar(self, deposito):
        self.saldo += deposito
        print(f'Depósito de R${deposito:.2f} realizado. Novo saldo: R${self.saldo:.2f}')

    def sacar(self, saque):
        if saque > self.saldo:
            print('Saldo insuficiente. Faça depósito em sua conta.')
            print(f'Saldo ATUAL R$: {self.saldo} x Tentativa de Saque R$: {saque} = Faltam R$', saque - self.saldo)
        else:
            self.saldo -= saque
            print(f'Saque de R${saque:.2f} realizado. Novo saldo: R${self.saldo:.2f}')

    @staticmethod
    def cadastro_de_usuarios():
        while True:
            try:
                titular = input('Digite seu nome completo: ').strip()
                if ' ' not in titular:
                    print("Digite nome e sobrenome.")
                    continue
                cpf = input('Digite seu CPF (apenas números): ').strip()
                if len(cpf) != 11 or not cpf.isdigit():
                    print("Digite um CPF válido com 11 dígitos.")
                    continue
                senha = input('Digite sua senha: ').lower().strip()
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite novamente.")

        ContaBancaria.usuarios_cadastrados[titular] = {'cpf': cpf, 'senha': senha}
        print("Usuário cadastrado com sucesso!")

    @staticmethod
    def entrada():
        while True:
            try:
                titular = input('Digite seu nome completo: ').strip()
                if titular not in ContaBancaria.usuarios_cadastrados:
                    print("Usuário não cadastrado.")
                    continue

                cpf = input('Digite seu CPF: ').strip()
                senha = input('Digite sua senha: ').lower().strip()

                if (ContaBancaria.usuarios_cadastrados[titular]['cpf'] == cpf and
                        ContaBancaria.usuarios_cadastrados[titular]['senha'] == senha):
                    print("Login realizado com sucesso!")
                    break
                else:
                    print("Dados incorretos. Verifique seu CPF e senha e tente novamente.")
            except KeyError:
                print("Usuário não encontrado.")
            except ValueError:
                print("Entrada inválida. Por favor, digite novamente.")

        # Após login bem-sucedido, cria a instância da conta
        conta = ContaBancaria(titular, cpf, senha)

        while True:
            print("""
            Qual operação deseja fazer:
            [1] - Verificar Saldo
            [2] - Sacar
            [3] - Depositar
            [0] - Sair
            """)
            try:
                operacao = int(input("Qual operação deseja realizar: "))
                if operacao not in [0, 1, 2, 3]:
                    print("Operação inválida. Por favor, escolha uma opção válida.")
                    continue
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
                continue

            if operacao == 1:
                conta.verificar_saldo()

            elif operacao == 2:
                while True:
                    try:
                        saque = float(input('Digite o valor do saque: '))
                        conta.sacar(saque)
                        break
                    except ValueError:
                        print("Valor inválido. Por favor, digite um número.")

            elif operacao == 3:
                while True:
                    try:
                        deposito = float(input('Digite o valor do depósito: '))
                        conta.depositar(deposito)
                        break
                    except ValueError:
                        print("Valor inválido. Por favor, digite um número.")

            elif operacao == 0:
                break

        return conta


# Exemplo de uso:

# Cadastrar um usuário
ContaBancaria.cadastro_de_usuarios()

# Realizar login e operações bancárias
result = ContaBancaria.entrada()

# Verificar o saldo final da conta
print(f"Titular da conta: {result.titular_conta()}")
result.verificar_saldo()
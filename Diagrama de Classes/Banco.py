from Conta import Conta

class Banco:

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.contas = []

    def cadastrar(self, conta):
        if self.procurar_conta(conta.ID):
            print(f"Erro: Já existe uma conta com o ID {conta.ID}.")
            return False

        self.contas.append(conta)
        print(f"Conta para {conta.titular} (ID: {conta.ID}) cadastrada com sucesso!")
        return True

    def procurar_conta(self, ID):
        for conta in self.contas:
            if conta.ID == ID:
                return conta
        return None

    def excluir_conta(self, ID):
        conta = self.procurar_conta(ID)
        if conta:
            self.contas.remove(conta)
            print(f"Conta {ID} (Titular: {conta.titular}) excluída com sucesso.")
            return True
        else:
            print(f"Erro: Conta com ID {ID} não encontrada.")
            return False

    def transferir(self, id_origem, id_destino, valor):
        origem = self.procurar_conta(id_origem)
        destino = self.procurar_conta(id_destino)

        if not origem:
            print(f"Erro: Conta de origem (ID: {id_origem}) não encontrada.")
            return False
        if not destino:
            print(f"Erro: Conta de destino (ID: {id_destino}) não encontrada.")
            return False
        if origem == destino:
            print("Erro: A conta de origem e destino não podem ser as mesmas.")
            return False

        if origem.sacar(valor):
            destino.depositar(valor)
            print("Transferência realizada com sucesso.")
            return True
        else:
            print("Transferência falhou. Verifique o saldo de origem.")
            return False

    def listar_contas(self):
        if not self.contas:
            print("Nenhuma conta cadastrada no banco.")
            return

        print(f"\n--- Lista de Contas do {self.nome} ---")
        for conta in self.contas:
            print(conta)
        print("---------------------------------------")


def mostrar_menu():
    print("\n===== MENU BANCO DIGITAL =====\n1. Criar Conta\n2. Consultar Saldo\n3. Depositar\n4. Sacar\n5. Transferir\n6. Listar Contas\n7. Excluir Conta\n8. Sair\n==============================")
    return input("Escolha uma opção: ")


def main():
    meu_banco = Banco("Banco Digital", "001")

    while True:
        opcao = mostrar_menu()

        if opcao == '1':
            print("\n[ Criar Nova Conta ]")
            ID = input("Digite o ID da conta (ex: 123): ")
            titular = input("Digite o nome do titular: ")
            try:
                saldo_inicial = float(input("Digite o depósito inicial (ou 0): "))
                nova_conta = Conta(ID, titular, saldo_inicial)
                meu_banco.cadastrar(nova_conta)
            except ValueError:
                print("Erro: Saldo inicial inválido. Use apenas números.")

        elif opcao == '2':
            print("\n[ Consultar Saldo ]")
            ID = input("Digite o ID da conta: ")
            conta = meu_banco.procurar_conta(ID)
            if conta:
                print(f"Saldo da conta {ID}: R$ {conta.get_saldo():.2f}")
            else:
                print("Conta não encontrada.")

        elif opcao == '3':
            print("\n[ Depositar ]")
            ID = input("Digite o ID da conta: ")
            conta = meu_banco.procurar_conta(ID)
            if conta:
                valor = input("Digite o valor a depositar: ")
                conta.depositar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == '4':
            print("\n[ Sacar ]")
            ID = input("Digite o ID da conta: ")
            conta = meu_banco.procurar_conta(ID)
            if conta:
                valor = input("Digite o valor a sacar: ")
                conta.sacar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == '5':
            print("\n[ Transferir ]")
            id_origem = input("Digite o ID da conta de ORIGEM: ")
            id_destino = input("Digite o ID da conta de DESTINO: ")
            valor = input("Digite o valor a transferir: ")

            try:
                val_float = float(valor)
                meu_banco.transferir(id_origem, id_destino, val_float)
            except ValueError:
                print("Erro: Valor de transferência inválido.")


        elif opcao == '6':
            meu_banco.listar_contas()

        elif opcao == '7':
            print("\n[ Excluir Conta ]")
            ID = input("Digite o ID da conta a excluir: ")
            meu_banco.excluir_conta(ID)

        elif opcao == '8':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()
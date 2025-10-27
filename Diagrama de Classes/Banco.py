class Banco:

    def __init__(self, nome, numero, contas):
        self.nome = nome
        self.contas = []

    def cadastrar(self, conta):
        self.contas.append(conta)

    def procurar_conta(self, ID):
        for conta in self.contas:
            if conta.ID == ID_conta:
                return conta
        return None

    def excluir_conta(self, ID):
        for conta in self.contas:
            if conta.ID == ID_conta:
                del conta

class Conta:

    def __init__(self, ID, saldo, valor, titular):
        self.ID = ID
        self.saldo = saldo
        self.valor = valor
        self.titular = titular

    def creditar(self,valor, saldo):
        Conta.valor += saldo

    def debitar(self,valor,saldo):
        Conta.valor -= saldo

    def saldo_total(self,saldo):
        print(saldo)

    def transferir(self,ID,valor, saldo):
        origem = self.procurar_conta(id_origem)
        destino = self.procurar_conta(id_destino)
        if not origem or not destino:
            return None
        else:
            origem.saldo -= valor
            destino.saldo += valor

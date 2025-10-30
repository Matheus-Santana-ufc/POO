class Conta:

    def __init__(self, ID, titular, saldo_inicial=0.0):
        self.ID = ID
        self.titular = titular
        self._saldo = float(saldo_inicial)

    def depositar(self, valor):
        try:
            valor = float(valor)
            if valor > 0:
                self._saldo += valor
                print(f"Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {self._saldo:.2f}")
                return True
            else:
                print("Erro: O valor do depósito deve ser positivo.")
                return False
        except ValueError:
            print("Erro: Valor de depósito inválido.")
            return False

    def sacar(self, valor):
        try:
            valor = float(valor)
            if valor <= 0:
                print("Erro: O valor do saque deve ser positivo.")
                return False

            if self._saldo >= valor:
                self._saldo -= valor
                print(f"Saque de R$ {valor:.2f} realizado. Novo saldo: R$ {self._saldo:.2f}")
                return True
            else:
                print(f"Erro: Saldo insuficiente (Saldo: R$ {self._saldo:.2f})")
                return False
        except ValueError:
            print("Erro: Valor de saque inválido.")
            return False

    def get_saldo(self):
        return self._saldo

    def __str__(self):
        return f"Conta [ID: {self.ID}, Titular: {self.titular}, Saldo: R$ {self._saldo:.2f}]"
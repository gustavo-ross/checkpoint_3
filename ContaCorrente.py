from Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, saldo=0.0):
        super().__init__(numero, cliente, saldo)
        self.taxa = 1.00 # Taxa de operação

    # Polimorfismo / Sobrescrita
    def sacar(self, valor):
        valor_total = valor + self.taxa
        if 0 < valor and valor_total <= self._saldo:
            self._saldo -= valor_total
            print(f"✅ Saque de R$ {valor:.2f} efetuado. (Taxa de R$ {self.taxa:.2f} cobrada)")
            return True
        else:
            print("❌ Saldo insuficiente para o saque + taxa da Conta Corrente.")
            return False

    def to_dict(self):
        dados = super().to_dict()
        dados["tipo"] = "ContaCorrente"
        return dados
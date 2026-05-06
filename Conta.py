class Conta:
    def __init__(self, numero, cliente, saldo=0.0):
        self.numero = numero
        self.cliente = cliente
        self._saldo = saldo

    def get_saldo(self):
        return self._saldo

    def depositar(self, valor, silencioso=False):
        if valor > 0:
            self._saldo += valor
            if not silencioso:
                print(f"✅ Depósito de R$ {valor:.2f} efetuado com sucesso!")
            return True
        else:
            print("❌ Valor inválido para depósito.")
            return False

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f"✅ Saque de R$ {valor:.2f} efetuado com sucesso!")
            return True
        else:
            print("❌ Saldo insuficiente ou valor inválido.")
            return False

    def transferir(self, valor, conta_destino, is_pix=False):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            conta_destino.depositar(valor, silencioso=True)
            
            if is_pix:
                print(f"💸 BZZZT! PIX de R$ {valor:.2f} enviado com sucesso para {conta_destino.cliente.nome}!")
            else:
                print(f"🔄 Transferência interna de R$ {valor:.2f} concluída com sucesso!")
            return True
        else:
            print("❌ Saldo insuficiente para realizar a operação.")
            return False

    def to_dict(self):
        return {
            "numero": self.numero,
            "cliente": self.cliente.to_dict(),
            "saldo": self._saldo
        }
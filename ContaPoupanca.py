from Conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, numero, cliente, saldo=0.0):
        super().__init__(numero, cliente, saldo)

    def render_juros(self):
        # Simulando 100% do CDI (Ex: rendimento de 1% ao mês)
        rendimento = self._saldo * 0.01
        self._saldo += rendimento
        print(f"📈 Rendimento do mês aplicado! + R$ {rendimento:.2f} na sua poupança.")

    def to_dict(self):
        dados = super().to_dict()
        dados["tipo"] = "ContaPoupanca"
        return dados
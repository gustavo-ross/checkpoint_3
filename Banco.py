import json
from Cliente import Cliente
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

class Banco:
    def __init__(self):
        self.contas = []
        self.carregar_dados()

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        self.salvar_dados()

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None

    def cpf_ja_cadastrado(self, cpf):
        for conta in self.contas:
            if conta.cliente.cpf == cpf:
                return True
        return False

    def salvar_dados(self):
        dados = [conta.to_dict() for conta in self.contas]
        with open("banco.json", "w") as f:
            json.dump(dados, f, indent=4)

    def carregar_dados(self):
        try:
            with open("banco.json", "r") as f:
                dados = json.load(f)
                for item in dados:
                    # Adicionado a leitura da senha (usamos .get para evitar erros com contas antigas)
                    senha_salva = item["cliente"].get("senha", "1234") 
                    cli = Cliente(item["cliente"]["nome"], item["cliente"]["cpf"], senha_salva)
                    
                    if item["tipo"] == "ContaCorrente":
                        self.contas.append(ContaCorrente(item["numero"], cli, item["saldo"]))
                    elif item["tipo"] == "ContaPoupanca":
                        self.contas.append(ContaPoupanca(item["numero"], cli, item["saldo"]))
        except (FileNotFoundError, json.JSONDecodeError):
            self.contas = []
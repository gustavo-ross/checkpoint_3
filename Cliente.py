class Cliente:
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha

    def to_dict(self):
        return {"nome": self.nome, "cpf": self.cpf, "senha": self.senha}
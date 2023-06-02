class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # quando eu preciso do contexto da classe
    @classmethod
    def criar_de_ano_nascimento(cls, ano, nome):
        idade = 2023 - ano
        return cls(nome, idade)
    
    # se não preciso de contexto nem de classe nem da instância
    @staticmethod
    def maior_de_idade(idade):
        return idade >= 18

p1 = Pessoa("José", 45)
print(p1.nome, p1.idade)

p2 = Pessoa.criar_de_ano_nascimento(1989, "João")
print(p2.nome, p2.idade)

print(Pessoa.maior_de_idade(17))
print(Pessoa.maior_de_idade(25))

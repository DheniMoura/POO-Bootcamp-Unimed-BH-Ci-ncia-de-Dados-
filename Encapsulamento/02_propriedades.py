class Pessoa:
    def __init__(self, nome, ano_nasc):
        self._nome = nome
        self._ano_nasc = ano_nasc

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2023
        return _ano_atual - self._ano_nasc
    
p1 = Pessoa("José", 1984)

print(f"Nome: {p1.nome} \tIdade: {p1.idade}")

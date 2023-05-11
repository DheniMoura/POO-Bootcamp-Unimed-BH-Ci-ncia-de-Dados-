class Bicicleta:
    # Atributos
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    # Métodos
    def buzinar(self):
        print("Buzinando!")

    def parar(self):
        print("Bicicleta parada")

    def correr(self):
        print("Bicicleta correndo")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

# instanciando um objeto
b1 = Bicicleta("Vermelha", "Caloi", 2022, 600)
b2 = Bicicleta("Amarelo", "Monark", 1998, 250)

# ambas as formas de executar o método são equivalentes
b1.buzinar()
Bicicleta.buzinar(b1)

# acessando os atributos
print(b1.cor, b1.modelo)
print(b1)
print(b2)
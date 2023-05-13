class Veiculo:
    def __init__(self, cor, placa, qtd_rodas):
        self.cor = cor
        self.placa = placa
        self.qtd_rodas = qtd_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"



class Motocicleta(Veiculo):
    pass



class Carro(Veiculo):
    pass



class Caminhao(Veiculo):
    def __init__(self, cor, placa, qtd_rodas, carregado):
        super().__init__(cor, placa, qtd_rodas)
        self.carregado = carregado

    def carregado(self):
        print(f"{'sim' if self.carregado else 'não'}")



m1 = Motocicleta("preto", "ABC1234", 2)
cr1 = Carro("branco", "BDC2345", 4)
cm1 = Caminhao("branco", "CDE3456", 8, False)
print(m1)
print(cr1)
print(cm1)
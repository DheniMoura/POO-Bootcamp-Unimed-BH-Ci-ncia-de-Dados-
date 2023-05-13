class Animal:
    def __init__(self, qtd_patas):
        self.qtd_patas = qtd_patas
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"



class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo



class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)



class Gato(Mamifero):
    pass


class FalarMixin:
    def falar(self):
        print(' Estou falando')

class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_pelo, **kw):
        super().__init__(cor_pelo, **kw)
        # print(Ornitorrinco.mro()) # para saber a hierarquia

g1 = Gato(qtd_patas=4, cor_pelo="branco")
o1 = Ornitorrinco(qtd_patas=4, cor_pelo="preto", cor_bico="marrom")

print(g1)
print(o1)
o1.falar()
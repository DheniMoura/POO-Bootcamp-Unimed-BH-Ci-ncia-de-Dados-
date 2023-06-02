# Interfaces definem o que uma classe deve fazer e não como
# Python permite heranças múltiplas, mas não tem a palavra reservada interface
# utilizar o módulo abc (abstract base class)
# um método se torna abstrato quando utilizamos o @abstractmethod

from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC): #interface
    # As classes que herdarem de ControleRemoto deverão implementar os métodos abstratos
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    # propriedade
    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
    
    def desligar(self):
        print("Desligando a TV")

    @property
    def marca(self):
        return "LG"


class ControleArCond(ControleRemoto):
    def ligar(self):
        print("Ligando o ar-condicionado")
    
    def desligar(self):
        print("Desligando o ar-condicionado")

    @property
    def marca(self):
        return "Consul"


c1 = ControleTV()
c1.ligar()
c1.desligar()
print(c1.marca)

c2 = ControleArCond()
c2.ligar()
c2.desligar()
print(c2.marca)
'''
O método construtor sempre é executado quando uma nova instância da classe é criada.
Nesse método inicializamos o estado do objeto.
Para declarar o método construtor da classe, cria-se um método com o nome __init__
'''


class Cachorro:
    
    # exemplo de construtor
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("auau")


    '''
    Sempre é executado quando uma instância (objeto) é destruída.
    Destrutores em Python não são tão necessário quando em C++ porque o Python tem um
    coletor de lixo que lida com o gerenciamento de memória automaticamente.
    Para declarar o método destrutor da classe, cria-se um método como nome __del__.
    '''

    # exemplo de destrutor
    def __del__(self):
        print("Destruindo a instância")


# Nesse exemplo o objeto é excluído na sequência
def criar_cachorro():
        c = Cachorro("Zeus", "Branco", True)
        print(c.nome)


c1 = Cachorro("Boby", "Merlin", True)
print(c1.latir())
c2 = Cachorro("Mila", "Caramelo", False)

del c2

criar_cachorro()
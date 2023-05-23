class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0
    
    @x.setter #necessário para atribuir valor a x, já que é um property
    def x(self, value):
        self._x += value
    
    @x.deleter #necessário para para deletar x, podendo realmente deletar ou atribuir novo valor
    def x(self):
        self._x = -1

foo = Foo(10)
print(foo.x)
foo.x=10
print(foo.x)
del foo.x
print(foo.x)
class Animal:
    def emitir_som(self):
        raise NotImplementedError("Subclasses devem implementar este método")

class Cachorro(Animal):
    def emitir_som(self):
        return 'Au au'


class Gato(Animal):
    def emitir_som(self):
        return 'Minhau'
class Pato(Animal):
    def emitir_som(self):
        return 'Quá quá'

pato1 = Pato()
print(pato1.emitir_som())
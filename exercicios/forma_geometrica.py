import math
class FormaGeometrica:
    def calcular_perimetro(self):
        return None
        

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def calcular_perimetro(self):
        return self.largura * self.altura


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    def calcular_perimetro(self):
        return math.pi * self.raio ** 2
 

circulo1 = Circulo(5)
print(circulo1.calcular_perimetro())
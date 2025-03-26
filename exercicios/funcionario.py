class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
       return salario_base

class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus):
        self.nome = nome
        self.salario_base = salario_base
        self.bonus = bonus
    def calcular_salario(self):
        return self.salario_base + self.salario_base*(self.bonus/100)

class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, comissao):
        self.nome = nome
        self.salario_base = salario_base
        self.comissao = comissao
    def calcular_salario(self):
        return self.salario_base + self.comissao

f1 = Gerente('Francisco', 3000, 10)
f2 = Gerente('Joao', 3000, 10)
f3 = Gerente('Zé', 3000, 10)
f4 = Gerente('Tico', 3000, 10)

lista_final = [f1, f2, f3, f4]

def Folha_de_pagamento(lista_final):
    for i in lista_final:
        print(i.nome)
        print(i.calcular_salario())
        

print(Folha_de_pagamento(lista_final))





    

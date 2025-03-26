class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
       return salario_base

class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus)
        self.nome = nome
        self.salario_base = salario_base
        self.bonus = bonus
    def calcular_salario(self):
        return salario_base + bonus

class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, comissao)
        self.nome = nome
        self.salario_base = salario_base
        self.comissao = comissao
    def calcular_salario(self):
        return salario_base + comissao

    

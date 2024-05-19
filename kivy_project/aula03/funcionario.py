class Funcionario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.horas = {}
        self.salario_hora = {}
    
    def cadastro_hora(self, mes, horas):
        if mes not in self.horas:
            self.horas[mes] = horas
    
    def cadastro_salario_hora(self, mes, valor):
        if mes not in self.salario_hora:
            self.salario_hora[mes] = valor
    
    def calcula_salario(self, mes):
        if mes not in self.horas or mes not in self.salario_hora:
            print('Mês Inexistente!!')
        else:
            return self.horas[mes] * self.salario_hora[mes]
    
    def __repr__(self):
        return f'Funcionário: {self.nome},\nEmail: {self.email},\nhoras/mês: {self.horas},\nsalário-hora: {self.salario_hora}'

# Comentários explicativos sobre o código:

# - Definição da classe Funcionario com métodos para cadastro de horas, cadastro de salário por hora

#   e cálculo do salário em um determinado mês.

# - Os atributos incluem nome, email, horas e salário por hora, armazenados em dicionários.

# - Método __repr__ para representar o funcionário como uma string.


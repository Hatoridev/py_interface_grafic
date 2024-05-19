from funcionario import Funcionario

funcionario = Funcionario('Matheus', 'matheus@blablabla.com.br')
funcionario.cadastro_hora('Jan', 300)
funcionario.cadastro_hora('Fev', 200)
funcionario.cadastro_salario_hora('Jan', 30)
funcionario.cadastro_salario_hora('Fev', 30)

print(funcionario)
print(funcionario.calcula_salario('Jan'))
print(funcionario.calcula_salario('Fev'))

# Comentários explicativos sobre o código:

# - Importação da classe Funcionario do arquivo funcionarios.py.

# - Instanciação de um objeto Funcionario com nome 'Matheus' e email 'matheus@blablabla.com.br'.

# - Cadastro de horas trabalhadas para os meses de Janeiro e Fevereiro.

# - Cadastro de salário por hora para os meses de Janeiro e Fevereiro.

# - Impressão dos dados do funcionário usando o método __repr__.

# - Cálculo do salário para os meses de Janeiro e Fevereiro usando o método calcula_salario.


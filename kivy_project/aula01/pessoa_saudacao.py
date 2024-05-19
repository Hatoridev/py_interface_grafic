class Pessoa:
    idade = 15
    
    def saudacao(self):
        print('Olá Pessoas!')

matheus = Pessoa()

print(matheus.idade)
print(matheus.saudacao)
matheus.saudacao()

# Comentários explicativos sobre o arquivo:

# - A classe Pessoa é definida com um atributo idade e um método saudacao().

# - Um objeto matheus da classe Pessoa é instanciado.

# - É impresso o valor do atributo idade do objeto matheus.

# - É mostrada a referência para o método saudacao do objeto matheus.

# - O método saudacao do objeto matheus é chamado, resultando na impressão da saudação "Olá Pessoas!".


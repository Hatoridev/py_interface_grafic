from area import Retangulo
import math

while True:
    piso_a = float(input("Digite um lado do piso: "))
    piso_b = float(input("Digite o outro lado do piso: "))
    piso = Retangulo(piso_a, piso_b)
    
    az_a = float(input("Digite o lado do azulejo: "))
    az_b = float(input("Digite o outro lado do azulejo: "))
    azulejo = Retangulo(az_a, az_b)
    
    area_piso = piso.area()
    area_az = azulejo.area()
    
    qntd_az = area_piso / area_az
    
    if area_piso % area_az == 0:
        print(f'A quantidade exata de azulejos para preencher o piso é de {qntd_az}')
    else:
        print(f'A quantidade mínima de azulejos para preencher o piso é de {math.ceil(qntd_az)}')

# Comentários explicativos sobre o código:

# - Importação da classe Retangulo do módulo area e da biblioteca math para cálculos matemáticos.

# - Loop infinito que solicita ao usuário os lados do piso e dos azulejos.

# - Criação de instâncias da classe Retangulo para o piso e os azulejos com os valores fornecidos pelo usuário.

# - Cálculo das áreas do piso e dos azulejos usando o método area da classe Retangulo.

# - Cálculo da quantidade de azulejos necessários para cobrir o piso.

# - Verificação se a área do piso é divisível pela área dos azulejos sem resto.

# - Impressão da quantidade exata ou mínima de azulejos necessários para cobrir o piso.


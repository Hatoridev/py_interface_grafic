import time
import os

class Cronometro:
    def __init__(self, segundos=0, minutos=0, horas=0):
        self.segundos = segundos
        self.minutos = minutos
        self.horas = horas
    
    def __repr__(self):
        return f'{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}'

    def incremento(self):
        self.segundos += 1
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
            if self.minutos >= 60:
                self.minutos = 0
                self.horas += 1
    
    def start(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do console
            print(self)
            self.incremento()
            time.sleep(1)

cronometro1 = Cronometro()
cronometro1.start()

# Comentários explicativos sobre o código:

# - Importação dos módulos time e os.

# - Definição da classe Cronometro com métodos para inicialização, incremento e execução do cronômetro.

# - Método __repr__ para representar o cronômetro como uma string formatada.

# - Método incremento para aumentar os segundos, minutos e horas.

# - Método start para iniciar o cronômetro e atualizar a tela a cada segundo.

# - Criação de uma instância de Cronometro chamada cronometro1 e chamada do método start para iniciar o cronômetro.


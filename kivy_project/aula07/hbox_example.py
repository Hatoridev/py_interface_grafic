import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]
        for i in range(5):
            btn = Button(text=f"Este é o botão {i+1}", background_color=random.choice(colors))
            layout.add_widget(btn)
        return layout

if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()

# Comentários explicativos:

# - Importa o módulo random para geração de cores aleatórias

# - Importa a classe App do módulo kivy.app

# - Importa a classe Button do módulo kivy.uix.button

# - Importa a classe BoxLayout do módulo kivy.uix.boxlayout

# - Define as cores RGB utilizadas na aplicação

# - Classe HBoxLayoutExample que herda de App

#     - Método build para construir a interface do aplicativo

#         - Cria uma instância da classe BoxLayout com padding

#         - Define uma lista de cores para os botões

#         - Cria 5 botões com texto e cor de fundo aleatória e os adiciona ao layout

#         - Retorna o layout

# - Verifica se o arquivo está sendo executado como o programa principal

#     - Cria uma instância da classe HBoxLayoutExample e executa o aplicativo


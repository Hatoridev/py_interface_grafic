from kivy.app import App
from kivy.uix.image import AsyncImage

class MainApp(App):
    def build(self):
        img = AsyncImage(source='https://supermariorun.com/assets/img/stage/mario03.png',
                         size_hint=(1, 5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        return img

if __name__ == '__main__':
    app = MainApp()
    app.run()

# Comentários explicativos:

# - Importa a classe App do módulo kivy.app

# - Importa a classe AsyncImage do módulo kivy.uix.image

# - Classe MainApp que herda de App

#     - Método build para construir a interface do aplicativo

#         - Cria uma instância da classe AsyncImage com uma imagem online

#         - Retorna a imagem

# - Verifica se o arquivo está sendo executado como o programa principal

#     - Cria uma instância da classe MainApp e executa o aplicativo


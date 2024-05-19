from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        button = Button(text='Clique em mim!')
        button.bind(on_press=self.on_press_button)
        return button

    def on_press_button(self, instance):
        print('Você apertou o botão!')

if __name__ == '__main__':
    app = ButtonApp()
    app.run()

# Importações:

# - Importando a classe App do módulo kivy.app

# - Importando a classe Button do módulo kivy.uix.button

# Classe ButtonApp:

# - Definindo a classe principal do aplicativo, que herda de App

# - Método build é chamado ao iniciar o aplicativo

# - Criando um widget Button com texto e configurando o evento on_press

# - Método on_press_button é chamado quando o botão é pressionado e imprime uma mensagem

# Execução do aplicativo:

# - Verifica se o script está sendo executado diretamente

# - Cria uma instância da classe ButtonApp

# - Executa o aplicativo


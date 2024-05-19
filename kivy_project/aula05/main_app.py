from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        label = Label(
            text='Fala galera!',
            size_hint=(.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        return label

if __name__ == '__main__':
    app = MainApp()
    app.run()

# Importações:

# - Importando a classe App do módulo kivy.app

# - Importando a classe Label do módulo kivy.uix.label

# Classe MainApp:

# - Definindo a classe principal do aplicativo, que herda de App

# - Método build é chamado ao iniciar o aplicativo

# - Criando um widget Label com texto e configurações de layout

# - Retornando o label para ser exibido na tela

# Execução do aplicativo:

# - Verifica se o script está sendo executado diretamente

# - Cria uma instância da classe MainApp

# - Executa o aplicativo


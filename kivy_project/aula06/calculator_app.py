from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "-", "+"]
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.solution)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Clear the solution widget
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                # Don’t add two operators right after each other
                return
            elif current == "" and button_text in self.operators:
                # First character cannot be an operator
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text

        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            try:
                # Evaluate the solution and set it to the text input
                solution = str(eval(self.solution.text))
                self.solution.text = solution
            except Exception:
                self.solution.text = "Error"

if __name__ == '__main__':
    app = MainApp()
    app.run()

# Importações:

# - Importando a classe App do módulo kivy.app

# - Importando a classe BoxLayout do módulo kivy.uix.boxlayout

# - Importando a classe Button do módulo kivy.uix.button

# - Importando a classe TextInput do módulo kivy.uix.textinput

# Classe MainApp:

# - Definindo a classe principal do aplicativo, que herda de App

# - Método build é chamado ao iniciar o aplicativo

# - Inicializa operadores, controle de estado de operadores e último botão pressionado

# - Cria e configura o layout principal e o campo de solução

# - Define e adiciona botões numéricos e operacionais ao layout principal

# - Adiciona o botão de igualdade e vincula a função de cálculo da solução

# Método on_button_press:

# - Manipula os eventos de clique dos botões

# - Atualiza o campo de solução com o texto do botão pressionado

# - Limpa o campo de solução se o botão 'C' for pressionado

# - Evita a inserção de operadores consecutivos

# - Não permite que o primeiro caractere seja um operador

# Método on_solution:

# - Manipula o evento de clique do botão de igualdade

# - Avalia a expressão no campo de solução e atualiza o resultado

# - Trata exceções e exibe "Error" se a expressão for inválida

# Execução do aplicativo:

# - Verifica se o script está sendo executado diretamente

# - Cria uma instância da classe MainApp

# - Executa o aplicativo


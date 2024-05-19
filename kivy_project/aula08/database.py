import datetime

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}
        for line in self.file:
            email, password, name, created = line.strip().split(":")
            self.users[email] = (password, name, created)
        self.file.close()

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), self.get_date())
            self.save()
            return 1
        else:
            print("Email already exists")
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ":" + self.users[user][0] + ":" + self.users[user][1] + ":" + self.users[user][2] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]

# Importações:

# - Importando o módulo datetime para manipulação de datas e horas

# Classe DataBase:

# - Define uma classe para manipular um banco de dados simples de usuários

# - Método __init__ é chamado ao criar uma instância da classe e inicializa os atributos

# - Método load carrega os dados do arquivo de banco de dados

# - Método get_user retorna informações de um usuário com base no email

# - Método add_user adiciona um novo usuário ao banco de dados

# - Método validate verifica se o email e a senha fornecidos correspondem a um usuário válido

# - Método save salva os dados do banco de dados no arquivo

# - Método estático get_date retorna a data atual como uma string formatada

class UserInput:
    """class to interact with user"""

    def __init__(self):
        self.api_key = ''
        self.address = ''
        self.url = ''
        self.lang = 'ru'

    def api_input(self):
        while True:
            self.api_key = input("Введите API-ключ к сервису Dadata:\n")
            if len(self.api_key) == 40 and self.api_key.isalnum():
                break
            else:
                print("Введен явно неверный ключ, повторите ввод.")

    def address_input(self):
        self.address = input("Пожалуйста, введите адрес ('S' - изменение настроек, 'Q' - выход): ").lower()

    def settings(self):
        menu = ''
        while menu != '0':
            menu = input("Пожалуйста, выберите значение, которое хотите изменить:\n"
                         "1 - URL-адрес, 2 - API-ключ, 3 - язык ответа на запрос.\n"
                         "Чтобы вернуться к вводу адреса нажмите '0'. ")
            if menu == '1':
                self.url = input("Введите новый URL, по которому будет отправляться запрос:\n")
            elif menu == '2':
                while True:
                    self.api_key = input("Введите API-ключ к сервису Dadata:\n")
                    if len(self.api_key) == 40 and self.api_key.isalnum():
                        break
                    else:
                        print("Введен явно неверный ключ.")
            elif menu == '3':
                while True:
                    self.lang = input("Выберете язык ответов на запросы (ru/en): ")
                    if self.lang == 'en' or self.lang == 'ru':
                        break
                    else:
                        print("Неверный ввод.")
            elif menu == '0':
                self.address = input("Пожалуйста, введите адрес: ").lower()
            else:
                print("Неверный ввод.")

    def index_input(self, data):
        while True:
            index = input("Пожалуйста, выберете интересующий Вас адрес из списка и введите его номер: ")
            if index.isalpha():
                print("Неверный ввод.")
            elif int(index) > len(data['suggestions']) or int(index) < 1:
                print("Неверный ввод.")
            else:
                return index

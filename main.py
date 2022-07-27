import requests
import sqlite3
database = sqlite3.connect('settings.db')
curs = database.cursor()
curs.execute('SELECT url FROM settings')
URL = curs.fetchone()[0]
curs.execute('SELECT api_key FROM settings')
API_KEY = curs.fetchone()[0]
curs.execute('SELECT lang FROM settings')
LANG = curs.fetchone()[0]
print("Вас приветствует программа по поиску географических координат по заданному адресу.")
if API_KEY == "":
    print("Для начала работы, пожалуйста, введите API-ключ от сервиса Dadata.", end='\n')
    check = 0
    while check == 0:
        API_KEY = input()
        if len(API_KEY) == 40 and API_KEY.isalnum():
            check = 1
            curs.execute(f'UPDATE settings SET api_key = "{API_KEY}"')
            database.commit()
        else:
            print("Введен явно неверный ключ, повторите ввод.")
print("Чтобы изменить пользовательские настройки (Базовый URL к сервису Dadata, API-ключ,")
print("язык ответа от сервиса) нажмите 'S', для выхода из программы нажмите 'Q' и 'Enter'.")
headers = {
    "Content-type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Token {API_KEY}",
}
address = input("Пожалуйста, введите адрес: ").lower()
while address != 'q' and address != 'й':
    if address == 's' or address == 'ы':
        print("Чтобы вернуться к вводу адреса нажмите '0'")
        print("Пожалуйста, выберите значение, которое хотите изменить:")
        menu = input("1 - URL-адрес, 2 - API-ключ, 3 - язык ответа на запрос. ")
        if menu == '1':
            new_url = input("Введите новый URL, по которому будет отправляться запрос:\n")
            curs.execute(f'UPDATE settings SET url = "{new_url}"')
            database.commit()
            URL = new_url
        elif menu == '2':
            check = 0
            while check == 0:
                new_api = input("Введите новый API-ключ:\n")
                if len(new_api) == 40 and new_api.isalnum():
                    check = 1
                else:
                    print("Введен явно неверный ключ, повторите ввод.")
            curs.execute(f'UPDATE settings SET api_key = "{new_api}"')
            database.commit()
            API_KEY = new_api
        elif menu == '3':
            new_lang = input("Выберете язык ответов на запросы (ru/en): ")
            if new_lang == 'en' or new_lang == 'ru':
                curs.execute(f'UPDATE settings SET lang = "{new_lang}"')
                database.commit()
                LANG = new_lang
            else:
                print("Неверный ввод.")
        elif menu == '0':
            address = input("Пожалуйста, введите новый адрес ('S' - изменение настроек, 'Q' - выход): ")
        else:
            print("Неверный ввод.")
    else:
        params = {
            'query': address,
            'language': LANG
        }
        data = requests.get(url=URL, params=params, headers=headers)
        result = data.json()
        if (len(result['suggestions']) == 0):
            print("Адреса не обнаружены. Попробуйте переформулировать запрос.")
        else:
            for place in range(len(result['suggestions'])):
                print(place + 1, result['suggestions'][place]['value'], sep=". ", end="\n")
            check = 0
            while check == 0:
                index = input("Пожалуйста, выберете интересующий Вас адрес из списка и введите его номер: ")
                if index.isalpha():
                    print("Неверный ввод.")
                elif int(index) > len(result['suggestions']) or int(index) < 1:
                    print("Неверный ввод.")
                else:
                    check = 1
                    print("Широта объекта: ", result['suggestions'][int(index)-1]['data']['geo_lat'])
                    print("Долгота объекта: ", result['suggestions'][int(index)-1]['data']['geo_lon'])
        address = input("Пожалуйста, введите новый адрес ('S' - изменение настроек, 'Q' - выход): ")
database.close()


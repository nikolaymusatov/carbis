class UserOutput:
    """class for outputting data"""

    def __init__(self):
        pass

    def greeting(self):
        print("Вас приветствует программа по поиску географических координат по заданному адресу.")

    def list_output(self, data):
        if len(data['suggestions']) == 0:
            print("Адреса не обнаружены. Попробуйте переформулировать запрос.")
            return 0
        else:
            for place in range(len(data['suggestions'])):
                print(place + 1, data['suggestions'][place]['value'], sep=". ", end="\n")

    def lat_lon_output(self, data, index):
        print("Широта объекта: ", data['suggestions'][int(index) - 1]['data']['geo_lat'])
        print("Долгота объекта: ", data['suggestions'][int(index) - 1]['data']['geo_lon'])

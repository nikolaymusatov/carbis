from class_db import Database
from class_api import Api
from class_input import UserInput
from class_output import UserOutput


class Application:
    """Main class"""

    def __init__(self):
        pass

    def run(self):
        data = Database()
        data.create()
        user_input = UserInput()
        user_output = UserOutput()
        user_output.greeting()
        if data.select('api_key') == '':
            data.default_values_replace()
            user_input.api_input()
            data.update('api_key', user_input.api_key)
        api = Api(data.select('api_key'))
        user_input.address_input()
        while user_input.address != 'q':
            if user_input.address == 's':
                user_input.settings()
                if user_input.url != '':
                    data.update('url', user_input.url)
                if user_input.api_key != '':
                    data.update('api_key', user_input.api_key)
                data.update('lang', user_input.lang)
            response = api.query(data.select('url'), user_input.address, data.select('lang'))
            if user_output.list_output(response) != 0:
                index = user_input.index_input(response)
                user_output.lat_lon_output(response, index)
            user_input.address_input()
        data.close()


application = Application()
application.run()

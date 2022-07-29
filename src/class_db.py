import sqlite3


class Database:
    """class to work with database"""

    def __init__(self):
        self.database = sqlite3.connect('123.db')
        self.cursor = self.database.cursor()

    def create(self):
        self.cursor.execute("""CREATE TABLE if NOT EXISTS settings(
            url text,
            api_key text,
            lang text)""")
        self.cursor.execute("INSERT INTO settings VALUES ('', '', '')")

    def default_values_replace(self):
        self.cursor.execute("DELETE FROM settings")
        self.cursor.execute("INSERT INTO settings VALUES ('https://suggestions.dadata.ru/suggestions/api/4_1/rs"
                            "/suggest/address', '', 'ru')")

    def select(self, value):
        self.cursor.execute(f"SELECT {value} FROM settings")
        return self.cursor.fetchone()[0]

    def update(self, value, new_value):
        self.cursor.execute(f"UPDATE settings SET {value} = '{new_value}'")
        self.database.commit()

    def close(self):
        self.database.close()

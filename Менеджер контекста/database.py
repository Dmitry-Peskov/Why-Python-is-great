import sqlite3


class ConnectSQLiteDB:

    def __init__(self, db_path: str):
        self.path = db_path

    def __enter__(self):
        self.connect = sqlite3.connect(self.path)
        return self.connect

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connect.close()
        if exc_val:
            raise


if __name__ == "__main__":
    path = "test.db"
    with ConnectSQLiteDB(path) as connect:
        # тут мы получили соединение с БД и внутри блока можем его использовать
        cursor = connect.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print(result)
    # тут соединение с БД было закрыто

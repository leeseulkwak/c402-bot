import mariadb
import sys


class MariaDBConnector:
    def __init__(self, config):
        self.config = config
        self.conn = None

    def connect(self):
        try:
            self.conn = mariadb.connect(**self.config)
            return self.conn
        except mariadb.Error as e:
            print(f"마리아디비 연결시 에러: {e}")
            sys.exit(1)

    def close(self):
        if self.conn:
            self.conn.close()

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'admin',
    'password': '1234',
    'database': 'Chatbot'
}

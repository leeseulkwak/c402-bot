# from utils.DBConnector import MariaDBConnector

import os
import sys

cwd = os.getcwd()
sys.path.append(os.path.join(cwd))
# print(sys.path)

from utils.DBConnector import MariaDBConnector
from config.DBconfig_Chatbot import config

db = None

try:
    db = MariaDBConnector(config)
    conn = db.connect()

    sql = 'select * from chatbot_train_data'
    with conn.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
        # for row in rows:
        #     print(row)
        print(rows)

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()

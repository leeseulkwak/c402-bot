import openpyxl
from utils.DBConnector import MariaDBConnector
import utils.DBConnector
import os

config=utils.DBConnector.config
db = MariaDBConnector(config)
conn=db.connect()


def all_clear_train_data(db):
    sql='''
    delete from chatbot_train_data
'''
    with conn.cursor() as cursor:
         cursor.execute(sql)

    sql='''
    ALTER TABLE chatbot_train_data AUTO_INCREMENT=1
'''
    with conn.cursor() as cursor:
        cursor.execute(sql)

def insert_data(db, xls_row):
    intent, ner, query, answer, answer_img_url=xls_row

    sql='''
    INSERT chatbot_train_data(intent, ner, query, answer, answer_image)
    values(
        '%s', '%s', '%s', '%s', '%s'
    )
''' % (intent.value, ner.value, query.value, answer.value, answer_img_url.value)
    
    sql=sql.replace("'None'", "null")

    
    with conn.cursor() as cursor:
        cursor.execute(sql)
        print('{}저장'.format(query.value))
        conn.commit()

cwd=os.getcwd()
train_file=os.path.join(cwd, 'train_data.xlsx')

print(train_file)

# train_file='./train_data.xlsx'
db=None
try:
    
        all_clear_train_data(db)

        #학습 엑셀 파일 불러오기
        wb=openpyxl.load_workbook(train_file)
        sheet=wb['Sheet1']
        for row in sheet.iter_rows(min_row=2):

            insert_data(db, row)

            
        wb.close()

except Exception as e:
        print(e)

finally:
        if conn is not None:
            conn.close()


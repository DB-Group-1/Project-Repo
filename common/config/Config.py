"""
API 서버의 설정 파일
"""

import pandas as pd
import pymysql

BASE_URL = "http://localhost"
PORT = 5000

DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWORD = "1234"
DB_NAME = 'kakaotalk'

def connect_db(sql: str):
    connection = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8'
    )
    with connection.cursor() as cur:
        if sql.strip().lower().startswith('select'):
            cur.execute(sql)
            result = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            return pd.DataFrame(result, columns=columns)
        else:
            cur.execute(sql)
            connection.commit()
    connection.close()
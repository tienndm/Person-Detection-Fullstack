import os

class PostgreConf:
    user = os.getenv('POSTGRE_USER')
    pwd = os.getenv('POSTGRE_PASSWORD')
    host = os.getenv('POSTGRE_HOST')
    port = os.getenv('POSTGRE_PORT')
    db = os.getenv('POSTGRE_DB')
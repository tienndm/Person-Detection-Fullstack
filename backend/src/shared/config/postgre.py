import os

class PostgreConf:
    host = os.getenv("POSTGRE_HOST", "db")
    port = int(os.getenv("POSTGRE_PORT", 5432))
    user = os.getenv("POSTGRE_USER", "postgres")
    pwd = os.getenv("POSTGRE_PASSWORD", "postgres")
    db = os.getenv("POSTGRE_DB", "postgres")
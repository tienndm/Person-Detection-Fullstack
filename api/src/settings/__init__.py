import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME")
APP_VERSION = os.getenv("APP_VERSION")

SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY", "").lower() == 'true'
SQLALCHEMY_ISOLATION_LEVEL = os.getenv('SQLALCHEMY_ISOLATION_LEVEL') or 'SERIALIZABLE'

DATABASE_URI = os.getenv('DATABASE_URI','sqlite+aiosqlite:///:memory:')
print(DATABASE_URI)

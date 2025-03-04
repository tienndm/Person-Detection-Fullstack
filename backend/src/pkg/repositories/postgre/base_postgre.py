from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BasePostgre:
    def __init__(self, host: str, port: int, user: str, password: str, dbname: str):
        self.engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{dbname}")
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def execute(self, query):
        session = self.get_session()
        try:
            result = session.execute(query)
            session.commit()
            return result
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def add(self, obj):
        session = self.get_session()
        try:
            session.add(obj)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def delete(self, obj):
        session = self.get_session()
        try:
            session.delete(obj)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def createTables(self):
        Base.metadata.create_all(self.engine)
    
    def dropTables(self):
        Base.metadata.drop_all(self.engine)
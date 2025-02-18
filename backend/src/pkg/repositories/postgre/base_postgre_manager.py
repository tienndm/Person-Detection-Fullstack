__doc__ = """
# BasePostgreManager Documentation

## Overview
Handles PostgreSQL connections and query execution using SQLAlchemy. Provides context management (__enter__/__exit__) for safe use of database resources.

## Key Methods
- __init__: Initializes DB connection parameters.
- connect: Connects to the PostgreSQL database.
- execQuery: Executes SQL queries with optional parameters and manages transactions.
- close: Closes the database connection.
- getDate: Returns the current datetime (formatted in ISO) in UTC+7.
- __enter__/__exit__: Support for usage in "with" statements.
"""

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timezone, timedelta
from typing import Optional, List, Any


class BasePostgreManager:
    def __init__(self, host: str, port: int, user: str, password: str, dbname: str):
        """
        Initialize connection parameters for the PostgreSQL database.
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.dbname = dbname
        self.engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{dbname}")
        self.Session = sessionmaker(bind=self.engine)
        self.session = None

    def connect(self):
        """
        Establish a connection to the PostgreSQL database.
        """
        self.session = self.Session()

    def execQuery(self, query: str, params: Optional[dict] = None):
        """
        Execute an SQL query with optional parameters.
        Commits the transaction if not a SELECT statement.
        """
        if not self.session:
            raise RuntimeError("Database session is not established")

        try:
            result = self.session.execute(text(query), params)
            if result.returns_rows:
                return result.fetchall()
            self.session.commit()
            return []
        except Exception as e:
            self.session.rollback()
            raise RuntimeError(f"Failed to execute query: {e}")

    def close(self):
        """
        Close the database session.
        """
        if self.session:
            self.session.close()
            self.session = None

    def getDate(self):
        """
        Return the current datetime in ISO format with UTC+7 timezone.
        """
        return (
            datetime.now(timezone.utc)
            .astimezone(timezone(timedelta(hours=7)))
            .isoformat()
        )

    def __enter__(self):
        """
        Context manager entry; connects to the database.
        """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Context manager exit; closes the database session.
        """
        self.close()

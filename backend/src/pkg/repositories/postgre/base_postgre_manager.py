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

## Author
- Author: Tien Nguyen
- Date: 2025-17-02
"""

from datetime import datetime, timezone, timedelta
from typing import Optional, List, Any
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine, Connection


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
        self.engine: Optional[Engine] = None
        self.connection: Optional[Connection] = None

    def connect(self):
        """
        Establish a connection to the PostgreSQL database.
        """
        try:
            self.engine = create_engine(
                f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"
            )
            self.connection = self.engine.connect()
        except Exception as e:
            raise RuntimeError(f"Failed to connect to database {self.dbname}: {e}")

    def execQuery(self, query: str, params: Optional[List[Any]] = None):
        """
        Execute an SQL query with optional parameters.
        Commits the transaction if not a SELECT statement.
        """
        if not self.connection:
            raise RuntimeError("Database connection is not established")

        try:
            result = self.connection.execute(text(query), params)
            if result.returns_rows:
                return result.fetchall()
            self.connection.commit()
            return []
        except Exception as e:
            self.connection.rollback()
            raise RuntimeError(f"Failed to execute query: {e}")

    def close(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()
            self.connection = None
        if self.engine:
            self.engine.dispose()
            self.engine = None

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
        Context manager exit; closes the database connection.
        """
        self.close()

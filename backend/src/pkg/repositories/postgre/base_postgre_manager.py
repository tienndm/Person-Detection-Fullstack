__doc__ = """
# BasePostgreManager Documentation

## Overview
Handles PostgreSQL connections and query execution. Provides context management (__enter__/__exit__) for safe use of database resources.

## Key Methods
- __init__: Initializes DB connection parameters.
- connect: Connects to the PostgreSQL database.
- execQuery: Executes SQL queries with optional parameters and manages transactions.
- close: Closes the database connection.
- getDate: Returns the current datetime (formatted in ISO) in UTC+7.
- __enter__/__exit__: Support for usage in "with" statements.
"""

import psycopg2

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
        self.connection = None

    def connect(self):
        """
        Establish a connection to the PostgreSQL database.
        """
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                dbname=self.dbname,
            )
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
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                if cursor.description:
                    return cursor.fetchall()
                self.connection.commit()
                return []
        except psycopg2.Error as e:
            self.connection.rollback()
            raise RuntimeError(f"Failed to execute query: {e}")

    def close(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()
            self.connection = None

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

__doc__ = """
# CoreManager Documentation

## Overview
Handles PostgreSQL connections and query execution using SQLAlchemy.

## Key Methods
- __init__: Initializes DB Core Manager.
- insert: insert data into database.
- createTable: create table when not existed.

## Author
- Author: Tien Nguyen
- Date: 2025-17-02
"""

import os
from .base_postgre_manager import BasePostgreManager
from sqlalchemy.engine import Row
from datetime import datetime

class CoreManager(BasePostgreManager):
    def __init__(self, host: str, port: int, user: str, password: str, dbname: str):
        super().__init__(host, port, user, password, dbname)
        self.connect()

    def insert(self, uuid: str, personCount: int):
        input_save_dir = os.path.join("input", f"{uuid}.jpg")
        output_save_dir = os.path.join("output", f"{uuid}.jpg")
        query = """
        INSERT INTO core (person_count, input_save_dir, output_save_dir)
        VALUES (:person_count, :input_save_dir, :output_save_dir)
        """
        params = {
            "person_count": personCount,
            "input_save_dir": input_save_dir,
            "output_save_dir": output_save_dir
        }
        self.execQuery(query=query, params=params)

    def fetch(self):
        query = """
        SELECT * FROM core
        """
        result = self.execQuery(query=query)
        data = [dict(row._mapping) for row in result]
        for row in data:
            for key, value in row.items():
                if isinstance(value, datetime):
                    row[key] = value.isoformat()
        return data

    def createTable(self):
        query = """
        CREATE TABLE IF NOT EXISTS core (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            person_count INT NOT NULL,
            input_save_dir VARCHAR(255) NOT NULL,
            output_save_dir VARCHAR(255) NOT NULL
        )
        """
        self.execQuery(query=query)

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

class CoreManager(BasePostgreManager):
    def __init__(self, host: str, port: int, user: str, password: str, dbname: str):
        super().__init__(host, port, user, password, dbname)
        self.connect()

    def insert(self, uuid: str, personCount: int):
        input_save_dir = os.path.join("input", f"{uuid}.jpg")
        output_save_dir = os.path.join("output", f"{uuid}.jpg")
        query = """
        INSERT INTO core (person_count, input_save_dir, output_save_dir)
        VALUES (%s, %s, %s)
        """
        self.execQuery(query=query, params=[personCount, input_save_dir, output_save_dir])

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

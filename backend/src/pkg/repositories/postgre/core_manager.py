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

from shared.config.detection import DetectionConf


class CoreManager(BasePostgreManager):
    def __init__(self, host: str, port: int, user: str, password: str, dbname: str):
        super().__init__(host, port, user, password, dbname)
        self.connect()

    def insert(self, uuid: str, personCount: int):
        input_save_dir = os.path.join(DetectionConf.savedImageDir, f"input/{uuid}.jpg")
        output_save_dir = os.path.join(
            DetectionConf.savedImageDir, f"output/{uuid}.jpg"
        )
        self.cursor.execute(
            f"INSERT INTO core (person_count, input_save_dir, output_save_dir) VALUES ({personCount}, {input_save_dir}, {output_save_dir})"
        )
        self.connection.commit()

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

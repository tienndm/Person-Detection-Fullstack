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
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime

from .base_postgre_manager import BasePostgreManager
from .base_postgre import BasePostgre

class DetectPersonManager(BasePostgre):
    def __init__(self, host: str, port: int, user: str, password: str, dbname: str):
        super().__init__(host, port, user, password, dbname)

    def insert(self, uuid: str):
        pass

    def fetch(self):
        return self.coreManager.fetch()

    def createTable(self):
        self.coreManager.createTable()

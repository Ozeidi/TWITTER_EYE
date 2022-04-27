# coding=utf-8

import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

from env import DB_URI

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(DB_URI)
Session = sessionmaker(bind=engine)

Base = declarative_base()

# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()
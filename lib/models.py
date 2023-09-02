import os
import sys
sys.path.append(os.getcwd)
from sqlalchemy import (create_engine, PrimaryKeyConstraint, Column, String, Integer, ForeignKey, Table, UniqueConstraint)
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
if __name__ == '__main__':
    engine = create_engine('sqlite:///db/restaurants.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
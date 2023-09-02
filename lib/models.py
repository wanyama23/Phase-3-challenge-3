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
customer_restaurants = Table(
    "customer_restaurants",
    Base.metadata,
    Column("customer_id", ForeignKey("customers.id"), primary_key=True),
    Column("restaurant_id", ForeignKey("restaurants.id"), primary_key=True),
    extend_existing=True,
)

# ....................customers class....................
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
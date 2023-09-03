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
    reviews = relationship("Review", backref=backref ("customer"))
    restaurants = relationship("Restaurant",secondary="customer_restaurants", back_populates="customers")
    def __repr__(self):
        return f'Customer: {self.first_name}'
    def customer_rev(self):
        return self.reviews
    def customer_rest(self):
        return self.restaurants
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def favorite_restaurant(self):
        favorite_restauran = session.query(Restaurant).order_by(Restaurant.star_rating.desc()).first()
        return favorite_restauran
    def add_review(self, restaurant,rating,session):
        review = Review(customer=self, restaurant=restaurant, star_rating=rating)
        session.add (review)
        session.commit()
    def delete_reviews(self, restaurant, session):
        reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from db.settings_db import *

Base = declarative_base()


class CryptoSale(Base):
    __tablename__ = 'cryptosale'
    id = Column(Integer, autoincrement=True, primary_key=True)
    count_coins = Column(Integer)
    price = Column(Integer)
    text = Column(String)
    telephone = Column(String)

    def __init__(self, id, count_coins, price, text, telephone):
        self.id = id
        self.count_coins = count_coins
        self.price = price
        self.text = text
        self.telephone = telephone


Base.metadata.create_all(db)

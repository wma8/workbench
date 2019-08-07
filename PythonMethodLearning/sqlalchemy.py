from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __table__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    password = Column(String(100))
    # review encoding

engine = create_engine('mysql+mysqlconnector://weikun:1234@localhost:3306/dev')
DBSession = sessionmaker(bind=engine)





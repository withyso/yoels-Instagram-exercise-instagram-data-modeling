import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
import enum

Base = declarative_base()

class MyEnum(enum.Enum):
    one = 1
    two = 2
    three = 3

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, index=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True)

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    users_from_id = Column(Integer, ForeignKey('user.id'))
    users_from_id_relationship = relationship(User)
    users_to_id = Column(Integer, ForeignKey('user.id'))
    users_to_id_relationship = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('user.id'))
    users_id_relationship = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String)
    author_id = Column(Integer, ForeignKey('user.id'))
    author_id_relationship = relationship(User)
    post_id = Column=(Integer, ForeignKey('post.id'))
    post_relationship = relationship(Post)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    type = Column(Integer)
    post_id = Column(Integer, ForeignKey('post.id'))
    post_id_relationship = relationship(Post)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

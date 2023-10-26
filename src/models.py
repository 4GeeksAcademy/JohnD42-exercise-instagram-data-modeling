import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class MediaTypeEnum(enum.Enum):
    text = 'text'
    image = 'image'
    video = 'video'

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), primary_key=True)
    email = Column(String(250), primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    media_type = Column(Enum(MediaTypeEnum), nullable=False)
    url = Column(String(250), nullable=False)
    post = relationship(Post)

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    author_id = Column(Integer, ForeignKey('user.id'))
    comment_text = Column(Text, nullable=False)
    post = relationship(Post)
    user = relationship(User)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

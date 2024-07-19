import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    userID = Column(Integer, primary_key=True)
    Email = Column(String)
    Password = Column(String)
    First_Name = Column(String)
    Last_Name = Column(String)
    Favorites = relationship("favorites", secondary="user_favorites", backref="user")

class Planet(Base):
    __tablename__ = 'Planet'
    PlanetID = Column(Integer, primary_key=True)
    Name = Column(String)
    Description = Column(String)
    Image = Column(String)
    Favorites = relationship("favorites", backref="Planet")

class Character(Base):
    __tablename__ = 'character'
    characterID = Column(Integer, primary_key=True)
    Name = Column(String)
    Description = Column(String)
    Image = Column(String)
    Favorites = relationship("favorites", backref="character")

class UserJedi(Base):
    __tablename__ = 'user_jedi'
    userJediID = Column(Integer, primary_key=True)
    characterID = Column(Integer, ForeignKey('character.characterID'))
    character = relationship("Character", backref="user_jedi")

class UserSith(Base):
    __tablename__ = 'user_sith'
    userSithID = Column(Integer, primary_key=True)
    characterID = Column(Integer, ForeignKey('character.characterID'))
    character = relationship("Character", backref="user_sith")

class Favorites(Base):
    __tablename__ = 'favorites'
    favoritesID = Column(Integer, primary_key=True)
    userID = Column(Integer, ForeignKey('user.userID'))
    PlanetID = Column(Integer, ForeignKey('Planet.PlanetID'))
    FharacterID = Column(Integer, ForeignKey('character.characterID'))
    Users = relationship("user", secondary="user_favorites", backref="favorites")

class Userfavorites(Base):
    __tablename__ = 'user_favorites'
    userID = Column(Integer, ForeignKey('user.userID'), primary_key=True)
    FavoritesID = Column(Integer, ForeignKey('favorites.favoritesID'), primary_key=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

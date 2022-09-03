"""
FastAPI app called 'Bookipedia' that serves information about books and their cuisines. A simple example of a
"many-to-many" relationship *without* extra data.
"""

from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from pydantic import BaseModel
from dataclasses import dataclass

# Make the engine
engine = create_engine("postgresql://postgres:postgres@localhost:5431/foodDB", echo=True, future=True)

# Make the DeclarativeMeta
Base = declarative_base()

# Declare Classes / Tables
# Make the DeclarativeMeta
Base = declarative_base()

# Declare Classes / Tables
recipe_cuisine = Table('recipe_cuisine', Base.metadata,
                       Column('recipe_id', ForeignKey('recipes.id'), primary_key=True),
                       Column('cuisine_id', ForeignKey('cuisines.id'), primary_key=True)
                       )


@dataclass
class Cuisine(Base):
    __tablename__ = 'cuisines'
    id: id = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    recipes = relationship("Recipe", secondary="recipe_cuisine", back_populates='cuisines')


@dataclass
class Recipe(Base):
    __tablename__ = 'recipes'
    id: int = Column(Integer, primary_key=True)
    title: str = Column(String, nullable=False)
    cuisines: Cuisine = relationship("Cuisine", secondary="recipe_cuisine", back_populates='recipes')

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


#
# class RecipeBase(BaseModel):
#     id: int
#     title: str
#
#     class Config:
#         orm_mode = True
#
#
# class CuisineBase(BaseModel):
#     id: int
#     name: str
#
#     class Config:
#         orm_mode = True
#
#
# class RecipeSchema(RecipeBase):
#     cuisines: list[CuisineBase]
#
#
# class CuisineSchema(CuisineBase):
#     cuisines: list[RecipeBase]


# @dataclass
# class Cuisine(Base):
#     __tablename__ = 'cuisines'
#     id: id = Column(Integer, primary_key=True)
#     name: str = Column(String, nullable=False)
#     recipes: Recipe = relationship("Recipe", secondary="recipe_cuisine", back_populates='cuisines')


# Create the tables in the database
Base.metadata.create_all(engine)

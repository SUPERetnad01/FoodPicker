"""
FastAPI app called 'Bookipedia' that serves information about books and their cuisines. A simple example of a
"many-to-many" relationship *without* extra data.
"""

from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from pydantic import BaseModel

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


class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    cuisines = relationship("Cuisine", secondary="recipe_cuisine", back_populates='recipes')


class RecipeBase(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class CuisineBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class RecipeSchema(RecipeBase):
    cuisines: list[CuisineBase]


class CuisineSchema(CuisineBase):
    cuisines: list[RecipeBase]


class Cuisine(Base):
    __tablename__ = 'cuisines'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    recipes = relationship("Recipe", secondary="recipe_cuisine", back_populates='cuisines')


# Create the tables in the database
Base.metadata.create_all(engine)

"""
FastAPI app called 'Bookipedia' that serves information about books and their cuisines. A simple example of a
"many-to-many" relationship *without* extra data.
"""

from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey, Boolean, Float
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

recipe_dishType = Table('recipe_dishType', Base.metadata,
                        Column('recipe_id', ForeignKey('recipes.id'), primary_key=True),
                        Column('dishType_id', ForeignKey('dishTypes.id'), primary_key=True)
                        )

recipe_occasions = Table('recipe_occasions', Base.metadata,
                         Column('recipe_id', ForeignKey('recipes.id'), primary_key=True),
                         Column('occasion_id', ForeignKey('occasions.id'), primary_key=True)
                         )

recipe_diets = Table('recipe_diets', Base.metadata,
                     Column('recipe_id', ForeignKey('recipes.id'), primary_key=True),
                     Column('diet_id', ForeignKey('diets.id'), primary_key=True)
                     )


@dataclass
class Cuisine(Base):
    __tablename__ = 'cuisines'
    id: id = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False,unique=True)
    recipes = relationship("Recipe", secondary="recipe_cuisine", back_populates='cuisines')


@dataclass
class DishType(Base):
    __tablename__ = 'dishTypes'
    id: id = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False, unique=True)
    recipes = relationship("Recipe", secondary="recipe_dishType", back_populates='dishTypes')


@dataclass
class Occasion(Base):
    __tablename__ = 'occasions'
    id: id = Column(Integer, primary_key=True)
    name: str = Column(String, unique=True, nullable=False)
    recipes = relationship("Recipe", secondary="recipe_occasions", back_populates='occasions')


@dataclass
class Diet(Base):
    __tablename__ = 'diets'
    id: id = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False, unique=True)
    recipes = relationship("Recipe", secondary="recipe_diets", back_populates='diets')


@dataclass
class Recipe(Base):
    __tablename__ = 'recipes'
    id: int = Column(Integer, primary_key=True)
    title: str = Column(String, nullable=False)
    vegetarian: bool = Column(Boolean)
    vegan: bool = Column(Boolean)
    glutenFree: bool = Column(Boolean)
    dairyFree: bool = Column(Boolean)
    veryHealthy: bool = Column(Boolean)
    cheap: bool = Column(Boolean)
    veryPopular: bool = Column(Boolean)
    sustainable: bool = Column(Boolean)
    lowFodmap: bool = Column(Boolean)
    weightWatcherSmartPoints: int = Column(Integer)
    gaps: str = Column(String)
    preparationMinutes: int = Column(Integer)
    cookingMinutes: int = Column(Integer)
    aggregateLikes: int = Column(Integer)
    healthScore: int = Column(Integer)
    creditsText: str = Column(String)
    license: str = Column(String)
    sourceName: str = Column(String)
    pricePerServing: float = Column(Float)
    recipeId: int = Column(Integer)
    readyInMinutes: int = Column(Integer)
    servings: int = Column(Integer)
    sourceUrl: str = Column(String)
    image: str = Column(String)
    imageType: str = Column(String)
    summary: str = Column(String)
    spoonacularSourceUrl: str = Column(String)
    diets: Diet = relationship("Diet", secondary="recipe_diets", back_populates='recipes')
    occasions: Occasion = relationship("Occasion", secondary="recipe_occasions", back_populates='recipes')
    dishTypes: DishType = relationship("DishType", secondary="recipe_dishType", back_populates='recipes')
    cuisines: Cuisine = relationship("Cuisine", secondary="recipe_cuisine", back_populates='recipes')

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# Create the tables in the database
Base.metadata.create_all(engine)

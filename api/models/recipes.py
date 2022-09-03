from sqlalchemy import MetaData, create_engine, Column, Boolean, Integer, String, Float, ARRAY, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from dataclasses import dataclass

engine = create_engine("postgresql://postgres:postgres@localhost:5431/foodDB", echo=True, future=True)
Base = declarative_base()

@dataclass
class Recipes(Base):
    __tablename__ = 'recipe'
    # id: int = Column(Integer)
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
    creditsText: int = Column(String)
    license: int = Column(String)
    sourceName: int = Column(String)
    pricePerServing: float = Column(Float)
    recipeId: int = Column(Integer, primary_key=True)
    title: str = Column(String)
    readyInMinutes: int = Column(Integer)
    servings: int = Column(Integer)
    sourceUrl: str = Column(String)
    image: str = Column(String)
    imageType: str = Column(String)
    summary: str = Column(String)
    cuisines: list[str] = Column(ARRAY(String))
    dishTypes: list[str] = Column(ARRAY(String))
    diets: list[str] = Column(ARRAY(String))
    occasions: list[str] = Column(ARRAY(String))
    spoonacularSourceUrl: str = Column(String)

    def __repr__(self):
        return f'Recipe: {self.title}'
    #
    # def as_dict(self):
    #     return {c.name: getattr(self, c.name) for c in self.__table__.columns}


Base.metadata.create_all(engine)

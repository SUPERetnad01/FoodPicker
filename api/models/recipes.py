# from sqlalchemy import MetaData, create_engine, Column, Boolean, Integer, String, Float, ARRAY, Table, ForeignKey
# from sqlalchemy.orm import relationship, declarative_base
#
# engine = create_engine("postgresql://postgres:postgres@localhost:5431/foodDB", echo=True, future=True)
# Base = declarative_base()
#
# recipe_cuisine = Table(
#     "recipe_cuisine",
#     Base.metadata,
#     Column("recipe_id", Integer, ForeignKey('recipes.id'), primary_key=True),
#     Column("cuisine_id", Integer, ForeignKey('cuisines.id'), primary_key=True)
# )
#
#
# class Recipe(Base):
#     __tablename__ = 'recipes'
#     id: int = Column(Integer, primary_key=True)
#     # vegetarian: bool = Column(Boolean)
#     # vegan: bool = Column(Boolean)
#     # glutenFree: bool = Column(Boolean)
#     # dairyFree: bool = Column(Boolean)
#     # veryHealthy: bool = Column(Boolean)
#     # cheap: bool = Column(Boolean)
#     # veryPopular: bool = Column(Boolean)
#     # sustainable: bool = Column(Boolean)
#     # lowFodmap: bool = Column(Boolean)
#     # weightWatcherSmartPoints: int = Column(Integer)
#     # gaps: str = Column(String)
#     # preparationMinutes: int = Column(Integer)
#     # cookingMinutes: int = Column(Integer)
#     # aggregateLikes: int = Column(Integer)
#     # healthScore: int = Column(Integer)
#     # creditsText: int = Column(String)
#     # license: int = Column(String)
#     # sourceName: int = Column(String)
#     # pricePerServing: float = Column(Float)
#     # recipeId: int = Column(Integer)
#     title: str = Column(String)
#     # readyInMinutes: int = Column(Integer)
#     # servings: int = Column(Integer)
#     # sourceUrl: str = Column(String)
#     # image: str = Column(String)
#     # imageType: str = Column(String)
#     # summary: str = Column(String)
#     cuisines = relationship('Cuisine', secondary="recipe_cuisine", back_populates='recipes')
#     # dishTypes: list[str] = Column(ARRAY(String))
#     # diets: list[str] = Column(ARRAY(String))
#     # occasions: list[str] = Column(ARRAY(String))
#     # spoonacularSourceUrl: str = Column(String)
#
#
# class Cuisine(Base):
#     __tablename__ = 'cuisines'
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     recipes = relationship('Recipe', secondary="recipe_cuisine", backref='cuisines')
#
#
# Base.metadata.create_all(engine)

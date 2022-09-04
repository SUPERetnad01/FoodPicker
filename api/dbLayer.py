from sqlalchemy import create_engine, func
from sqlalchemy.sql.expression import select
from sqlalchemy.orm import sessionmaker, joinedload

from models.Recipes import Recipe, Cuisine, DishType, Occasion, Diet
# from models.recipes import Book, Cuisine
from flask import jsonify
import json

engine = create_engine("postgresql://postgres:postgres@localhost:5431/foodDB", echo=True, future=True)
Session = sessionmaker(bind=engine)
session = Session()


def get_five_random_recipes():
    with Session(bind=engine) as session:
        result = session.query(Recipe).options(joinedload(Recipe.cuisines)).order_by(func.random()).limit(5).all()

    return result


#
def get_first_recipe():
    with Session(bind=engine) as session:
        b = session.query(Recipe).options(joinedload(Recipe.cuisines)).where(Recipe.id == 1).one()
        for x in b.cuisines:
            print(x.name)
        return b
        # b_schema = RecipeSchema.from_orm(b)
        # return b_schema


def test_set():
    from sqlalchemy.orm import Session
    with Session(bind=engine) as session:
        book1 = Recipe(title="Dead People Who'd Be Influencers Today")
        book2 = Recipe(title="How To Make Friends In Your 30s")

        author1 = Cuisine(name="Blu Renolds")
        author2 = Cuisine(name="Chip Egan")
        author3 = Cuisine(name="Alyssa Wyatt")

        dishType = DishType(name="main_meal")
        dishType1 = DishType(name="second_meal")

        oc1 = Occasion(name="cristmas")
        oc2 = Occasion(name="birthday")

        d = Diet(name="vegiterian")
        d1 = Diet(name="nocarbs")

        book1.cuisines = [author1, author2]
        book2.cuisines = [author1, author3]
        book1.dishTypes = [dishType, dishType1]
        book2.dishTypes = [dishType, dishType1]
        book1.occasions = [oc1, oc2]
        book2.occasions = [oc1, oc2]
        book1.diets = [d, d1]
        book2.diets = [d, d1]

        session.add_all([book1, book2, author1, author2, author3, dishType, dishType1])
        session.commit()


if __name__ == "__main__":
    # add_value_to_db()
    # values = get_first_recipe()
    test_set()
    get_first_recipe()

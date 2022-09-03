from sqlalchemy import create_engine, func
from sqlalchemy.sql.expression import select
from sqlalchemy.orm import sessionmaker, joinedload

from models.bookstutorial import Recipe, Cuisine
# from models.recipes import Book, Cuisine
from flask import jsonify
import json

engine = create_engine("postgresql://postgres:postgres@localhost:5431/foodDB", echo=True, future=True)
Session = sessionmaker(bind=engine)
session = Session()


# def get_five_random_recipes():
#     result = session.query(Recipe).options(joinedload(Recipe.cuisines)).all()  # .order_by(func.random()).limit(5).all()
#     # stmt = (
#     #     select(Recipe).options(joinedload(Recipe.cuisines, innerjoin=True))
#     # )
#     # result = session.execute(stmt)
#     print(result[0].cuisines)
#     return result
#
#
# def get_first_recipe():
#     r = session.query(Recipe).where(Recipe.id == 1).one()
#     for b in r.cuisines:
#         print(b.cuisine)
#     return r


# def add_value_to_db():
#     r1 = Recipe(title="fried rice")
#     r2 = Recipe(title="baked potatos")
#     c = Cuisine(name="italian")
#     c2 = Cuisine(name="french")
#     r1.cuisines = [c, c2]
#     r2.cuisines = [c, c2]
#     session.add_all([r1, r2, c, c2])
#     session.commit()

def test_set():
    from sqlalchemy.orm import Session
    with Session(bind=engine) as session:
        book1 = Recipe(title="Dead People Who'd Be Influencers Today")
        book2 = Recipe(title="How To Make Friends In Your 30s")

        author1 = Cuisine(name="Blu Renolds")
        author2 = Cuisine(name="Chip Egan")
        author3 = Cuisine(name="Alyssa Wyatt")

        book1.cuisines = [author1, author2]
        book2.cuisines = [author1, author3]

        session.add_all([book1, book2, author1, author2, author3])
        session.commit()


if __name__ == "__main__":
    # add_value_to_db()
    # values = get_first_recipe()
    # test_set()
    with Session(bind=engine) as session:
        b1 = session.query(Recipe).where(Recipe.id == 1).one()
        print(b1.title)

        for a in b1.cuisines:
            print(a.name)

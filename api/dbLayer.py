from sqlalchemy import create_engine
from sqlalchemy.sql.expression import func
from sqlalchemy.orm import sessionmaker
from models.recipes import Recipes
from flask import jsonify
import json

engine = create_engine("postgresql://postgres:postgres@localhost:5431/foodDB", echo=True, future=True)
Session = sessionmaker(bind=engine)
session = Session()


def get_five_random_recipes():
    result = session.query(Recipes).order_by(func.random()).limit(5).all()
    return result


if __name__ == "__main__":
    recipes = get_five_random_recipes()
    for recipe in recipes:
        print(jsonify(recipe))

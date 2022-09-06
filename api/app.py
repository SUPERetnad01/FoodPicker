from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import dbLayer

app = Flask(__name__)

engine = create_engine("postgresql://postgres:postgres@localhost:5431/foodDB", echo=True, future=True)
Session = sessionmaker(bind=engine)


@app.route('/get5recipes')
def hello_geek():
    recipes = dbLayer.get_five_random_recipes()
    return jsonify(recipes)


@app.route('/getFirstRecipe')
def get_one_recipe():
    recipes = dbLayer.get_first_recipe()
    return jsonify(recipes.as_dict())


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

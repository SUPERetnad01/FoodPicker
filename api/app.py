from flask import Flask, jsonify
import dbLayer

app = Flask(__name__)


@app.route('/get5recipes')
def hello_geek():
    recipes = dbLayer.get_five_random_recipes()
    # fix_json_array(recipes, ["cuisines", "diets", "dishTypes", "occasions"])
    return jsonify(recipes)


@app.route('/getOneRecipe')
def get_one_recipe():
    recipes = dbLayer.get_first_recipe()
    return jsonify(recipes.as_dict())


# def fix_json_array(objects, attributes):
#     for obj in objects:
#         for attr in attributes:
#             print(attr)
#             arr = getattr(obj, attr)
#             if isinstance(arr, list) and len(arr) > 1 and arr[0] == '{':
#                 arr = arr[1:-1]
#                 arr = ''.join(arr).split(",")
#                 print(arr)
#                 setattr(obj, attr, arr)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

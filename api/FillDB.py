import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ast import literal_eval
import numpy as np
import pandas as pd
import scipy.sparse as sparse
import pandas as pd

import spoonacular
from api.models.Recipes import Recipe, Occasion, Diet, DishType, Cuisine

engine = create_engine("postgresql://postgres:postgres@localhost:5431/foodDB", echo=True, future=True)
Session = sessionmaker(bind=engine)
session = Session()


def get_recipes_df(offset, amount_of_times, max_ready_time):
    all_dishes = []
    offset_list = [num * offset for num in range(0, amount_of_times)]
    for offset in offset_list:
        dishes = spoonacular.get_random_dishes(type_of_dish="main_course",
                                               max_ready_time=max_ready_time, offset=offset, sort="popular",
                                               amount_per_page=offset)
        # all_dishes.append(dishes)
        all_dishes = all_dishes + dishes
    food_df = pd.DataFrame(all_dishes)
    print(food_df.shape)
    return food_df


def fix_string_to_array(field):
    field = field.replace("{", "[")
    field = field.replace("}", "]")
    return field


def make_functional_array(s):
    f = s.replace('[', '').replace(']', '').replace('"', '').split(",")
    p = []

    for x in f:
        if x == None or x == '':
            continue
        p.append(x)
    return p


def create_dict_for_relationships(df, table):
    all_items = []
    dictionary_for_relations = {}
    for index, value in df.items():
        all_items = all_items + make_functional_array(value)

    uniqueValues = pd.Series(all_items).unique().tolist()

    for item in all_items:
        if table == "cuisines":
            dictionary_for_relations[item] = Cuisine(name=item)
        if table == "diets":
            dictionary_for_relations[item] = Diet(name=item)
        if table == "dishTypes":
            dictionary_for_relations[item] = DishType(name=item)
        if table == "occasions":
            dictionary_for_relations[item] = Occasion(name=item)
    return dictionary_for_relations


if __name__ == "__main__":
    # recipes_df = get_recipes_df(offset=100, amount_of_times=5, max_ready_time=40)
    recipes_df = pd.read_csv('recipe_v2.csv')
    recipes_df = recipes_df.drop(columns=['Unnamed: 0.1', 'Unnamed: 0'])
    ob_dict = {}
    for field in ["cuisines", "diets", "dishTypes", "occasions"]:
        dictionary = create_dict_for_relationships(recipes_df[field], field)
        ob_dict[field] = dictionary

    recipes = []
    for index in range(0, recipes_df.shape[0]):
        item = recipes_df.iloc[index]
        recipe = Recipe(
            title=item.title,
            vegetarian=item.vegetarian,
            vegan=item.vegan,
            glutenFree=item.glutenFree,
            dairyFree=item.dairyFree,
            veryHealthy=item.veryHealthy,
            cheap=item.cheap,
            veryPopular=item.veryPopular,
            sustainable=item.sustainable,
            lowFodmap=item.lowFodmap,
            weightWatcherSmartPoints=int(item.weightWatcherSmartPoints),
            gaps=item.gaps,
            preparationMinutes=int(item.preparationMinutes),
            cookingMinutes=int(item.cookingMinutes),
            aggregateLikes=int(item.aggregateLikes),
            healthScore=int(item.healthScore),
            creditsText=item.creditsText,
            license=item.license,
            sourceName=item.sourceName,
            pricePerServing=float(item.pricePerServing),
            recipeId=int(item.recipeId),
            readyInMinutes=int(item.readyInMinutes),
            servings=int(item.servings),
            sourceUrl=item.sourceUrl,
            image=item.image,
            imageType=item.imageType,
            summary=item.summary,
            spoonacularSourceUrl=item.spoonacularSourceUrl
        )

        recipe.cuisines = [ob_dict["cuisines"][i] for i in make_functional_array(item.cuisines)]
        recipe.diets = [ob_dict["diets"][i] for i in make_functional_array(item.diets)]
        recipe.dishTypes = [ob_dict["dishTypes"][i] for i in make_functional_array(item.dishTypes)]
        recipe.occasions = [ob_dict["occasions"][i] for i in make_functional_array(item.occasions)]
        recipes.append(recipe)

    session.add_all(recipes)
    session.commit()

    # recipes_df.to_sql(
    #     name='recipes',
    #     con=engine,
    #     if_exists='replace',
    #     index=False
    # )

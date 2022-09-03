from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import numpy as np
import pandas as pd
import scipy.sparse as sparse
import pandas as pd

import spoonacular

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


if __name__ == "__main__":
    # recipes_df = get_recipes_df(offset=100, amount_of_times=5, max_ready_time=40)
    recipes_df = pd.read_csv('recipe_v2.csv')
    #
    # for field in ["cuisines", "diets", "dishTypes", "occasions"]:
    #     recipes_df[field] = recipes_df[field].map(lambda field: fix_string_to_array(field))
    #     print(recipes_df.columns)
    #     r = recipes_df[["recipeId", field]]
    #     field_df = pd.DataFrame()
    #     field_df


    recipes_df.to_sql(
        name='recipe',
        con=engine,
        if_exists='replace',
        index=False
    )

import requests


def get_random_dishes(specific_cuisine=None, excluded_cuisine=None, excluded_ingredients=None, diet=None,
                      type_of_dish=None, max_ready_time=None, offset=0, sort=None,amount_per_page=5):
    url = "https://api.spoonacular.com/recipes/complexSearch?apiKey=a89b2bb485304c67b47658e7fb66a8dd"
    headers = {
        'Accept': 'application/json',
        "Content-Type": "application/json",
    }
    params = {
        "instructionsRequired": "true",
        "addRecipeInformation": "true",
        "type": type_of_dish,
        "sort": sort,
        "excludeCuisine": excluded_cuisine,
        "diet": diet,
        "cuisine": specific_cuisine,
        "offset": offset,
        "excludeIngredients": excluded_ingredients,
        "number": amount_per_page,
        "max_ready_time": max_ready_time,
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()["results"]


def get_instructions_for_dish(dish):
    url = f"https://api.spoonacular.com/recipes/{dish['id']}?apiKey=a89b2bb485304c67b47658e7fb66a8dd"
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)

    return None


def get_dish(id):
    url = f"https://api.spoonacular.com/recipes/{id}/information?apiKey=a89b2bb485304c67b47658e7fb66a8dd"
    headers = {'Accept': 'application/json'}

    response = requests.get(url, headers=headers)
    return response

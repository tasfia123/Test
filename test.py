import os
from dotenv import load_dotenv

from requests.models import encode_multipart_formdata
import requests
import random
import webbrowser
import json

load_dotenv()



# SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY") -- FOR SENDGRID
# SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS") -- FOR SENDGRID

def liquor_type():
    liquor = input("Please select a liquor type: ").lower()
    valid_selections = ["whiskey", "whisky", "beer", "port", "vermouth", "everclear", "absinthe", "cider", "brandy", "aperol", "wine", "gin", "vodka", "rum", "tequila"]
    if liquor not in valid_selections:
        print("OOPS! Invalid liquor type. Please try again.")
        exit()
    else:
        print(f"Selected liquor: '{liquor}'")
        print("\n")
        
    
    request_url = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={liquor}"
    response = requests.get(request_url)
    liquor_data = json.loads(response.text)

    drinks = liquor_data["drinks"]

    while True:
        random_drink = random.choice(drinks)
        print("Cocktail choice:",random_drink["strDrink"])

        user_choice = input("Do you want this type of cocktail? If so, type 'yes' If no, hit 'enter': ").lower()
        if  user_choice == "yes":
            break
            
            print("\n")
    
    drink_id = random_drink["idDrink"]

    request_url_id = f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={drink_id}"
    id_response = requests.get(request_url_id)
    id_data = json.loads(id_response.text)
    
    request_url_ingredients = f"https://www.thecocktaildb.com/api/json/v1/1/list.php?i=list"
    ingredients_response = requests.get(request_url_ingredients)
    ingredients_data = json.loads(ingredients_response.text)

    print("\n")
    print("Instructions: ")

    for i in (id_data["drinks"]):
        print(i["strInstructions"], "\n")

        print("Ingredients: ")
        print("Ingredient 1: ", i["strMeasure1"], i["strIngredient1"])
        print("Ingredient 2: ", i["strMeasure2"], i["strIngredient2"])
        print("Ingredient 3: ", i["strMeasure3"], i["strIngredient3"])
        print("Ingredient 4: ", i["strMeasure4"], i["strIngredient4"])
        print("Ingredient 5: ", i["strMeasure5"], i["strIngredient5"])
        print("Ingredient 6: ", i["strMeasure6"], i["strIngredient6"])
        print("Ingredient 7: ", i["strMeasure7"], i["strIngredient7"])
        print("Ingredient 8: ", i["strMeasure8"], i["strIngredient8"])
        print("Ingredient 9: ", i["strMeasure9"], i["strIngredient9"])
        print("Ingredient 10: ", i["strMeasure10"], i["strIngredient10"])
        print("Ingredient 11: ", i["strMeasure11"], i["strIngredient11"])
        print("Ingredient 12: ", i["strMeasure12"], i["strIngredient12"])
        print("Ingredient 13: ", i["strMeasure13"], i["strIngredient13"])
        print("Ingredient 14: ", i["strMeasure14"], i["strIngredient14"])
        print("Ingredient 15: ", i["strMeasure15"], i["strIngredient15"])

# can't get this code to work correctly -- if you have any thoughts let me know
    # for ingredients in ingredients_data["drinks"]:
    #     if i["strIngredient1"] in ingredients["strIngredient1"]:
    #         print(i["strMeasure1"], i["strIngredient1"])
    #     if i["strIngredient2"] in ingredients["strIngredient1"]:
    #         print(i["strMeasure2"], i["strIngredient2"])
    #     if i["strIngredient3"] in ingredients["strIngredient1"]:
    #         print(i["strMeasure3"], i["strIngredient3"])
    #     if i["strIngredient4"] in ingredients["strIngredient1"]:
    #         print(i["strMeasure4"], i["strIngredient4"])
    #     if i["strIngredient5"] in ingredients["strIngredient1"]:
    #         print(i["strMeasure5"], i["strIngredient5"])
    #     if i["strIngredient6"] in ingredients["strIngredient1"]:
    #         print(i["strMeasure6"], i["strIngredient6"])
    #     if i["strIngredient7"] in ingredients["strIngredient1"]:
    #         print(i["strMeasure7"], i["strIngredient7"])
    #     if i["strIngredient8"] in ingredients["strIngredient1"]:
    #         print(i["strMeasure8"], i["strIngredient8"])
    #     if i["strIngredient9"] in ingredients["strIngredient1"]:
    #         print(i["strMeasure9"], i["strIngredient9"])
    #     if i["strIngredient10"] in ingredients["strIngredient1"]:
    #         print(i["strMeasure10"], i["strIngredient10"])
    #     if i["strIngredient11"] in ingredients["strIngredient1"]:
    #         print(i["strMeasure11"], i["strIngredient11"])
    #     else:
    #         print()

        url = i["strDrinkThumb"]
        webbrowser.open(url)


liquor_type()

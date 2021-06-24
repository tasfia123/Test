# # ##Email the choice to user 
import os
from dotenv import load_dotenv

from requests.models import encode_multipart_formdata
import requests
import random
import webbrowser
import json

load_dotenv()


valid_selections = ["whiskey", "whisky", "beer", "port", "vermouth", "everclear", "absinthe", "cider", "brandy", "aperol", "wine", "gin", "vodka", "rum", "tequila"]


liquor = input("Please select a liquor type: ").lower()
    
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

        user_choice = input("Do you want this type of cocktail? If so, type 'yes' If no, type any key: ").lower()
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
    print("LENGTH", id_data["drinks"])
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



        url = i["strDrinkThumb"]
        webbrowser.open(url)




##Email the choice to user 
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY2", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")
print("SendGrid Code",SENDGRID_API_KEY)

client = SendGridAPIClient("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") #> <class 'sendgrid.sendgrid.SendGridAPIClient>
print("CLIENT:", type(client))

subject = "Your Cocktail Recipe is HERE!!"

random = "Tammana"
cocktail_choice = random_drink["strDrink"]
drink = id_data["drinks"][0]
instructions = drink["strInstructions"]
ingrediant_one = drink["strIngredient1"]
measurement_one= drink["strMeasure1"]
#this is where the template is not working 
html_content = f"Hello {random}, you chose a cocktail with {liquor}!!, this is the name of your cocktail {cocktail_choice}!!,\n"
html_content += f"instructions:{instructions}"
html_content += f"These are the ingrediants you need:"
html_content += f"{ingrediant_one}, {measurement_one}"

print("HTML:", html_content)
message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html_content)

try:
    response = client.send(message)

    print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
    print(response.status_code) #> 202 indicates SUCCESS
    print(response.body)
    print(response.headers)

except Exception as err:
   print(type(err))
   print(err) 



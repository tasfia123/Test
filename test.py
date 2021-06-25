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
        url = random_drink["strDrinkThumb"]
        webbrowser.open(url)

        user_choice = input("Do you want this type of cocktail? If so, type 'yes' If no, type any key: ").lower()
        
        if  user_choice == "yes":
            break
            
            print("\n")
    
    drink_id = random_drink["idDrink"]

    request_url_id = f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={drink_id}"
    id_response = requests.get(request_url_id)
    id_data = json.loads(id_response.text)
    

drink = id_data["drinks"][0]

for index in range(1, 15):
    key = "strIngredient"+str(index)
    ingredient = drink[key]
    key = "strMeasure"+str(index)
    measurement = drink[key]
    if (ingredient is not None):
        if measurement is not None:
            print(measurement, ingredient)
        else:
            print(ingredient)


liquor

##Email the choice to user 

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS")

USER_NAME = os.getenv("USER_NAME", default="Cocktail Lover")

def send_email(subject="YOUR COCKTAIL RECIPE IS HERE!", html="<p>Enjoy your drink!</p>", recipient_address=SENDER_EMAIL_ADDRESS):

    client = SendGridAPIClient(SENDGRID_API_KEY)
    print("CLIENT:", type(client))
    print("SUBJECT:", subject)

    message = Mail(from_email=SENDER_EMAIL_ADDRESS, to_emails=recipient_address, subject=subject, html_content=html)

    try:
       response = client.send(message)
       print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
       print(response.status_code) #> 202 indicates SUCCESS
       return response
    except Exception as e:
       print("OOPS", type(e), e.message)
       return None

if __name__ == "__main__":
    
    subject = "YOUR COCKTAIL RECIPE IS HERE!"

    cocktail_choice = random_drink["strDrink"]
    drink = id_data["drinks"][0]
    instructions = drink["strInstructions"]
    ingredient_1 = drink["strIngredient1"]
    measurement_1 = drink["strMeasure1"]
    ingredient_2 = drink["strIngredient2"]
    measurement_2 = drink["strMeasure2"]
    ingredient_3 = drink["strIngredient3"]
    measurement_3 = drink["strMeasure3"]
    ingredient_4 = drink["strIngredient4"]
    measurement_4 = drink["strMeasure4"]
    ingredient_5 = drink["strIngredient5"]
    measurement_5 = drink["strMeasure5"]
    ingredient_6 = drink["strIngredient6"]
    measurement_6 = drink["strMeasure6"]
    ingredient_7 = drink["strIngredient7"]
    measurement_7 = drink["strMeasure7"]
    ingredient_8 = drink["strIngredient8"]
    measurement_8 = drink["strMeasure8"]
    ingredient_9 = drink["strIngredient9"]
    measurement_9 = drink["strMeasure9"]
    ingredient_10 = drink["strIngredient10"]
    measurement_10 = drink["strMeasure10"]
    ingredient_11 = drink["strIngredient11"]
    measurement_11 = drink["strMeasure11"]
    ingredient_12 = drink["strIngredient12"]
    measurement_12 = drink["strMeasure12"]
    ingredient_13 = drink["strIngredient13"]
    measurement_13 = drink["strMeasure13"]
    ingredient_14 = drink["strIngredient14"]
    measurement_14 = drink["strMeasure14"]
    ingredient_15 = drink["strIngredient15"]
    measurement_15 = drink["strMeasure15"]
    image = drink["strDrinkThumb"]

    cocktail_html = f"""
    <h3>Hello, {USER_NAME}!</h3>
    <h4>You chose a cocktail with {liquor}.</h4>
    <h4>The name of your cocktail is {cocktail_choice}!</h4>
    
    <h4>Here are the instructions:</h4>
    <p>{instructions}</p>
    
    <h4>Here are the required ingredients:</h4>
    <ul>
    	<li>{measurement_1} | {ingredient_1}</li>
    	<li>{measurement_2} | {ingredient_2}</li>
    	<li>{measurement_3} | {ingredient_3}</li>
    	<li>{measurement_4} | {ingredient_4}</li>
    	<li>{measurement_5} | {ingredient_5}</li>
    	<li>{measurement_6} | {ingredient_6}</li>
    	<li>{measurement_7} | {ingredient_7}</li>
    	<li>{measurement_8} | {ingredient_8}</li>
    	<li>{measurement_9} | {ingredient_9}</li>
    	<li>{measurement_10} | {ingredient_10}</li>
    	<li>{measurement_11} | {ingredient_11}</li>
    	<li>{measurement_12} | {ingredient_12}</li>
    	<li>{measurement_13} | {ingredient_13}</li>
    	<li>{measurement_14} | {ingredient_14}</li>
    	<li>{measurement_15} | {ingredient_15}</li>
    </ul>
    <img src="{image}">
    """

    send_email(subject, cocktail_html)
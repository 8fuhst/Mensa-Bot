from datetime import datetime, timedelta
import sys

from Api_requests import *
from telegram_bot import *
import glob

good_stuff = ['Burger', 'Nuggets', 'Schnitzel', 'schnitzel']

# when sending 
DEBUG = False
def check_for_saved_meals():
    print(glob.glob("/Users/tomherrmann/Documents/GitHub/Mensa-Bot/meals"))

def create_meal(meal, cantine, price):
    meal = {
        'dish': meal,
        'canteen': cantine,
        'price': price
    }
    return meal



def check_for_good_stuff(BOT_TOKEN, CHAT_ID):
    # vegan = ""
    # vegetarian = ""
    # fav = ""
    # response2 = get_speiseplan_tomorrow()
    # if response2:
    #     Header = "Der **morgige** Speiseplan " + (datetime.now() + timedelta(1)).strftime("%d.%m.%Y") + " ist: \n"
    #     if DEBUG:
    #         print(Header)
    #     else:
    #         telegram_bot_sendtext(Header, BOT_TOKEN, CHAT_ID)
    #     for meal in response2:
    #         if [ele for ele in good_stuff if (ele in meal['dish'])]:
    #             fav = "⭐️"
    #         if meal['vegan'] == True:
    #             vegan = '🥦 '
    #         if meal['vegetarian'] == True:
    #             vegetarian = "🌿"
    #         meal_text = '- ' + fav + vegan + vegetarian + meal['dish'] + ' ' + (meal['price']) + "€ \n\n"
    #         vegan = ""
    #         vegetarian = ""
    #         fav = ""
    #         if DEBUG:
    #             print(meal_text)
    #         else:
    #             telegram_bot_sendtext(meal_text, BOT_TOKEN, CHAT_ID)
    response = get_speiseplan_today()
    vegan = ""
    vegetarian = ""
    fav = ""
    if response:
        Header = "Der **heutige** Speiseplan " + datetime.today().strftime("%d.%m.%Y") + " ist: \n"
        if DEBUG:
            print(Header)
        else:
            telegram_bot_sendtext(Header, BOT_TOKEN, CHAT_ID)
        for meal in response:
            if [ele for ele in good_stuff if (ele in meal['dish'])]:
                fav = "⭐ "
            if meal['vegan'] == True:
                vegan = '🥦 '
            if meal['vegetarian'] == True:
                vegetarian = '🌿 '
            meal_text = '- ' + fav + vegan + vegetarian + meal['dish'] + ' ' + (meal['price']) + "€ \n\n"
            vegan = ""
            vegetarian = ""
            fav = ""
            if DEBUG:
                print(meal_text)
            else:
                telegram_bot_sendtext(meal_text, BOT_TOKEN, CHAT_ID)



def get_feedback():
    response  = requests.get("https://mensa.mafiasi.de/api/feedback/meal")

def send_feedback(meal, feedback):
    pass


if __name__ == '__main__':
    if DEBUG == True:
        try:
            check_for_good_stuff(1, 1)
        except UnboundLocalError:
            print("Error: Please provide a valid token and chat id")
    else:
        try:
            check_for_good_stuff(sys.argv[1],sys.argv[2])
        except UnboundLocalError:
            print("Error: Please provide a valid token and chat id")




    # for meal in response:
    #     if [ele for ele in good_stuff if (ele in meal['dish'])]:
    #         if DEBUG == True:
    #             print("DEBUG: tomorrow" + meal['dish'])
    #         else:
    #             if meal['canteen'] == 10:
    #                  canteen = "Ikum"
    #             telegram_bot_sendtext("Morgen gibt es " + meal['dish'] + (meal['price']) + "€ in der Mensa" + canteen, BOT_TOKEN, CHAT_ID)

import requests
import json

###########
# Functions
###########
# Return karrestaurang menu
def restaurant_menu():
    url = "http://carboncloudrestaurantapi.azurewebsites.net/api/menuscreen/getdataday?restaurantid=5"
    try:
        r = requests.get(url)
        menu = r.json()
    except ValueError:
        print "Error requesting API"
        exit(0)

    print "Chalmers Restaurant menu: "
    for category in menu["recipeCategories"]:
        print category["name"] + ": " + category["recipes"][0]["displayNames"][0]["displayName"]

##############
# Main program
##############
print ""
restaurant_menu()
print ""

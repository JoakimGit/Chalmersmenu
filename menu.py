import requests
import json
import sys

###########
# Functions
###########
# Return karrestaurang menu
def restaurant_menu():
    # Get todays menu from API
    url = "http://carboncloudrestaurantapi.azurewebsites.net/api/menuscreen/getdataday?restaurantid=5"
    try:
        r = requests.get(url)
        menu = r.json()
    except ValueError:
        print "Error requesting API"
        return -1
    # Check if there's any food served today
    if menu["recipeCategories"] is None:
        print "It's closed today :("
        return -1
    # Print todays menu
    print "Chalmers Restaurant menu: "
    for category in menu["recipeCategories"]:
        print category["name"] + ": " + category["recipes"][0]["displayNames"][0]["displayName"]

# Returns this weeks menu from karrestaurangen.
# Day is numbered from (1->5 for monday->friday)
# If menu for whole week is desired, argument is 0.
def week_menu(day):
    
    # Get weekly menu from API
    url = "http://carboncloudrestaurantapi.azurewebsites.net/api/menuscreen/getdataweek?restaurantid=5"
    try:
        r = requests.get(url)
        menu = r.json()
    except ValueError:
        print "Error requesting API"
        exit(0)
    
    # Display current day
    weekdays = ["the week:\n", "Monday:\n", "Tuesday:\n", "Wednesday:\n","Thursday:\n", "Friday:\n"]
    current_day = 1;
    print "Chalmers Restaurant menu for", weekdays[day]

    # Find the menu of the selected day, skip all days that are incorrect
    for day_menu in menu["menus"]:
        current_day += 1
        # If day is specified, only print that day, otherwise print whole week.
        if day is not 0 and current_day-1 is not day:
            continue
        if menu["menus"][0]["recipeCategories"] is None:
            print "It's closed today :("
            exit(0)
        for category in day_menu["recipeCategories"]:
            print category["name"] + ": " + category["recipes"][0]["displayNames"][0]["displayName"]
        print ""
##############
# Main program
##############
print ""
if len(sys.argv) == 1:
    restaurant_menu()
else:
    day = sys.argv[1].lower()
    if day == "monday":
        week_menu(1)
    elif day == "tuesday":
        week_menu(2)
    elif dau == "wednesday":
        week_menu(3)
    elif day == "thursday":
        week_menu(4)
    elif day == "friday":
        week_menu(5)
    else:
        week_menu(0)





























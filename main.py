import os
from requests import request
from dotenv import load_dotenv
from house import House
import json
from listsortedbag import ListSortedBag

load_dotenv('.env')


def get_house(city, state):
    # payload can be modified to accept more specific searches
    user_city = str(city)
    user_state = str(state)
    payload = {
        'location': user_city + ',' + user_state
    }
    # required request parameters to connect to Zillow API
    headers = {
        'X-RapidAPI-Key': os.getenv('API_KEY'),
        'X-RapidAPI-Host': os.getenv('HOST')
    }
    url = "https://zillow56.p.rapidapi.com/search"

    response = request("GET", url, headers=headers, params=payload)
    # write response as a json file
    writefile = open('houses.json', 'w')
    writefile.write(response.text)
    writefile.close()


def load_house_file(city):
    with open('houses.json') as file:
        api_dict = json.load(file)
        try:
            for house in api_dict['results']:
                if house.get('city').lower() == city.lower():
                    house_list.add(
                        House(
                            address=house.get('streetAddress'),
                            price=house.get('price'),
                            city=house.get('city'),
                            state=house.get('state'),
                            zip_code=house.get('zipcode'),
                            living_area=house.get('livingArea'),
                            bedroom=house.get('bedrooms'),
                            bath=house.get('bathrooms')
                        )
                    )
        except KeyError:
            print('Error invalid search or API error.')
        finally:
            file.close()


def print_house_list(list_of_houses):
    for house in list_of_houses:
        house.print_house()


def search_house_list_by_zip(list_of_houses):
    search_zip_code = str(input('Enter a Full or Partial Zip Code to Search: '))
    for house in list_of_houses:
        try:
            if search_zip_code in str(house.zip_code):
                house.print_house()
        except TypeError:
            continue


def search_house_list_by_address(list_of_houses):
    search_address = str(input('Enter a Full or Partial Address to Search: ')).lower()
    for house in list_of_houses:
        try:
            if search_address in str(house.address).lower():
                house.print_house()
        except TypeError:
            continue


def search_house_list_by_price(list_of_houses):
    min_val = float(input('Enter The Minimum Price or Enter "0" for No Minimum Price: '))
    max_val = float(input('Enter The Maximum Price or Enter "0" for No Maximum Price: '))
    for house in list_of_houses:
        try:
            if min_val != 0 and max_val != 0 and (min_val < house.price < max_val):
                house.print_house()
            elif min_val == 0 and max_val != 0 and house.price < max_val:
                house.print_house()
            elif min_val != 0 and max_val == 0 and min_val < house.price:
                house.print_house()
            elif min_val == 0 and max_val == 0:
                house.print_house()
        except TypeError:
            continue


def search_house_list_by_area(list_of_houses):
    min_val = float(input('Enter The Minimum Square Footage or Enter "0" for No Minimum Square Footage: '))
    max_val = float(input('Enter The Maximum Square Footage or Enter "0" for No Maximum Square Footage: '))
    for house in list_of_houses:
        try:
            if min_val != 0 and max_val != 0 and (min_val <= house.living_area <= max_val):
                house.print_house()
            elif min_val == 0 and max_val != 0 and house.living_area <= max_val:
                house.print_house()
            elif min_val != 0 and max_val == 0 and min_val <= house.living_area:
                house.print_house()
            elif min_val == 0 and max_val == 0:
                house.print_house()
        except TypeError:
            continue


def search_house_list_by_num_bedrooms(list_of_houses):
    search_num_bedrooms = int(input('Enter the Number of Bedrooms to Search: '))
    for house in list_of_houses:
        try:
            if search_num_bedrooms == int(house.bedroom):
                house.print_house()
        except TypeError:
            continue


def search_house_list_by_num_bathrooms(list_of_houses):
    search_num_bathrooms = int(input('Enter the Number of Bathrooms to Search: '))
    for house in list_of_houses:
        try:
            if search_num_bathrooms == int(house.bath):
                house.print_house()
        except TypeError:
            continue


def display_averages(list_of_houses):
    total_price = 0
    total_area = 0
    total_bedrooms = 0
    total_bathrooms = 0
    num_of_houses = len(list_of_houses)

    for house in list_of_houses:
        try:
            total_price += house.price
            total_area += house.living_area
            total_bedrooms += house.get_bedroom_count()
            total_bathrooms += house.get_bathroom_count()
        except TypeError:
            continue

    total_price = total_price / num_of_houses
    total_area = total_area / num_of_houses
    total_bedrooms = total_bedrooms / num_of_houses
    total_bathrooms = total_bathrooms / num_of_houses

    print('-------------------------------')
    print(f'{"Avg Price: ":<20}${total_price:,.2f}')
    print(f'{"Avg Square Footage: ":<20}{total_area:,.2f}')
    print(f'{"Avg Bedroom Count: ":<20}{total_bedrooms:,.2f}')
    print(f'{"Avg Bathroom Count: ":<20}{total_bathrooms:,.2f}')
    print('-------------------------------')


def search_city_state():
    user_quit = ""
    while user_quit != "y":
        try:
            city_input = str(input('Enter a city: '))
            state_input = str(input('Enter a state: '))
            if os.path.exists('houses.json'):
                os.remove('houses.json')

            get_house(city_input, state_input)
            load_house_file(city_input)
            break
        except ValueError:
            print("Submit Proper Values.")
            user_quit = input("Quit? y/n")


house_list = ListSortedBag()
search_city_state()

user_action = ""
while user_action != "0":
    print("\n1: Search by New City and State")
    print("2: Search House list by Zip Code")
    print("3: Search House list by Address")
    print("4: Search House list by Price Range")
    print("5: Search House list by Living Area")
    print("6: Search House list by # of Bedrooms")
    print("7: Search House list by # of Bathrooms")
    print("8: Display Averages of House Attributes by City and State")
    print("9: Display Housing listings")
    print("0: Quit Program\n")
    user_action = input("Enter The Number of Your Action: ")

    if user_action == "1":
        house_list = ListSortedBag()
        search_city_state()
    if user_action == "2":
        search_house_list_by_zip(house_list)
    if user_action == "3":
        search_house_list_by_address(house_list)
    if user_action == "4":
        search_house_list_by_price(house_list)
    if user_action == "5":
        search_house_list_by_area(house_list)
    if user_action == "6":
        search_house_list_by_num_bedrooms(house_list)
    if user_action == "7":
        search_house_list_by_num_bathrooms(house_list)
    if user_action == "8":
        display_averages(house_list)
    if user_action == "9":
        print_house_list(house_list)

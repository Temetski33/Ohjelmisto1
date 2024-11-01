# Moduuli 12 teht 2

import requests

api_key = "8b9a077456633eec8e7cd3887a6ac23a"

def get_temp(the_city, city_lat, city_lon):
    lat = city_lat
    lon = city_lon
    lang = "fi"

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&lang={lang}&units=metric"

    response = requests.get(url)
    response_body = response.json()

    print(f"Haun tulos on {the_city}.")
    print(f"Säätila on '{response_body['weather'][0]['description']}' ja lämpötila {response_body['main']['temp']:.1f} C.")


def get_city(wanted_city):
    city_name = wanted_city
    state_code = ""
    country_code = ""
    limit = ""
    city_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={api_key}"

    city_response = requests.get(city_url)
    city_response_body = city_response.json()

    city_stats = []
    city_stats.append(city_response_body[0]['name'])
    city_stats.append(city_response_body[0]['lat'])
    city_stats.append(city_response_body[0]['lon'])
    return city_stats


# Pääohjelma
desired_city = input("Syötä kaupunki: ")
stats_list = get_city(desired_city)

our_city = stats_list[0]
our_city_lat = stats_list[1]
our_city_lon = stats_list[2]

get_temp(our_city, our_city_lat, our_city_lon)
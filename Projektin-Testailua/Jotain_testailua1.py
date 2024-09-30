import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="teemu",
    passwd="salakala",
    database="flight_game",
    autocommit=True,
    collation='utf8mb4_general_ci'
)

def create_player(screen_name):
    cursor = connection.cursor()

    initial_co2_budget = 10000
    initial_co2_consumed = 0
    initial_currency = 10000
    initial_location = "KLAX"

    sql = "INSERT INTO game (co2_consumed, co2_budget, location, screen_name, currency) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql, (initial_co2_consumed, initial_co2_budget, initial_location, screen_name, initial_currency))


def start_game():
    screen_name = input("Syötä nimesi: ")
    create_player(screen_name)

    print(f"Hei {screen_name}! Aloitetaan peli")

    cities = select_random_location()
    show_location(cities)

    chosen_city = select_location(cities)
    print(f"Valitsit kaupungin: {chosen_city['municipality']}")


def select_random_location():

    cursor = connection.cursor(dictionary=True)
    sql = "SELECT municipality, iso_country FROM airport ORDER BY RAND() LIMIT 15"
    cursor.execute(sql)
    result = cursor.fetchall()

    return result

def show_location(cities):

    print("\nValitse seuraava keikkakaupunki:")

    index = 1
    for city in cities:
        print(f"{index}. {city['municipality']}, {city['iso_country']}")
        index += 1


def select_location(cities):

    choice = int(input("Valitse kaupunki (1-15): ")) - 1
    chosen_location = cities[choice]
    return chosen_location

""""
def calculate_distance():
    cursor = connection.cursor()
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor.execute(sql, ("KLAX",))

    starting_city = cursor.fetchone()
    next_city = cursor.fetchone()

    starting_city_coordinates = starting_city[0], starting_city[1]
    next_city_coordinates = next_city[0], next_city[1]

"""


start_game()
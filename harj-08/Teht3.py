#select name, latitude_deg, longitude_deg from airport where ident

from geopy import distance
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='teemu',
         password='salakala',
         autocommit=True,
        collation='utf8mb4_general_ci'
         )

def fetch_airport_by_icao(code):
    sql = f"select name, municipality, latitude_deg, longitude_deg from airport where ident='{code}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    #print(result_row)
    return result_row

user_input = input(f"Anna ICAO koodi: ")
user_input = user_input.upper()
result = fetch_airport_by_icao(user_input)
if result:
    print(f"Asema 1: {result[0]}")
    asema1_cord1 = float(result[2])
    asema1_cord2 = float(result[3])
else:
    print(f"Hakemallasi koodilla ei löydy asemaa.")

user_input2 = input(f"Anna ICAO koodi: ")
user_input2 = user_input2.upper()
result2 = fetch_airport_by_icao(user_input2)
if result2:
    print(f"Asema 2: {result2[0]}")
    asema2_cord1 = float(result2[2])
    asema2_cord2 = float(result2[3])
else:
    print(f"Hakemallasi koodilla ei löydy asemaa.")


if result and result2:
    asema1_cords = (asema1_cord1, asema1_cord2)
    asema2_cords = (asema2_cord1, asema2_cord2)
    result_distance = distance.distance(asema1_cords, asema2_cords)
    print(f"Lentoasemoiden välinen etäisyys on {result_distance}.")
else:
    print("Ei voida laskea etäisyyttä.")

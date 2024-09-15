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
    sql = f"select type from airport where iso_country='{code}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchall()
    #print(*result_row, sep = "\n")
    return result_row

user_input = input(f"Anna maakoodi: ")
user_input = user_input.upper()
result = fetch_airport_by_icao(user_input)

if result:
    print(f"Haku onnistui.")

    small = result.count(('small_airport',))
    print(f"Pieniä lentokenttiä: {small}")

    medium = result.count(('medium_airport',))
    print(f"Keskikokoisia lentokenttiä: {medium}")

    large = result.count(('large_airport',))
    print(f"Suuria lentokenttiä: {large}")

    heli = result.count(('heliport',))
    print(f"Helikopterikenttiä: {heli}")

    closed = result.count(('closed',))
    print(f"Suljettuja lentokenttiä: {closed}")

else:
    print(f"Hakemallasi koodilla ei löydy asemaa.")


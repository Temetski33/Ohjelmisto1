#Tähä tulee teht2 joskus
#iso-country type (NÄITÄ ON USEITA: large medium small closed heliport AINAKIN)

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
    sql = f"select name, type from airport where iso_country='{code}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchall()
    print(*result_row, sep = "\n")
    return result_row

user_input = input(f"Anna maakoodi: ")
user_input = user_input.upper()
result = fetch_airport_by_icao(user_input)
if result:
    print(f"Haettu lentoasema: {result[0]}, {result[1]}")
else:
    print(f"Hakemallasi koodilla ei löydy asemaa.")
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
    sql = f"select name, municipality from airport where ident='{code}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    #print(result_row)
    return result_row

user_input = input(f"Anna ICAO koodi: ")
user_input = user_input.upper()
result = fetch_airport_by_icao(user_input)
if result:
    print(f"Haettu lentoasema: {result[0]}, {result[1]}")
else:
    print(f"Hakemallasi koodilla ei löydy asemaa.")
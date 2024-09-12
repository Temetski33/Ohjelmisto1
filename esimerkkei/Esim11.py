#Hikoiluversio moduulin 7 tehtävästä 3.
#Tein vähän ylimäärästä duunia ja tää oli vähän eri mitä kysyttiin.

import mysql.connector

#funktioversio hausta
"""def get_db_connection():
    return mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='teemu',
         password='salakala',
         autocommit=True,
        collation='utf8mb4_general_ci'
         )"""

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='teemu',
         password='salakala',
         autocommit=True,
        collation='utf8mb4_general_ci'
         )

def tehtyvalinta():
    valinta = int(input(f"Syötä uusi lentoasema kirjoita 1, hae aseman tiedot kirjoita 2, lopeta kirjoita 3: "))
    if valinta == 0 or valinta >= 4:
        print("Syötevirhe")
    elif 0 < valinta < 4:
        return valinta


def add_country(code, name):
    sql = f"INSERT INTO country VALUES  ('{code}', '{name}', null, null, null)"
    cursor = connection.cursor()
    cursor.execute(sql)

def valintafunc():
    tulos = tehtyvalinta()

    if tulos == 1:
        print(f"Syötetään uusi lentoasema.")
        country_name = input("Anna lisättävän maan nimi: ")
        country_code = input("Anna lisättävän maan koodi: ")
        add_country(country_code, country_name)
    elif tulos == 2:
        print(f"Haetaan aseman tiedot.")
        cursor = connection.cursor()
        haettukoodi = input(f"Syötä haettavan seman ICAO koodi: ")
        sql2 = "SELECT name, iso_country FROM country"
        cursor.execute(sql2)
        result = cursor.fetchall()
        haettumaa = next((i for i, elem in enumerate(result) if elem[1] == haettukoodi), -1)
        print(f"Koodiasi vastaava lentoasema on {result[haettumaa][0]}.")
    elif tulos == 3:
        print(f"Lopetetaan ohjelma.")
    return tulos

toistokerroin = 1
while 0 < toistokerroin < 3:
    toistokerroin = valintafunc()
import mysql.connector

# "tallennetaan" connect-funktion palauttama yhteys muuttujaan
# jatkokäyttöä varten
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='teemu',
         password='salakala',
         autocommit=True,
        # tarvitaan uudelle 9.0 versiolle ajurista:
        collation='utf8mb4_general_ci'
         )
#print(connection)

def print_countries():
    cursor = connection.cursor()
    sql = "SELECT name, iso_country FROM country"
    sql2 = "SELECT name, iso_country FROM country WHERE name='ää'"
    cursor.execute(sql)
    # haetaan vain ensimmäinen (tai seuraava rivi osoittimen kohdalta"
    #result = cursor.fetchone()
    #print(result)
    # fetchmany palauttaa n seuraavaa osoittimen kohdalta
    #result = cursor.fetchmany(3)
    #print(result)
    # fetchall palauttaa kaikki(loput)
    result = cursor.fetchall()
    #tulosrivien lukumäärä
    print(cursor.rowcount)
    print(result)
    #tulostetaan toisen rivin maakoodi
    #print(result[1][1])
    # käsitellään koko tulosjoukko (lista) toistorakenteella
    if cursor.rowcount == 0:
        print("ei yhtään maata")
    else:
        for row in result:
            print(f"Maan {row[0]} maakoodi on {row[1]}.")
        print(f"Maita yhteensä: {cursor.rowcount}")

print_countries()

def add_country(code, name):
    sql = f"INSERT INTO country VALUES  ('{code}', '{name}', null, null, null)"
    cursor = connection.cursor()
    cursor.execute(sql)

country_name = input("Anna lisättävän maan nimi: ")
country_code = input("Anna lisättävän maan koodi: ")
add_country(country_code, country_name)

# nyt meni vähä ylimäärästä tietokantaan emt emt
#Moduulin 8 tuntiesimerkkejä. Teht3

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

asema1_cords = (64, 40)
asema2_cords = (60, 42)
result_distance = distance.distance(asema1_cords, asema2_cords)
print(result_distance)
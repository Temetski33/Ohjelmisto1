#Moduuli 13 teht 2

from flask import Flask
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='teemu',
         password='salakala',
         autocommit=True,
        collation='utf8mb4_general_ci'
         )

@app.route('/kenttä/<code>')
def fetch_airport_by_icao(code):
    sql = f"select name, municipality from airport where ident='{code}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    result_list = {
        "ICAO": code,
        "Name": result_row[0],
        "Municipality": result_row[1]
    }
    return result_list

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
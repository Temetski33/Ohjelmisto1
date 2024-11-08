#Mod 13 teht 1 tuntiesim juttuja

import json
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/jotain')
def printtaa_joku_juttu():
    return 'Tos ois toinen kolmas juttu!'

@app.route('/sum')
def calculate_sum():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
    except ValueError:
        return 'Virheellinen syöte, käytä numeroita!'
    except TypeError:
        return 'Parametri puuttuu! Haloo!'
    return {
        "funktio": "Laske kahden arvon summa",
        "tulos": num1 + num2
    }


# "mock data" ns. testidataa
nimet = ['Aku', 'Iines', 'Hannu', 'Heluna']

@app.route('/names')
def get_names():
    return nimet

@app.route('/name/<id>')
def get_name(id):
    try:
        result = {"id": id, "nimi": nimet[int(id)]}
    except IndexError:
        # status-koodin vaihtaminen vaatii oman response-olion luonnin
        res_body = {"error": "Not found! Haloo!"}
        # muutetaan sanakirja -> json-muotoinen merkkijono
        res_body = json.dumps(res_body)
        response = Response(status=404, response=res_body,
                            content_type="application/json")
        return response
    return result

# yleinen virheenkäsittely 404-virheille
@app.errorhandler(404)
def not_found(error_message):
    #print(error_message)
    print(request.path)
    res_body = {"route": request.path, "error": "error"}
    # muutetaan sanakirja -> json-muotoinen merkkijono
    res_body = json.dumps(res_body)
    response = Response(status=404, response=res_body,
                        content_type="application/json")
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, port=3000)

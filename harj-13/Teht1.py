#Moduuli 13 teht 1

from flask import Flask


app = Flask(__name__)

@app.route('/alkuluku/<int:luku>')
def onko_alkuluku(luku):
    on_alku = True

    #testataan vain puolet koska sekin riittää
    testauksen_loppu = luku / 2 + 1
    testauksen_loppu = round(testauksen_loppu)

    if luku < 2:
        on_alku = False

    for jakaja in range(2, testauksen_loppu):
        if luku % jakaja == 0:
            on_alku = False
            break

    # tulostetaan saadut vastaukset web-sivulle
    vastaus = {
        "Number": luku,
        "isPrime": on_alku
    }

    # palautetaan vastaus web-sivulle
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

import json
from flask import Flask,Response
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='12345',
    autocommit=True
)

def search_icao(icao):
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    if result:
        name, municipality = result
        return name, municipality
    else:
        return None, None

@app.route("/airport/<icao>")
def get_airport(icao):
    name , location = search_icao(icao)
    response = {
        "Icao": icao,
        "Name": name,
        "Location": location
    }
    return Response(json.dumps(response), mimetype='application/json')

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
from flask import Flask, Response
import json

app = Flask(__name__)

def is_prime(number):
    count = 0
    if number < 2:
        return False
    for i in range (2, number + 1):
        if number % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False

@app.route("/prime_number/<int:number>")
def prime_number(number):
    response = {
        "Number": number,
        "IsPrime": is_prime(number)
    }

    return Response(json.dumps(response), mimetype='application/json')

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
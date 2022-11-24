import requests
from flask import Flask
# https://www.youtube.com/watch?v=n4ANDISaJ38
# https://www.youtube.com/watch?v=sk7vQADh5X0

app = Flask(__name__)

@app.route("/")
def main():
    return "Hola mundo"

"""
eth 3453.39   0.10949235      31,510.10
mana 1500.00   93.04156172      16.12
"""

@app.route("/monedas")
def precioXCripto(price_mxn=3453.39):
    response = requests.get('https://api.bitso.com/v3/order_book/?book=eth_mxn')   # https://api.bitso.com/v3/available_books/
    json_response = response.json()
    price_mxn = price_mxn
    value = 0

    for i in range(50):
        price = float(json_response['payload']['asks'][i]['price'])   # asks
        amount = float(json_response['payload']['asks'][i]['amount'])   # bids
        value += price * amount
        print(f"el valor es {value}, {i}")
        if value > price_mxn:
            price_eth = price
            value_eth = (price_mxn / price_eth) * 1.04
            print(f"El precio ether {price_eth}")
            print(f"El valor de {price_mxn} MAX en ether {value_eth}")
            # break
    return f"El valor de ether es: {value_eth}"

# hacer la llamada a la función

if __name__ == '__main__':
    app.run(debug=True, port=8080)
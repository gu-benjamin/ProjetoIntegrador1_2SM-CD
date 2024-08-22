from flask import Flask
from bd import Carros

app = Flask('carros')

@app.route('/carros', methods=['GET'])
def get_carros():
    return Carros
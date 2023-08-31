# Este es un Back End
from flask import Flask, render_template, jsonify, request
import numpy as np
from joblib import load  # Para cargar el modelo
import os

# Cargar el modelo
dt = load('dt1.joblib')

# Servidor (back-end)
# Levantar un Back-End = generar el servidor
# Va a escuchar las peticiones
servidorWeb = Flask(__name__)

# anotaciones, hacemos una ruta


@servidorWeb.route("/holamundo", methods=['GET'])
def holamundo():
    return render_template('pagina1.html')


# Envío de datos a través de JSON
@servidorWeb.route('/modelo', methods=['POST'])
def modeloPrediccion():
    contenido = request.json()
    print(contenido)
    return jsonify({'resultado': "Hola"})


if __name__ == '__main__':
    servidorWeb.run(debug=False, host='0.0.0.0', port='8080')

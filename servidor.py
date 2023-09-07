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
    contenido = request.json
    print(contenido)
    datosEntrada = np.array([
        # Estos valores son fijos de las otras variables
        0.88, 0, 2.6, 0.098, 25, 67, 0.9968, 1, 0.4,
        contenido['pH'],
        contenido['sulphates'],
        contenido['alcohol']
    ])
    # Utilizar el modelo para predecir
    # El predictos sirve para predecir un dato, por eso el reshape
    resultado = dt.predict(datosEntrada.reshape(1, -1))
    # El modelo nos va a dar la salida del clasificador
    return jsonify({'resultado': str(resultado[0])})


if __name__ == '__main__':
    servidorWeb.run(debug=False,host='0.0.0.0',port='8080')

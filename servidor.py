from flask import Flask, render_template

# Levantar un Back-End = generar el servidor
# Va a escuchar las peticiones
servidorWeb = Flask(__name__)

# anotaciones, hacemos una ruta
@servidorWeb.route("/holamundo", methods=['GET'])
def holamundo():
	return render_template('pagina1.html')

if __name__ == '__main__':
	servidorWeb.run(debug=False, host='0.0.0.0', port='8080')

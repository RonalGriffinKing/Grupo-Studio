from flask import Flask, jsonify, request, render_template
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos
db_config = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'database': 'apple'
}

# Ruta para servir la página HTML
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para obtener datos de la base de datos
@app.route('/data', methods=['GET'])
def get_data():
    try:
        # Conectar a la base de datos
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        # Ejecutar la consulta
        cursor.execute("SELECT * FROM iphones")
        rows = cursor.fetchall()
        
        # Cerrar la conexión
        cursor.close()
        conn.close()
        
        # Devolver los datos en formato JSON
        return jsonify(rows)
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)})

if __name__ == '__main__':
    app.run(debug=True)

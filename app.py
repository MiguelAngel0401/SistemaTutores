from flask import Flask, render_template, request
from models.db import get_connection

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        carrera = request.form['carrera']
        grupo = request.form['grupo']
        tutor = request.form['tutor']
        actividad = request.form['documentos']
        asistencia = request.form['asistencia']
        
        # Obtén el valor de seguimiento ('h' o 'm')
        seguimiento = request.form.get('hm', '')

        # Valida que 'seguimiento' tenga un valor válido
        if seguimiento not in ['h', 'm']:
            # Establece un valor predeterminado en caso de que no haya sido seleccionado
            seguimiento = ''

        fecha = request.form['fecha']
        causa_baja = request.form['causa_baja']
        canalizacion = request.form['canalizacion']

        connection = get_connection()
        cursor = connection.cursor()

        query = "INSERT INTO entregables (Carrera, Grupo, Tutor, Actividad, Asistencia, SegInividual, SegAcc, SegAccFech, Baja, Canalizacion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (carrera, grupo, tutor, actividad, asistencia, seguimiento, '', fecha, causa_baja, canalizacion)

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

        return "Los datos han sido insertados correctamente en la base de datos."

if __name__ == '__main__':
    app.run(debug=True)

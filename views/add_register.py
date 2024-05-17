from flask import request
from models.db import get_connection

def submitForm():
    if request.method == 'POST':
        carrera = request.form['carrera']
        grupo = request.form['grupo']
        tutor = request.form['tutor']
        actividad = request.form['documentos']
        actividad2 = request.form['documentos2']
        actividad3 = request.form['documentos3']
        actividad4 = request.form['documentos4']
        asistencia = request.form['asistencia']
        asistencia2 = request.form['asistencia2']
        asistencia3 = request.form['asistencia3']
        asistencia4 = request.form['asistencia4']
        nombres = request.form['nombres']
        seguimiento = request.form['seguimiento']


        if carrera == 'tsu0':
            carrera = 'TIADSM'
        elif carrera == 'tsu1':
            carrera = 'TIAIRD'
        elif carrera == 'tsu2':
            carrera = 'TIAEVND'
        elif carrera == 'tsu3':
            carrera = 'IDGS'
        elif carrera == 'tsu4':
            carrera = 'IRIC'
        elif carrera == 'tsu5':
            carrera = 'IEVND'

        if grupo == 'grupo0':
            grupo = '1A'
        elif grupo == 'grupo1':
            grupo = '1B'
        elif grupo == 'grupo2':
            grupo = '2A'
        elif grupo == 'grupo3':
            grupo = '2B'
        elif grupo == 'grupo4':
            grupo = '3A'
        elif grupo == 'grupo5':
            grupo = '3B'
        elif grupo == 'grupo6':
            grupo = '4A'
        elif grupo == 'grupo7':
            grupo = '4B'
        elif grupo == 'grupo8':
            grupo = '5A'
        elif grupo == 'grupo9':
            grupo = '5B'
        elif grupo == 'grupo10':
            grupo = '6A'
        elif grupo == 'grupo11':
            grupo = '6B'
        elif grupo == 'grupo12':
            grupo = '7A'
        elif grupo == 'grupo13':
            grupo = '7B'
        elif grupo == 'grupo14':
            grupo = '8A'
        elif grupo == 'grupo15':
            grupo = '8B'
        elif grupo == 'grupo16':
            grupo = '9A'
        elif grupo == 'grupo17':
            grupo = '9B'
        elif grupo == 'grupo18':
            grupo = '10A'
        elif grupo == 'grupo19':
            grupo = '10B'

        if tutor == 'Profe0':
            tutor = 'Jose Manuel Flores Juarez'
        elif tutor == 'Profe1':
            tutor = 'Diana Lizeth Ahuatzi Reyes'
        elif tutor == 'Profe2':
            tutor = 'Alfredo Garcia Ruiz'
        elif tutor == 'Profe3':
            tutor = 'Elizabeth Cortes Ramos'
        elif tutor == 'Profe4':
            tutor = 'Maricela Gress Roldan'
        elif tutor == 'Profe5':
            tutor = 'Jose Marin Rugerio Atriano'
        elif tutor == 'Profe6':
            tutor = 'Sonia Lopez Rodriguez'
        elif tutor == 'Profe7':
            tutor = 'Margarita Lima Esteban'
        elif tutor == 'Profe8':
            tutor = 'Juan Gabriel Valencia Muñoz'
        elif tutor == 'Profe9':
            tutor = 'Miguel Torreon Hernandez'
        elif tutor == 'Profe10':
            tutor = 'Francisco Lopez Briones'
        elif tutor == 'Profe11':
            tutor = 'Aldo Giovani Luria Garcia'

        fecha = request.form['fecha']
        causa_baja = request.form['causa_baja']
        canalizacion = request.form['canalizacion']

        connection = get_connection()
        cursor = connection.cursor()

        query = """INSERT INTO entregables (Carrera, Grupo, Tutor, Actividad, Actividad2, Actividad3, Actividad4,
                Asistencia, Asistencia2, Asistencia3, Asistencia4, SegInividual, SegAcc, SegAccFech, Baja,
                Canalizacion)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (carrera, grupo, tutor, actividad, actividad2, actividad3, actividad4, asistencia, asistencia2,
                asistencia3, asistencia4, nombres, seguimiento, fecha, causa_baja,
                canalizacion)

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

        return "Los datos han sido insertados correctamente en la base de datos."

def get_form():
    conector = get_connection()
    cursor = conector.cursor()
    consult = "SELECT * FROM entregables "
    cursor.execute(consult)
    data_tuplas = cursor.fetchall()
    cursor.close()
    conector.close()
    data = []
    for data_tuple in data_tuplas:
        if len(data_tuple) >= 17:
            seg_acc_status = 'Entregado' if data_tuple[13] == 1 else 'No Entregado'
            data.append({
                'No': data_tuple[0],
                'Carrera': data_tuple[1],
                'Grupo': data_tuple[2],
                'Tutor': data_tuple[3],
                'Actividad': data_tuple[4],
                'Actividad2': data_tuple[5],
                'Actividad3': data_tuple[6],
                'Actividad4': data_tuple[7],
                'Asistencia': data_tuple[8],
                'Asistencia2': data_tuple[9],
                'Asistencia3': data_tuple[10],
                'Asistencia4': data_tuple[11],
                'SegInividual': data_tuple[12],
                'SegAcc': seg_acc_status,
                'SegAccFech': data_tuple[14],
                'Baja': data_tuple[15],
                'Canalizacion': data_tuple[16],
            })

    return data

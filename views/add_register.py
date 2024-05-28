from flask import request, redirect, url_for
from models.db import get_connection

def insert_tutor(tutor_name):
    connection = get_connection()
    cursor = connection.cursor()
    query = "INSERT INTO tutor (nombre) VALUES (%s)"
    cursor.execute(query, (tutor_name,))
    connection.commit()
    
    cursor.execute("SELECT LAST_INSERT_ID()")
    tutor_id = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return tutor_id

def insert_actividad(actividad, asistencia, grupo, id_tutor):
    connection = get_connection()
    cursor = connection.cursor()
    query = "INSERT INTO actividades (Actividad, Asistencia, Grupo, id_tutor) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (actividad, asistencia, grupo, id_tutor))
    connection.commit()
    
    cursor.execute("SELECT LAST_INSERT_ID()")
    actividad_id = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return actividad_id

def insert_alumno(nombre, baja, canalizacion, materia, tutor_id):
    connection = get_connection()
    cursor = connection.cursor()
    query = "INSERT INTO alumnos (nombre, encuesta_baja, canalizacion, mat_acredi_extr, id_tutor) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nombre, baja, canalizacion, materia, tutor_id))
    connection.commit()
    cursor.close()
    connection.close()

def submitForm():
    if request.method == 'POST':
        tutor = request.form.get('tutor')
        tutor_id = insert_tutor(tutor)
        print(f"Generated tutor_id: {tutor_id}")

        actividades = request.form.getlist('documentos[]')
        asistencias = request.form.getlist('asistencia[]')
        grupo = request.form.get('grupo')

        for actividad, asistencia in zip(actividades, asistencias):
            actividad_id = insert_actividad(actividad, asistencia, grupo, tutor_id)
            print(f"Inserted actividad_id: {actividad_id}")

            carrera = request.form.get('carrera')
            seguimiento = request.form.get('seguimiento')

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

                



            connection = get_connection()
            cursor = connection.cursor()
            query = """INSERT INTO entregables (Carrera, Grupo, idActividad, idAlumno, id_tutor, Seguimiento)
                        VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (carrera, grupo, actividad_id, None, tutor_id, seguimiento))
            connection.commit()
            cursor.close()
            connection.close()

        nombres = request.form.getlist('nombres[]')
        bajas = request.form.getlist('baja[]')
        canalizaciones = request.form.getlist('canalizacion[]')
        materias = request.form.getlist('materias[]')

        for nombre, baja, canalizacion, materia in zip(nombres, bajas, canalizaciones, materias):
            insert_alumno(nombre, baja, canalizacion, materia, tutor_id)

        return redirect(url_for('table'))

def get_form():
    connection = get_connection()
    cursor = connection.cursor()
    query = """SELECT entregables.No, entregables.Carrera, entregables.Grupo, actividades.Actividad, 
                    alumnos.nombre AS Alumno, tutor.nombre AS Tutor, entregables.Seguimiento
               FROM entregables
               LEFT JOIN actividades ON entregables.idActividad = actividades.id
               LEFT JOIN alumnos ON entregables.idAlumno = alumnos.id
               LEFT JOIN tutor ON entregables.id_tutor = tutor.id"""
    cursor.execute(query)
    data_tuples = cursor.fetchall()
    cursor.close()
    connection.close()

    data = []
    for row in data_tuples:
        tutor_id = row[5]
        tutor_nombre = ''
        
        data.append({
            'No': row[0],
            'Carrera': row[1],
            'Grupo': row[2],
            'Actividad': row[3],
            'Alumno': row[4],
            'Tutor': tutor_nombre,
            'Seguimiento': row[6],
        })
    return data


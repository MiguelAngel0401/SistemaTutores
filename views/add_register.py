from flask import request
from models.db import get_connection

from flask import request, redirect, url_for
from models.db import get_connection
import datetime

def insert_tutor(tutor_name):
    connection = get_connection()
    cursor = connection.cursor()
    query = "INSERT INTO tutor (nombre) VALUES (%s)"
    cursor.execute(query, (tutor_name,))
    connection.commit()
    cursor.close()
    connection.close()

    connection = get_connection()
    cursor = connection.cursor()
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
    cursor.close()
    connection.close()

    cursor.execute("SELECT LAST_INSERT_ID()")
    actividad_id = cursor.fetchone()[0]
    connection.commit()
    cursor.close()

    return actividad_id

def insert_alumno(nombre, baja, canalizacion, materia, tutor_id):
    connection = get_connection()
    cursor = connection.cursor()
    query = "INSERT INTO alumno (nombre, encuesta_baja, canalizacion, mat_acredi_extr, tutor_id) VALUES (%s, %s, %s, %s, %s)"
    #query = "INSERT INTO alumno (nombre, encuesta_baja, canalizacion, mat_acredi_extr, tutor_id) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nombre, baja, canalizacion, materia, tutor_id))
    connection.commit()
    cursor.close()
    connection.close()

def submitForm():
    if request.method == 'POST':
        tutor = request.form.get('tutor')
        tutor_id = insert_tutor(tutor)

        actividades = request.form.getlist('documentos[]')
        asistencias = request.form.getlist('asistencia[]')
        grupo = request.form.get('grupo')

        for actividad, asistencia in zip(actividades, asistencias):
            actividad_id = insert_actividad(actividad, asistencia, grupo, tutor_id)

            carrera = request.form.get('carrera')
            grupo = request.form.get('grupo')
            seguimiento = request.form('grupo')

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
                        VALUES (%s, %s, s%, %s, %s, %s)"""
            cursor.execute(query, (carrera, grupo, actividad_id, '', tutor_id, seguimiento))
            connection.commit()
            cursor.close()
            connection.close()

        nombres = request.form.getlist('nombres[]')
        bajas = request.form.getlist('baja[]')
        canalizaciones = request.form.getlist('canalizacion[]')
        materias = request.form.getlist('materias[]')

        for nombre, baja, canalizacion, materia in zip(nombres, bajas, canalizaciones, materias):
            insert_alumno(nombre, baja, canalizacion, materia, tutor_id)

        connection = get_connection()
        cursor = connection.cursor()

        cursor.close()
        connection.close()

        return redirect(url_for('table'))

def get_form():
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM entregables"
    cursor.execute(query)
    data_tuples = cursor.fetchall()
    cursor.close()
    connection.close()

    data = []
    for row in data_tuples:
        data.append({
            'No': row[0],
            'Carrera': row[1],
            'Grupo': row[2],
            'Tutor': row[3],
            'Actividad': row[4],
            'Actividad2': row[5],
            'Actividad3': row[6],
            'Actividad4': row[7],
            'Asistencia': row[8],
            'Asistencia2': row[9],
            'Asistencia3': row[10],
            'Asistencia4': row[11],
            'SegInividual': row[12],
            'SegAcc': 'Entregado' if row[13] == '1' else 'No Entregado',
            'SegAccFech': row[14],
            'Baja': row[15],
            'Canalizacion': row[16]
        })
    return data


# ########Esto lo deje por respaldo, asi que mejor no lo borres hasta todo funcione correctamente########
#
# def submitForm():
#     if request.method == 'POST':
#         carrera = request.form.get('carrera')
#         grupo = request.form.get('grupo')
#         tutor = request.form.get('tutor')
#         actividades = request.form.getlist('documentos[]')
#         asistencias = request.form.getlist('asistencia[]')
#         seg_individual = request.form.get('nombres')
#         seg_acc = request.form.get('seguimiento')
#         fecha = request.form.get('fecha')
#         causa_baja = request.form.get('causa_baja')
#         canalizacion = request.form.get('canalizacion')

#         new_entry = Entregables(
#         Carrera=carrera,
#         Grupo=grupo,
#         Tutor=tutor,
#         Actividad=actividades[0] if len(actividades) > 0 else '',
#         Actividad2=actividades[1] if len(actividades) > 1 else '',
#         Actividad3=actividades[2] if len(actividades) > 2 else '',
#         Actividad4=actividades[3] if len(actividades) > 3 else '',
#         Asistencia=asistencias[0] if len(asistencias) > 0 else '',
#         Asistencia2=asistencias[1] if len(asistencias) > 1 else '',
#         Asistencia3=asistencias[2] if len(asistencias) > 2 else '',
#         Asistencia4=asistencias[3] if len(asistencias) > 3 else '',
#         SegInividual=seg_individual,
#         SegAcc=seg_acc,
#         SegAccFech=datetime.datetime.strptime(fecha, '%Y-%m-%d'),
#         Baja=causa_baja,
#         Canalizacion=canalizacion
#         )


#         if carrera == 'tsu0':
#             carrera = 'TIADSM'
#         elif carrera == 'tsu1':
#             carrera = 'TIAIRD'
#         elif carrera == 'tsu2':
#             carrera = 'TIAEVND'
#         elif carrera == 'tsu3':
#             carrera = 'IDGS'
#         elif carrera == 'tsu4':
#             carrera = 'IRIC'
#         elif carrera == 'tsu5':
#             carrera = 'IEVND'

#         if grupo == 'grupo0':
#             grupo = '1A'
#         elif grupo == 'grupo1':
#             grupo = '1B'
#         elif grupo == 'grupo2':
#             grupo = '2A'
#         elif grupo == 'grupo3':
#             grupo = '2B'
#         elif grupo == 'grupo4':
#             grupo = '3A'
#         elif grupo == 'grupo5':
#             grupo = '3B'
#         elif grupo == 'grupo6':
#             grupo = '4A'
#         elif grupo == 'grupo7':
#             grupo = '4B'
#         elif grupo == 'grupo8':
#             grupo = '5A'
#         elif grupo == 'grupo9':
#             grupo = '5B'
#         elif grupo == 'grupo10':
#             grupo = '6A'
#         elif grupo == 'grupo11':
#             grupo = '6B'
#         elif grupo == 'grupo12':
#             grupo = '7A'
#         elif grupo == 'grupo13':
#             grupo = '7B'
#         elif grupo == 'grupo14':
#             grupo = '8A'
#         elif grupo == 'grupo15':
#             grupo = '8B'
#         elif grupo == 'grupo16':
#             grupo = '9A'
#         elif grupo == 'grupo17':
#             grupo = '9B'
#         elif grupo == 'grupo18':
#             grupo = '10A'
#         elif grupo == 'grupo19':
#             grupo = '10B'

#         if tutor == 'Profe0':
#             tutor = 'Jose Manuel Flores Juarez'
#         elif tutor == 'Profe1':
#             tutor = 'Diana Lizeth Ahuatzi Reyes'
#         elif tutor == 'Profe2':
#             tutor = 'Alfredo Garcia Ruiz'
#         elif tutor == 'Profe3':
#             tutor = 'Elizabeth Cortes Ramos'
#         elif tutor == 'Profe4':
#             tutor = 'Maricela Gress Roldan'
#         elif tutor == 'Profe5':
#             tutor = 'Jose Marin Rugerio Atriano'
#         elif tutor == 'Profe6':
#             tutor = 'Sonia Lopez Rodriguez'
#         elif tutor == 'Profe7':
#             tutor = 'Margarita Lima Esteban'
#         elif tutor == 'Profe8':
#             tutor = 'Juan Gabriel Valencia Muñoz'
#         elif tutor == 'Profe9':
#             tutor = 'Miguel Torreon Hernandez'
#         elif tutor == 'Profe10':
#             tutor = 'Francisco Lopez Briones'
#         elif tutor == 'Profe11':
#             tutor = 'Aldo Giovani Luria Garcia'

#         fecha = request.form['fecha']
#         causa_baja = request.form['causa_baja']
#         canalizacion = request.form['canalizacion']

#         connection = get_connection()
#         cursor = connection.cursor()

#         query = """INSERT INTO entregables (Carrera, Grupo, Tutor, Actividad, Actividad2, Actividad3, Actividad4,
#                 Asistencia, Asistencia2, Asistencia3, Asistencia4, SegInividual, SegAcc, SegAccFech, Baja,
#                 Canalizacion)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
#         values = (carrera, grupo, tutor, actividad, actividad2, actividad3, actividad4, asistencia, asistencia2,
#                 asistencia3, asistencia4, nombres, seguimiento, fecha, causa_baja,
#                 canalizacion)

#         cursor.execute(query, values)
#         connection.commit()

#         cursor.close()
#         connection.close()

#         return "Los datos han sido insertados correctamente en la base de datos."

# def get_form():
#     conector = get_connection()
#     cursor = conector.cursor()
#     consult = "SELECT * FROM entregables "
#     cursor.execute(consult)
#     data_tuplas = cursor.fetchall()
#     cursor.close()
#     conector.close()
#     data = []
#     for data_tuple in data_tuplas:
#         if len(data_tuple) >= 17:
#             seg_acc_status = 'Entregado' if data_tuple[13] == 1 else 'No Entregado'
#             data.append({
#                 'No': data_tuple[0],
#                 'Carrera': data_tuple[1],
#                 'Grupo': data_tuple[2],
#                 'Tutor': data_tuple[3],
#                 'Actividad': data_tuple[4],
#                 'Actividad2': data_tuple[5],
#                 'Actividad3': data_tuple[6],
#                 'Actividad4': data_tuple[7],
#                 'Asistencia': data_tuple[8],
#                 'Asistencia2': data_tuple[9],
#                 'Asistencia3': data_tuple[10],
#                 'Asistencia4': data_tuple[11],
#                 'SegInividual': data_tuple[12],
#                 'SegAcc': seg_acc_status,
#                 'SegAccFech': data_tuple[14],
#                 'Baja': data_tuple[15],
#                 'Canalizacion': data_tuple[16],
#             })

#     return data

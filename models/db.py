import mysql.connector

def get_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cumplimientotutores"
    )
    return mydb

# Ejemplo de uso
if __name__ == "__main__":
    connection = get_connection()
    if connection.is_connected():
        print("Conexión exitosa a la base de datos.")
    else:
        print("No se pudo conectar a la base de datos.")

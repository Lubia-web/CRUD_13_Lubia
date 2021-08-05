# PASO 1: Importar el módulo "mysql.connector" previamente ¡INSTALADO!
import mysql.connector
class MyDatabase:
    
    def open_connection(self):
        connection = mysql.connector.connect( 
            host="localhost",                    
            user="root", 
            passwd="", 
            database="db_inicio")
        return connection
    def insert_db(self, nombre, correo, contrasena):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "INSERT INTO tbl_sesion(NOMBRE, CORREO, CONTRASENA) VALUES (%s,%s,%s)"
        data = (nombre, correo, contrasena)
        cursor.execute(query, data)
        my_connection.commit()
        my_connection.close()

def read_db(self):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "SELECT NOMBRE,CORREO,CONTRASENA FROM TBL_SESION"
        cursor.execute(query)
        registro= " "
        my_connection.commit()
        my_connection.close()



 
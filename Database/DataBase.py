import pyodbc
class Database:
    def __init__(self, server, database, username, password):
        try:
            self.conn_str = (
                f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                f'SERVER={server};'
                f'DATABASE={database};'
                f'UID={username};'
                f'PWD={password};'
            )
            self.conn = pyodbc.connect(self.conn_str)
            self.cursor = self.conn.cursor()
            print("Conexión exitosa a la base de datos.")
        except pyodbc.Error as e:
            print("Error al conectar con la base de datos:", e)
            self.conn = None

    def cerrar(self):
        if self.conn:
            self.conn.close()
            print("Conexión cerrada correctamente.")
        else:
            print("No hay conexión que cerrar.")
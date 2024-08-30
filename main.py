from Database.DataBase import Database
import tkinter as tk
from App.app import GestorApp
import json
def load_config(filename='config.json'):
    with open(filename, 'r') as file:
        return json.load(file)
def main():
    config = load_config()
    server = config.get('db_server')
    database = config.get('db_database')
    username = config.get('db_username')
    password = config.get('db_password')
    root = tk.Tk()
    root.geometry("300x200")
    root.config(bg="white")
    try:
        db = Database(server, database, username, password)
        app = GestorApp(root, db)
        root.mainloop()
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
    finally:
        try:
            db.cerrar()
        except Exception:
            print("No hay conexión que cerrar.")

if __name__ == "__main__":
    main()

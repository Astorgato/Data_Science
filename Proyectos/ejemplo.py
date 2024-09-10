import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host='localhost',           # O la dirección del servidor MySQL
    database='ServerPrueba', # Nombre de la base de datos
    user='root',           # Usuario de la base de datos
    password='Gato1234!'     # Contraseña del usuario
)
if conn.is_connected():
    print("Conexión exitosa")
    
cursor = conn.cursor() 
cursor.execute("SELECT * FROM Cliente") 
result = cursor.fetchall()

print(pd.DataFrame(result))
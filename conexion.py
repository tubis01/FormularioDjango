import psycopg2

try:
    # Establecer la conexión
    conexion = psycopg2.connect(
        database="ingenieria",
        user="alumno",  # Reemplaza 'tu_usuario' con tu usuario de PostgreSQL
        password="123456",  # Usa el password que configuraste para tu base de datos
        host="localhost",  # O la dirección IP del servidor de la base de datos si es remoto
        port="5432"  # El puerto por defecto de PostgreSQL es 5432
    )
    
    # Crear un cursor
    cursor = conexion.cursor()
    
    # Ejecutar una consulta SQL
    cursor.execute("SELECT version();")
    
    # Recuperar el resultado
    version = cursor.fetchone()
    print(f"Conexión exitosa a PostgreSQL. Versión de la base de datos: {version}")
    
    # Cerrar la conexión
    cursor.close()
    conexion.close()
    
except psycopg2.DatabaseError as e:
    print(f"Error al conectar a la base de datos: {e}")

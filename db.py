import pymysql

def get_connection():
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='NUNC4m13nt!',
        db='test'
    )
    return connection

def execute_query(connection, query, params=None):
    """Ejecuta una consulta SQL en la base de datos."""
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        connection.commit()
        return cursor.fetchall()


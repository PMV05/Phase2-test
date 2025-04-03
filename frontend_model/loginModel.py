from flask import session
from frontend_model.connectDB import *
import pymysql
from passlib.hash import sha256_crypt

def loginmodel(email, password):
    # Se crea una instancia para crear la conexion con la base de datos
    # En el query se selecciona el id, email y password del usuario activo, 
    # Segun el email entrado por el usuario
    db = Dbconnect()
    sql = "SELECT c_email, customer_ID, c_password, c_status FROM customer WHERE c_email = %s"
    userFound = db.select(sql, (email,))

    if not userFound:
        return None  # Usuario no encontrado

    user = userFound[0]

    if sha256_crypt.verify(password, user['c_password']):
        # Guardar ID en sesión
        session['customer'] = user['customer_ID']
        return user  # Devuelve el usuario completo
    else:
        return None  # Contraseña incorrecta


def registermodel(fname, lname, email, password):
    # Se crea una instancia para crear la conexion con la base de datos
    # En el query, se añade en la tabla de customer un nuevo cliente, donde 
    # se almacenara el nombre, apellido, email y password del usuario
    db = Dbconnect()

    # TODO: 
            
    sql = "INSERT INTO customer (c_first_name, c_last_name, c_email, c_password, c_status) VALUES (%s, %s, %s, %s, %s)" 

    status = 'active'

    hash_password = sha256_crypt.encrypt(password)
    
    db.execute(sql, (fname, lname, email, password, status))

    return True

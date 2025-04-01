import pymysql
from flask import session
from frontend_model.connectDB import *
from passlib.handlers.sha2_crypt import sha256_crypt
import re
from datetime import datetime

def getUserModel():
    db = Dbconnect()
    query = '''
        SELECT c.customer_ID, c.c_first_name, c.c_last_name, c.c_email, c.c_phone_number, c.c_status,
               a.ad_street, a.ad_city, a.ad_state, a.ad_postal_code,
               pm.payment_email
        FROM customer c
        JOIN address a ON c.customer_ID = a.customer_ID
        JOIN payment_method pm ON c.customer_ID = pm.customer_ID
        WHERE c.customer_ID = %s AND c.c_status = 'active'
    '''
    try:
        userFound = db.select(query, (session['customer'],))
        user = []
        for u in userFound:
            user.append({
                "id": u['customer_ID'],
                "c_first_name": u['c_first_name'],
                "c_last_name": u['c_last_name'],
                "c_email": u['c_email'],
                "c_phone_number": u['c_phone_number'],
                "c_status": u['c_status'],
                "ad_street": u['ad_street'],
                "ad_city": u['ad_city'],
                "ad_state": u['ad_state'],
                "ad_postal_code": u['ad_postal_code'],
                "payment_email": u['payment_email']
            })
        return user
    except pymysql.Error as error:
        print(error)
        return []

def editnumbermodel(number):
    db = Dbconnect()
    query = "UPDATE customer SET c_phone_number = %s WHERE customer_ID = %s"
    try:
        db.execute(query, (number, session['customer']))
        return 0
    except pymysql.Error as error:
        print(error)
        return 1

def addaddressmodel(street, state, postal_code, city):
    db = Dbconnect()
    query = ("INSERT INTO address (address_ID, ad_street, ad_city, ad_state, ad_postal_code)"
             " VALUES(%s, %s, %s, %s, %s)")
    try:
        db.execute(query, (session['customer'], street, city, state, postal_code))
        return 0
    except pymysql.Error as error:
        print(error)
        return 1

def editaddressmodel(street, state, postal_code, city, a_id):
    db = Dbconnect()
    query = ("UPDATE address SET ad_street = %s, ad_city = %s, "
             "ad_state = %s, ad_postal_code = %s WHERE customer_ID = %s AND address_ID = %s")
    try:
        db.execute(query, (street, city, state, postal_code, session['customer'], a_id))
        return 0
    except pymysql.Error as error:
        print(error)
        return 1

def getpaymentmodel(customer):
    db = Dbconnect()
    query = "SELECT * FROM payment_method WHERE customer_id = %s"
    try:
        return db.select(query, (customer,))
    except pymysql.Error as error:
        print(error)
        return []

def editpaymentemailmodel(email):
    db = Dbconnect()
    query = "UPDATE payment_method SET payment_email = %s WHERE customer_ID = %s"
    try:
        db.execute(query, (email, session['customer']))
        return 0
    except pymysql.Error as error:
        print(error)
        return 1

def editprofilemodel(fname, lname, email):
    db = Dbconnect()
    query = "UPDATE customer SET c_first_name = %s, c_last_name = %s, c_email = %s WHERE customer_ID = %s"
    try:
        db.execute(query, (fname, lname, email, session['customer']))
        return 0
    except pymysql.Error as error:
        print(error)
        return 1

def getAddressModel(customer):
    db = Dbconnect()
    sql = "SELECT * FROM address WHERE address_ID = %s"
    try:
        return db.select(sql, (customer,))
    except pymysql.Error as error:
        print(error)
        return []

def changepassmodel(email):
    db = Dbconnect()
    try:
        query = "SELECT c_password FROM customer WHERE c_email = %s"
        userFound = db.select(query, (email,))
        if userFound:
            hash = sha256_crypt.hash(userFound[0]['c_password'])
            query2 = "UPDATE customer SET c_password = %s WHERE c_email = %s "
            db.execute(query2, (hash, email))
            return 1
        return 0
    except pymysql.Error as error:
        print(error)
        return 0
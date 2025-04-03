import pymysql
from flask import session
from frontend_model.connectDB import Dbconnect
from passlib.handlers.sha2_crypt import sha256_crypt

def getUserModel():
    db = Dbconnect()
    query = '''
        SELECT c.customer_ID, c.c_first_name, c.c_last_name, c.c_email, c.c_password,
               c.c_phone_number, c.c_status,
               c.c_payment_email, c.c_payment_postal_code,
               a.ad_street, a.ad_city, a.ad_state, a.ad_postal_code
        FROM customer c
        LEFT JOIN address a ON c.customer_ID = a.customer_ID
        WHERE c.customer_ID = %s AND c.c_status = 'active'
    '''
    try:
        userFound = db.select(query, (session['customer'],))
        user = []
        for u in userFound:
            user.append({
                "id": u['customer_ID'],
                "first_name": u['c_first_name'],
                "last_name": u['c_last_name'],
                "email": u['c_email'],
                "password": u['c_password'],
                "phone_number": u['c_phone_number'],
                "status": u['c_status'],
                "street": u['ad_street'],
                "city": u['ad_city'],
                "state": u['ad_state'],
                "postal_code": u['ad_postal_code'],
                "c_payment_email": u['c_payment_email'],
                "c_payment_postal_code": u['c_payment_postal_code'],
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
    query_check = "SELECT * FROM address WHERE customer_ID = %s"
    address_exists = db.select(query_check, (session['customer'],))
    if address_exists:
        return editaddressmodel(street,  city, state, postal_code)

    query = ("INSERT INTO address (customer_ID, ad_street, ad_city, ad_state, ad_postal_code) "
             "VALUES (%s, %s, %s, %s, %s)")
    try:
        db.execute(query, (session['customer'], street, city, state, postal_code))
        return 0
    except pymysql.Error as error:
        print(error)
        return 1

def editaddressmodel(street,city, state, postal_code):
    db = Dbconnect()
    query = """
            UPDATE address 
                SET ad_street = %s, ad_city = %s, ad_state = %s, ad_postal_code = %s 
                WHERE customer_ID = %s
"""
    try:
        db.execute(query, (street, city, state, postal_code, session['customer']))
        return 0
    except pymysql.Error as error:
        print(error)
        return 1

def addpaymentmodel(payment_email, payment_postal_code, customer_ID):
    db = Dbconnect()
    try:
        check = db.select("SELECT c_payment_email FROM customer WHERE customer_ID = %s", (customer_ID,))
        if check and check[0]['c_payment_email']:
            return editpaymentemailmodel(payment_email, payment_postal_code)
        query = "UPDATE customer SET c_payment_email = %s, c_payment_postal_code = %s WHERE customer_ID = %s"
        db.execute(query, (payment_email, payment_postal_code, customer_ID))
        return 0
    except pymysql.Error as error:
        print(error)
        return 1


def editpaymentemailmodel(email, postal_code):
    db = Dbconnect()
    query = "UPDATE customer SET c_payment_email = %s, c_payment_postal_code = %s WHERE customer_ID = %s"
    try:
        db.execute(query, (email, postal_code, session['customer']))
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
    sql = "SELECT * FROM address WHERE customer_ID = %s"
    try:
        return db.select(sql, (customer,))
    except pymysql.Error as error:
        print(error)
        return []

def changepassmodel(email , newPass):
    db = Dbconnect()
    hashed_new_pass = sha256_crypt.encrypt(newPass)
    try:
        query2 = "UPDATE customer SET c_password = %s WHERE c_email  = %s"
        db.execute(query2, (hashed_new_pass, email))
        return 1
    except pymysql.Error as error:
        print(error)
        return 0
import pymysql
from flask import session
from frontend_model.connectDB import *
from passlib.handlers.sha2_crypt import sha256_crypt

def getUserModel():
    user = []
    db = Dbconnect()
    query = "SELECT * FROM customer WHERE customer_ID = %s AND c_status = 'active'"
    # Find user via the customer ID saved in session
    userFound = db.select(query, session['customer'])

    # Save tuple information in a list
    for users in userFound:
        user.append({"id": users['customer_ID'], "name": users['c_first_name'], "last_name": users['c_last_name'], "email": users['c_email'],
                     "password": users['c_password'], "phone_number": users['c_phone_number'], "status": users['c_status']})

    # Example: to access user info:

        # for u in user:
        # u['id'], u['name'], u['email'], etc...
    return user


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

    db.execute(query, (session['customer'], street, city, state, postal_code))

    return 0

def editaddressmodel(street, state, postal_code, city, a_id):
    db = Dbconnect()
    query = ("UPDATE address SET ad_street = %s, ad_city = %s, "
             "ad_state = %s ad_postal_code = %s WHERE customer_ID = %s AND address_ID = %s")
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
        methods = db.select(query, (customer,))
        return methods

    except pymysql.Error as error:
        print(error)
        return []

#TODO: VERIFICAR Y HACER
def editpaymentmodel(name, c_type, number, exp_date):
    print("STUDENTS MUST ADD")
    return 0


def editprofilemodel(fname, lname, email):
    db = Dbconnect()
    query = "UPDATE customer SET c_first_name = %s, c_last_name = %s, c_email = %s WHERE customer_ID = %s"
    try:
        db.execute(query,(fname, lname, email, session['customer']))
        return 0

    except pymysql.Error as error:
        print(error)
        return 1


def getAddressModel(customer):
    db = Dbconnect()
    sql = "SELECT * FROM address WHERE address_ID = %s"
    result = db.select(sql, (customer))

    return result


def changepassmodel(email):
    passw = ''
    # Connect to MySQL database server using credentials provided
    db = Dbconnect()
    query = "SELECT * FROM customer WHERE c_email = %s"

    userFound = db.select(query, email)

    for users in userFound:
        # Save the user's password in 'passw'
        passw = users['c_password']

    # Encrypt the password using the sha256_crypt function
    hash = sha256_crypt.encrypt(passw)

    try:
        # Once encrypted, save this new hashed password to DB
        query2 = "UPDATE customer SET c_password = %s WHERE c_email = %s "
        db.execute(query2, (hash, email))
        return 1

    except pymysql.Error as error:
        print(error)
        return 0

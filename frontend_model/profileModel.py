import pymysql
from flask import session
from frontend_model.connectDB import *
from passlib.handlers.sha2_crypt import sha256_crypt

def getUserModel():
    user = []
    db = Dbconnect()
    query = "SELECT * FROM Customer WHERE ID = %s"
    # Find user via the customer ID saved in session
    userFound = db.select(query, session['customer'])

    # Save tuple information in a list
    for users in userFound:
        user.append({"id": users['ID'], "name": users['first_name'], "last_name": users['last_name'], "email": users['email'],
                     "password": users['password'], "phone_number": users['phone_number'], "status": users['status']})

    # Example: to access user info:

        # for u in user:
        # u['id'], u['name'], u['email'], etc...
    return user


def editnumbermodel(number):
    db = Dbconnect()
    query = "UPDATE Customer SET phone_number = %s WHERE ID = %s"
    try:
        db.execute(query, (number, session['customer']))
        return 0

    except pymysql.Error as error:
        print(error)
        return 1


def addaddressmodel(aline1, state, zipcode, city):
    db = Dbconnect()
    query = ("INSERT INTO Address (ID, street, city, state, postal_code)"
             " VALUES(%s, %s, %s, %s, %s)")

    db.execute(query, (session['customer'], aline1, city, state, zipcode))

    return 0

def editaddressmodel(aline1, state, zipcode, city, a_id):
    db = Dbconnect()
    query = ("UPDATE Address SET street = %s, city = %s, "
             "state = %s postal_code = %s WHERE customer_ID = %s AND ID = %s")
    try:
        db.execute(query, (aline1, city, state, zipcode, session['customer'], a_id))
        return 0

    except pymysql.Error as error:
        print(error)
        return 1


def getpaymentmodel(customer):
    db = Dbconnect()
    query = "SELECT * FROM payment_method WHERE c_id = %s"

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
    query = "UPDATE Customer SET first_name = %s, last_name = %s, email = %s WHERE ID = %s"
    try:
        db.execute(query,(fname, lname, email, session['customer']))
        return 0

    except pymysql.Error as error:
        print(error)
        return 1


def getAddressModel(customer):
    db = Dbconnect()
    sql = "SELECT * FROM Address WHERE ID = %s"
    result = db.select(sql, (customer))

    return result


def changepassmodel(email):
    passw = ''
    # Connect to MySQL database server using credentials provided
    db = Dbconnect()
    query = "SELECT * FROM Customer WHERE email = %s"

    userFound = db.select(query, email)

    for users in userFound:
        # Save the user's password in 'passw'
        passw = users['password']

    # Encrypt the password using the sha256_crypt function
    hash = sha256_crypt.encrypt(passw)

    try:
        # Once encrypted, save this new hashed password to DB
        query2 = "UPDATE Customer SET password = %s WHERE email = %s "
        db.execute(query2, (hash, email))
        return 1

    except pymysql.Error as error:
        print(error)
        return 0

from flask import session
# TODO: 
from frontend_model.connectDB import *
import pymysql
from passlib.hash import sha256_crypt

# # This is a very basic dictionary with information for logging in
# # Simulating our database
# thisDict = {
#     "email": "javier.quinones3@upr.edu",
#     "password": "pass1234",
#     "user": "Javier"
# }


# def loginmodel(email, password):
#     # Receive email and password to check in the "database"
#     if email in thisDict.values() and password in thisDict.values():
#         # If it found the email and pass in the dictionary
#         session['customer'] = thisDict['user']
#         # Create the session['customer']
#         return "true"
#     else:
#         # If it didn't find user
#         return "false"

def loginmodel(email, password):

    # Receive email and password to check in the "database"

    user = []
    db = Dbconnect()
    sql = "SELECT email, ID, password, status FROM Customer WHERE email = %s"
    # Save user info in list
    userFound = db.select(sql, (email,))

    print(userFound)

    for res in userFound:
        user.append({"id": res['ID'], "email": res['email'], "password": res['password'], "status": res['status']})


    # Save user info in list

    # sha256_crypt.encrypt("password") = this is what is used to encrypt a password
    # sha256_crypt.verify(password_unhashed, password_hashed) = this is what is used to compare an unhashed and hashed password

    for u in user:
        if email == u['email'] and sha256_crypt.verify(password, u['password']) is True:
            session['customer'] = u['id']
            # Create the session['customer'] saving the customer ID if user is found
            return "true"
        else:
            # If it didn't find user
            return "false"


def registermodel(fname, lname, email, password):
    db = Dbconnect()

    # TODO: Falta verificar que el usuario no esté en la base de datos
            
    sql = "INSERT INTO Customer (first_name, last_name, email, password, status) VALUES (%s, %s, %s, %s, %s)" 

    status = 'active'

    hash_password = sha256_crypt.encrypt(password)
    
    db.execute(sql, (fname, lname, email, hash_password, status))

    return True

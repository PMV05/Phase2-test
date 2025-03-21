from frontend_model.loginModel import *
from flask import redirect, render_template


def logincontroller(email, password):
    result = loginmodel(email=email, password=password)
    # Check from loginModel's loginmodel() if user exists

    if 'request' in session:
        request = session['request']
        session.pop('request', None)
        return redirect(request)

    if result == "true":
        # If user exists, enter shop
        return redirect("/shop")
    else:
        # If user doesn't exist, return to login and trigger error message
        return redirect("/message")


def registercontroller(fname, lname, email, pass1, pass2):
    if pass1 != pass2:
        return '/register/<message>'

    # TODO: TO BE ADDED BY STUDENTS
    print("REGISTER TO BE ADDED BY STUDENTS")

    # Passwords must be hashed in the database
    hash = sha256_crypt.encrypt(pass1)

    res = registermodel(fname, lname, email, hash)

    if res:
        return '/shop'
    else:
        return '/register'


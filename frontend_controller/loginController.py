from frontend_model.loginModel import *
from flask import redirect, render_template


from frontend_model.loginModel import *
from flask import redirect, render_template, session  # Asegúrate de importar session

def logincontroller(email, password):
    user = loginmodel(email=email, password=password)

    if user:
        if 'request' in session:
            request_url = session.pop('request')
            return redirect(request_url)
        return redirect("/shop")
    else:
        return redirect("/wrong")



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


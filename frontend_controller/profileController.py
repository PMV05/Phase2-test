from frontend_model.profileModel import *
from flask import session

def getUser():
    return getUserModel()

def getAddress(customer):
    return getAddressModel(customer)

def editnumbercontroller(number):
    return editnumbermodel(number)

def addaddresscontroller(street, state, zipcode, city):
    return addaddressmodel(street, state, zipcode, city)

def editaddresscontroller(street, state, zipcode, city, a_id):
    return editaddressmodel(street, state, zipcode, city, a_id)

def getpaymentcontroller():
    return getpaymentmodel(session['customer'])

def editpaymentcontroller(paypal_email):
    return editpaymentemailmodel(paypal_email)

def editprofilecontroller(fname, lname, email):
    return editprofilemodel(fname, lname, email)

def changePass(email):
    return changepassmodel(email)
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

def editaddresscontroller(street, state, zipcode, city,):
    return editaddressmodel(street, state, zipcode, city,)

def getpaymentcontroller():
    return getpaymentmodel(session['customer'])

def addpaymentcontroller(payment_email, payment_postal_code, customer_ID):
    return addpaymentmodel(payment_email, payment_postal_code, customer_ID)

def editpaymentcontroller(paypal_email):
    return editpaymentemailmodel(paypal_email)

def editprofilecontroller(fname, lname, email):
    return editprofilemodel(fname, lname, email)

def changePass(email,newPass):
    return changepassmodel(email, newPass)
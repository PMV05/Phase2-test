# TODO:
import pymysql
from flask import session
from frontend_model.connectDB import *


# # Simulated tuple from customer database
# # By order: customer ID, first name, last name, address line 1, address line 2, city, state, zip code, email
# # password, phone number, payment card name, payment card type, payment card number, payment card expiration date, customer status

# user = [1, "Javier", "Quiñones", "Vista Rojas", "Calle 15 L15", "Arecibo", "Puerto Rico", "00612", "javier.quinones3@upr.edu",
#         "pass1234", 7871231234, "Javier Quiñones", "Mastercard", 1234123412341234, '2023-01-20', "active"]


# def getUserModel():
#     return user

def validateUserModel():
    user = []
    # Find user in DB according to customer ID saved in session
    db = Dbconnect()
    query = "SELECT * from customer WHERE c_id = %s"

    userFound = db.select(query, (session['customer'],))

    for users in userFound:
        user.append({"id": users['customer_ID'], "name": users['c_first_name'], "last_name": users['c_last_name'],
                     "email": users['c_email'],
                     "password": users['c_password'], "phone_number": users['c_phone_number'],
                     "status": users['c_status']})

    return user

def getUserCheckout():
    # Simulación de obtención de datos del usuario para el checkout
    return {
        "phone_number": "1234567890"  # Simula un número de teléfono
    }
def editCheckoutQuantity(product_id, new_quantity):
    db = Dbconnect()
    if new_quantity > 0:
        query = "UPDATE order_product SET op_product_quantity = %s WHERE product_id = %s AND customer_id = %s"
        db.execute(query, (new_quantity, product_id, session['customer']))
        return True  # Successfully updated
    
        
    
def saveCartToDB():
    if 'cart' not in session or not session['cart']:
        return False  # No cart data to save

    db = Dbconnect()

    for key, item in session['cart'].items():
        query = "INSERT INTO order_product (order_id, op_product_id, op_product_quantity, op_product_price) VALUES (%s, %s, %s, %s)"
        db.execute(query, (session['customer'], key, item['quantity'], item['total_price']))

    session.pop('cart')  # Clear session cart after saving
    return True
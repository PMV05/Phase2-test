        # TODO:
import pymysql
from flask import session
from frontend_model.connectDB import *


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
    db = Dbconnect()
    query = """
        SELECT
            c.customer_ID,
            c.c_first_name,
            c.c_last_name,
            a.ad_street,
            a.ad_city,
            a.ad_state,
            a.ad_postal_code,
            c.c_email,
            c.c_password,
            c.c_phone_number
        FROM customer c
        LEFT JOIN address a ON c.customer_ID = a.customer_ID
        LEFT JOIN payment_method pm ON c.customer_ID = pm.customer_ID
        WHERE c.customer_ID = %s
    """
    result = db.select(query, (session['customer'],))
    if not result:
        return {}
    
    row = result[0]
    user_data = {
        "customer_ID": row['customer_ID'],
        "first_name": row['c_first_name'],
        "last_name": row['c_last_name'],
        "address_line1": row['ad_street'],
        "city": row['ad_city'],
        "state": row['ad_state'],
        "postal_code": row['ad_postal_code'],
        "email": row['c_email'],
        "password": row['c_password'],
        "phone_number": row['c_phone_number'],
    }
    return user_data

      
        
def saveCartToDB():
    if 'cart' not in session or not session['cart']:
        return False 

    db = Dbconnect()

    for key, item in session['cart'].items():
        query = "INSERT INTO order_product (order_id, op_product_id, op_product_quantity, op_product_price) VALUES (%s, %s, %s, %s)"
        db.execute(query, (session['customer'], key, item['quantity'], item['total_price']))

    session.pop('cart')  
    return True
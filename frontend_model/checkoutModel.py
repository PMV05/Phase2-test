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
            c.c_phone_number,
            pm.payment_email
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
        "payment_email": row['payment_email']
    }
    return user_data

def editnumbermodel(number):
    db = Dbconnect()
    query = "UPDATE customer SET c_phone_number = %s WHERE customer_ID = %s"
    try:
        db.execute(query, (number, session['customer']))
        return 0
    except pymysql.Error as error:
        print(error)
        return 1

def editpaymentemailmodel(email):
    db = Dbconnect()
    query = "UPDATE payment_method SET payment_email = %s WHERE customer_ID = %s"
    try:
        db.execute(query, (email, session['customer']))
        return 0
    except pymysql.Error as error:
        print(error)
        return 1
    
def editaddressmodel(street, state, postal_code, city):
    db = Dbconnect()
    query = ("UPDATE address SET ad_street = %s, ad_city = %s, "
            "ad_state = %s, ad_postal_code = %s WHERE customer_ID = %s")
    try:
        db.execute(query, (street, city, state, postal_code, session['customer']))
        return 0
    except pymysql.Error as error:
        print(error)
        return 1
    
def saveCartToDB():
    if 'cart' not in session or not session['cart']:
        return False 

    db = Dbconnect()

    for key, item in session['cart'].items():
        query = "INSERT INTO order_product (order_id, op_product_id, op_product_quantity, op_product_price) VALUES (%s, %s, %s, %s)"
        db.execute(query, (session['customer'], key, item['quantity'], item['total_price']))

    session.pop('cart')  
    return True

def saveOrder(customer_id, cart, total):
    db = Dbconnect()
    cursor = db.connection.cursor(pymysql.cursors.DictCursor)

    # Buscar dirección y método de pago
    cursor.execute("SELECT address_ID FROM address WHERE customer_ID = %s", (customer_id,))
    address = cursor.fetchone()

    cursor.execute("SELECT payment_method_ID FROM payment_method WHERE customer_ID = %s", (customer_id,))
    payment = cursor.fetchone()

    if not address or not payment:
        return None

    address_id = address['address_ID']
    payment_id = payment['payment_method_ID']

    # Insertar nueva orden (con columnas correctas)
    cursor.execute("""
    INSERT INTO `order` (o_order_date, o_delivery_date, o_status, customer_ID, address_ID, payment_method_ID)
    VALUES (CURDATE(), DATE_ADD(CURDATE(), INTERVAL 3 DAY), 'in progress', %s, %s, %s)
    """, (customer_id, address_id, payment_id))

    db.connection.commit()

    order_id = cursor.lastrowid

    # Insertar productos en order_product
    for key, item in cart.items():
        cursor.execute("""
            INSERT INTO order_product (order_ID, op_product_ID, op_product_quantity, op_product_price)
            VALUES (%s, %s, %s, %s)
        """, (order_id, key, item['quantity'], item['price']))

    db.connection.commit()
    cursor.close()

    return order_id


def saveOrderWithProducts():
    customer_id = session.get("customer")
    cart = session.get("cart")
    total = session.get("total")

    if not customer_id or not cart:
        return None

    return saveOrder(customer_id, cart, total)
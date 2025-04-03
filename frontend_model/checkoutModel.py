import pymysql
from flask import session
from frontend_model.connectDB import Dbconnect


def validateUserModel():
    user = []
    db = Dbconnect()
    query = "SELECT * from customer WHERE c_id = %s"
    userFound = db.select(query, (session['customer'],))
    for users in userFound:
        user.append({
            "id": users['customer_ID'],
            "name": users['c_first_name'],
            "last_name": users['c_last_name'],
            "email": users['c_email'],
            "password": users['c_password'],
            "phone_number": users['c_phone_number'],
            "status": users['c_status']
        })
    return user


def getUserCheckout():
    db = Dbconnect()
    query = """
        SELECT c.customer_ID, c.c_first_name, c.c_last_name, c.c_email, c.c_phone_number,
            a.ad_street, a.ad_city, a.ad_state, a.ad_postal_code,
            c.c_payment_email, c.c_payment_postal_code
        FROM customer c
        LEFT JOIN address a ON c.customer_ID = a.customer_ID
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
    "phone_number": row['c_phone_number'],
    "payment_email": row['c_payment_email'],
    "payment_postal_code": row['c_payment_postal_code']
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


def editpaymentemailmodel(email, postal_code):
    db = Dbconnect()
    query = "UPDATE customer SET c_payment_email = %s, c_payment_postal_code = %s WHERE customer_ID = %s"
    try:
        db.execute(query, (email, postal_code, session['customer']))
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


def saveOrder(customer_id, cart, total):
    db = Dbconnect()
    cursor = db.connection.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT address_ID FROM address WHERE customer_ID = %s", (customer_id,))
    address = cursor.fetchone()

    if not address:
        return None

    address_id = address['address_ID']

    # Generar número de tracking numérico de 8 dígitos
    import random
    tracking_num = str(random.randint(10000000, 99999999))

    # Insertar orden
    cursor.execute("""
        INSERT INTO `order` (
            o_tracking_number, o_order_date, o_delivery_date, o_status, customer_ID, address_ID
        )
        VALUES (%s, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 3 DAY), 'in progress', %s, %s)
    """, (tracking_num, customer_id, address_id))
    db.connection.commit()

    order_id = cursor.lastrowid

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

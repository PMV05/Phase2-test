import pymysql
from frontend_model.connectDB import *
from datetime import datetime


# Se crea una instancia para la conceccion de la base de datos.
# Obtiene la consulta del SQL que obtiene las ordenes de los clientes.
# Se ejecuta la consulta SQL, pasando el customer_id como parámetro en la consulta.
# Obtenemos todos los resultados de la consulta.
# Se cierra el cursor después de ejecutar la consulta para liberar recursos.
# Devuelve los resultados obtenidos de las ordenes. 


def get_user_orders(customer_id):
    db = Dbconnect()
    cursor = db.connection.cursor(pymysql.cursors.DictCursor)

    query = """
    SELECT 
        o.order_ID, o.o_tracking_number, o.o_order_date, o.o_delivery_date,
        o.o_status, o.o_transaction_number,
        a.ad_street, a.ad_city, a.ad_state, a.ad_postal_code,
        op.op_product_ID, op.op_product_quantity, op.op_product_price,
        p.p_name, p.p_brand, p.p_image
    FROM `order` o
    JOIN address a ON o.address_ID = a.address_ID
    JOIN order_product op ON o.order_ID = op.order_ID
    JOIN product p ON op.op_product_ID = p.product_ID
    WHERE o.customer_ID = %s
    ORDER BY o.order_ID DESC
    """

    cursor.execute(query, (customer_id,))
    results = cursor.fetchall()
    cursor.close()

    # Agrupar por order_ID
    orders = {}
    for row in results:
        oid = row['order_ID']
        if oid not in orders:
            orders[oid] = {
                'tracking_num': row['o_tracking_number'],
                'order_date': row['o_order_date'].strftime('%m/%d/%y'),
                'arrival_date': row['o_delivery_date'].strftime('%m/%d/%y'),
                'address_line_1': row['ad_street'],
                'address_line_2': f"{row['ad_city']} {row['ad_state']}, {row['ad_postal_code']}",
                'status': row['o_status'],
                'total': 0,
                'amount': 0,
                'products': {}
            }

        # Agregar producto
        pid = len(orders[oid]['products']) + 1
        total_price = row['op_product_quantity'] * row['op_product_price']
        orders[oid]['products'][pid] = {
            'name': row['p_name'],
            'brand': row['p_brand'],
            'image': row['p_image'],
            'price': row['op_product_price'],
            'quantity': row['op_product_quantity'],
            'total_price': total_price
        }
        orders[oid]['total'] += total_price
        orders[oid]['amount'] += row['op_product_quantity']

    return orders

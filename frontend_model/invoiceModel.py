from frontend_model.connectDB import Dbconnect

def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False


# Definimos una funcion getOrderModel que tomara el order_id
# Se crea una conexion con la base de datos
# En este campo una vez hagamos todo el proceso del checkout nos brindara una tabla con toda la informacion importante de neustro pedido.
# Ejecutamos con order_id como parametro y almacenamos el resultado.
# Si hay resultados, se devuelve el primer resultado, si no, se devuelve vacio.
def getOrderModel(order_id):
    db = Dbconnect()
    query = """
        SELECT 
            o.o_tracking_number AS tracking_num,
            DATE_FORMAT(o.o_order_date, '%%m/%%d/%%y') AS order_date,
            DATE_FORMAT(o.o_delivery_date, '%%m/%%d/%%y') AS arrival_date,
            o.o_status,
            CONCAT(a.ad_street, ', ', a.ad_city) AS address_line_1,
            CONCAT(a.ad_state, ', ', a.ad_postal_code) AS address_line_2,
            c.c_payment_email AS payment_method,
            (
                SELECT SUM(op.op_product_quantity * op.op_product_price)
                FROM order_product op
                WHERE op.order_ID = o.order_ID
            ) AS total
        FROM `order` o
        JOIN address a ON o.address_ID = a.address_ID
        JOIN customer c ON o.customer_ID = c.customer_ID
        WHERE o.order_ID = %s
    """
    result = db.select(query, (order_id,))
    return result[0] if result else {}


# Definimos una funcion getOrderModel que tomara el order id.
# Se crea una conexion con la base de datos.
# Obtenenos los porductos comprados en un pedido.
def getProductsModel(order_id):
    db = Dbconnect()
    query = """
        SELECT 
            p.product_ID,
            p.p_name,
            p.p_brand,
            p.p_image,
            op.op_product_quantity,
            op.op_product_price,
            (op.op_product_quantity * op.op_product_price) AS total_price
        FROM order_product op
        JOIN product p ON op.op_product_ID = p.product_ID
        WHERE op.order_ID = %s;
    """
    return db.select(query, (order_id,))

from frontend_model.ordersModel import *


from frontend_model.ordersModel import (
    # get_order_products,
    # delete_order,
    # delete_order_products,
    getorder1M,
    getorder2M,
    getorder1prodM,
    getorder2prodM
)

#* Funciones de la simulacion 
def getorder1():
    return getorder1M()


def getorder2():
    return getorder2M()


def getorder1products():
    return getorder1prodM()


def getorder2products():
    return getorder2prodM()
#? Verificar que las funciones esten correctas 


# def get_order_products_controller(order_id):
#     return get_order_products(order_id)


# def delete_order_controller(order_id):
#     delete_order(order_id)
#     return {"status": "success", "message": f"Order {order_id} deleted."}


# def delete_order_products_controller(order_id):
#     delete_order_products(order_id)
#     return {"status": "success", "message": f"Products of order {order_id} deleted."}

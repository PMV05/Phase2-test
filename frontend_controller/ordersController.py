from frontend_model.ordersModel import get_user_orders

def get_orders_controller(customer_id):
    return get_user_orders(customer_id)

from frontend_model.invoiceModel import *

def getOrderInfo(order_id):
    return getOrderModel(order_id)

def getOrderProducts(order_id):
    return getProductsModel(order_id)

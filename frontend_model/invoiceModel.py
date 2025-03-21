
def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False

orderDict = {
    "tracking_num": "71287249",
    "order_date": "01/17/25",
    "arrival_date": "01/20/25",
    "address_line_1": "Vista Rojas Calle 15 L15",
    "address_line_2": "Arecibo Puerto Rico, 00614",
    "total": 507.00,
    "payment_method": "Mastercard"
}

productDict1 = {"1":{
    "image": 'imagenes_audifonos/apple/apple_airpods_4.jpg',
    "name": 'Apple Airpods 4',
    "brand": 'Apple',
    "price": 129.00,
    "quantity": 2,
    "total_price": 258.00
}}

productDict2 = {"2":{
    "image": 'imagenes_audifonos/apple/apple_airpods_max.jpg',
    "name": 'Apple Airpods Max',
    "brand": 'Apple',
    "price": 249.00,
    "quantity": 1,
    "total_price": 249.00
}}

products = productDict1
products = MagerDicts(products, productDict2)


def getOrderModel():
    return orderDict


def getProductsModel():
    return products

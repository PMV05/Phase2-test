# Dictionary uniter
def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False


# Simulated database of orders and their products
# order1 contains productsOrder1...
order1 = {"tracking_num": "71287249",
    "order_date": "01/17/23",
    "arrival_date": "01/20/23",
    "address_line_1": "Vista Rojas Calle 15 L15",
    "address_line_2": "Arecibo Puerto Rico, 00614",
    "total": 509.00,
    "amount": 3,
    "payment_method": "Mastercard",
    "status": 'shipped'}

order2 = {"tracking_num": "92391290",
    "order_date": "01/20/23",
    "arrival_date": "01/23/23",
    "address_line_1": "Vista Rojas Calle 15 L15",
    "address_line_2": "Arecibo Puerto Rico, 00614",
    "total": 297.00,
    "amount": 3,
    "payment_method": "Mastercard",
    "status": 'delivered'}

productDict1 = {"1": {
    "image": 'apple_airpods_4.jpg',
    "name": 'Airpods 4',
    "brand": 'Apple',
    "price": 129.00,
    "quantity": 1,
    "total_price": 129.00
}}

productDict2 = {"2": {
    "image": 'skullcandy_crusher_anc_2.jpg',
    "name": 'Crusher Evo',
    "brand": 'Skullcandy',
    "price": 190.00,
    "quantity": 2,
    "total_price": 380.00
}}

productsOrder1 = productDict1
productsOrder1 = MagerDicts(productsOrder1, productDict2)

productDict3 = {"3": {
    "image": 'beats_flex.jpg',
    "name": 'Beats Flex',
    "brand": 'Beats',
    "price": 69.00,
    "quantity": 2,
    "total_price": 138.00
}}

productDict4 = {"4": {
    "image": 'steelseries_arctis_gamebuds.jpg',
    "name": 'Artics gaming',
    "brand": 'Steelseries',
    "price": 159.00,
    "quantity": 1,
    "total_price": 159.00
}}

productsOrder2 = productDict3
productsOrder2 = MagerDicts(productsOrder2, productDict4)


def getorder1M():
    return order1


def getorder2M():
    return order2


def getorder1prodM():
    return productsOrder1


def getorder2prodM():
    return productsOrder2





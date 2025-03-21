from backend_model.profileModel import MagerDicts

# ORDER 1
# ------------------------------------------------------------
#
orderDict1 = {"1": {
    "tracking_num": "71287249",
    "order_date": "01/18/23",
    "arrival_date": "01/18/23",
    "address_line_1": "Plaza del Mar Calle Estrella 1039",
    "address_line_2": "Cabo Rojo Puerto Rico, 00623",
    "total": 129.00,
    "payment_method": "Mastercard",
    'status': 'Delivered'
}}

# ORDER 2
# ------------------------------------------------------------
#
orderDict2 = {'2': {
    "tracking_num": "71287250",
    "order_date": "02/28/23",
    "arrival_date": "03/05/23",
    "address_line_1": "Urb Los Pinos calle sol M-3",
    "address_line_2": "Arecibo Puerto Rico, 00612",
    "total": 499.97,
    "payment_method": "Mastercard",
    'status': 'Delivered'

}}

# ORDER 3
# ------------------------------------------------------------
#
orderDict3 = {'3': {
    "tracking_num": "71287251",
    "order_date": "06/17/23",
    "arrival_date": "06/30/23",
    "address_line_1": "Calle Tortola Estancias de la sabana K-10",
    "address_line_2": "San Juan Puerto Rico, 00901",
    "total": 799.00,
    "payment_method": "Mastercard",
    'status': 'Processed'
}}

# ORDER 4
# ------------------------------------------------------------
#
orderDict4 = {'4': {
    "tracking_num": "71287252",
    "order_date": "06/19/23",
    "arrival_date": "06/30/23",
    "address_line_1": "Visas del Mar H-9",
    "address_line_2": "Quebradillas Puerto Rico, 00614",
    "total": 609.97,
    "payment_method": "Mastercard",
    'status': 'Shipped'
}}



# PRODUCTS
# ------------------------------------------------------------
productDict1 = {"1": {
    "image": 'imagenes_audifonos/apple/apple_airpods_4.jpg',
    "name": 'Airpods 4',
    "brand": 'Apple',
    "price": 129.00,
    "quantity": 1,
    "total_price": 129.00,
    "order_id": '1'
}}

productDict2 = {"2": {
    "image": 'imagenes_audifonos/corsair/corsair_hs80_rgb.jpg',
    "name": 'HS80 RGB',
    "brand": 'Corsair',
    "price": 149.99,
    "quantity": 2,
    "total_price": 299.98,
    "order_id": '2'
}}

productDict3 = {"3": {
    "image": 'imagenes_audifonos/razer/razer_kraken_v4_pro.jpg',
    "name": 'Kraken V4 Pro',
    "brand": 'Razer',
    "price": 399.99,
    "quantity": 2,
    "total_price": 799.98,
    "order_id": '3'
}}

productDict4 = {"4": {
    "image": 'imagenes_audifonos/razer/razer_barracuda_chroma.jpg',
    "name": 'Barracuda Chroma',
    "brand": 'Razer',
    "price": 129.99,
    "quantity": 2,
    "total_price": 259.98,
    "order_id": '4'
}}



productDict5 = {"5": {
    "image": 'imagenes_audifonos/steelseries/steelseries_arctis_nova_pro.jpg',
    "name": 'Arctis Nova Pro',
    "brand": 'Steelseries',
    "price": 349.99,
    "quantity": 1,
    "total_price": 349.99,
    "order_id": '4'
}}

productDict6 = {"6": {
    "image": 'imagenes_audifonos/beats/beats_solo_4.jpg',
    "name": 'Solo 4',
    "brand": 'Beats',
    "price": 199.99,
    "quantity": 1,
    "total_price": 199.99,
    "order_id": '2'
}}


ordersList = MagerDicts(orderDict1, orderDict2)
ordersList = MagerDicts(ordersList, orderDict3)
ordersList = MagerDicts(ordersList, orderDict4)

productsList = MagerDicts(productDict1, productDict2)
productsList = MagerDicts(productsList, productDict3)
productsList = MagerDicts(productsList, productDict4)
productsList = MagerDicts(productsList, productDict5)
productsList = MagerDicts(productsList, productDict6)


def ordersModel():
    return ordersList


def getordermodel(ID):
    for key, order in ordersList.items():
        if key == ID:
            return order


def getorderproductsmodel(ID):
    returnList = {}
    num = 1
    for key, product in productsList.items():
        if product["order_id"] == ID:
            if returnList == {}:
                returnList = {'1': product}
            else:
                num += 1
                returnList = MagerDicts(returnList, {str(num): product})
    print(returnList)
    return returnList





from frontend_model.cartModel import *

def getCart():
    # Go to cartModel to get cart items and session variables: total and quantity
    if 'amount' not in session:
        session['amount'] = 0
    if 'total' not in session:
        session['total'] = 0
    return getCartModel()


def addCartController(p_id, name, image, price, stock, quantity, total, desc, brand, connectivity, earplacement):
    # Receive the variables that we got from POST originally and save in a dictItem to add to session cart
    # The add happens over at the cartModel
    dictitems = {p_id: {'name': name, 'image': image, 'price': price, 'quantity': quantity,
                        'total_price': total, 'stock': stock, 'desc': desc, 'brand':brand, 'connectivity':connectivity,
                        'earplacement':earplacement}}
    return addCartModel(dictitems)


def deleteCartItem(p_id):
    return deleteCartItemModel(p_id)
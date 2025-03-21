from flask import url_for, redirect

from frontend_model.checkoutModel import *


def validateUserCheckout():
    # Find the user in DB via checkoutModel function
    user = validateUserModel()

    for u in user:
        # Check if a specific part is empty/null/0/etc and save the appropriate message to send back to checkout
        # Checkout will display an error message according to the variable 'message' if some info is missing
        # Otherwise, it will proceed to invoice
        if u['phone_number'] == 0 or u['phone_number'] is 'NULL':
            message = "number"
            return redirect(url_for('checkout', message=message))
        else:
            return redirect("/invoice")
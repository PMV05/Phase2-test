from flask import url_for, redirect

from frontend_model.checkoutModel import *


# def validateUserCheckout():
#     # Find the user in DB via checkoutModel function
#     user = validateUserModel()

#     for u in user:
#         # Check if a specific part is empty/null/0/etc and save the appropriate message to send back to checkout
#         # Checkout will display an error message according to the variable 'message' if some info is missing
#         # Otherwise, it will proceed to invoice
#         if u['phone_number'] == 0 or u['phone_number'] is 'NULL':
#             message = "number"
#             return redirect(url_for('checkout', message=message))
#         else:
#             return redirect("/invoice")
        
       
def validateUserCheckout():
    # Find the user in DB via checkoutModel function
    user = validateUserModel()

    # Check if user is empty (in case there are no users)
    if not user:
        message = "user_not_found"
        return redirect(url_for('checkout', message=message))

    # Assuming the user is a list with one user dictionary (or just a single dictionary)
    u = user[0]  # Get the first user, or modify based on your data structure

    # Check if phone_number is missing or invalid
    if u.get('phone_number') in [None, 0, 'NULL']:
        message = "number"
        return redirect(url_for('checkout', message=message))
    
    # Otherwise, proceed to invoice
    return redirect("/invoice")
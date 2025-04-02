from functools import wraps # TODO:
from datetime import datetime
# TODO:
import pymysql
from flask import Flask, render_template, redirect, request, session
from frontend_controller.cartController import *
from frontend_controller.checkoutController import *
from frontend_controller.invoiceController import *
from frontend_controller.loginController import *
from frontend_controller.ordersController import *
from frontend_controller.profileController import *
from frontend_controller.shopController import *

app = Flask(__name__, template_folder='frontend/')
app.secret_key = 'akeythatissecret'

# In this template, you will usually find functions with comments tying them to a specific controller
# main.py accesses the frontend folders
# Every controller accesses its relevant model and will send the information back to this Flask app
# TODO:
def login_required(f):
    # This function is utilized to determine whether the user is logged in and can access the routes where
    # this function is added (such as checkout, profile, invoice, orders)
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'customer' not in session:
            session['request'] = request.url
            return redirect(url_for('enterpage', message='mustlogin'))  # Redirect to login page if session variable is not set
        return f(*args, **kwargs)
    return decorated_function

@app.route("/", defaults={'message': None})
@app.route("/<message>")
def enterpage(message):
    if message is None:
        return redirect("/shop")
    elif message == 'enter':
        return render_template('log.html', message=None)  # No enviar mensaje
    elif message == 'wrong':
        return render_template('log.html', message='Login credentials are incorrect. Please try again.')
    else:
        return render_template('log.html', message=None)


@app.route("/change")
def change():
    # An optional function for students to hash a specific password
    # changePass function can be found in profileController
    # Access this function by typing the word 'change' after your Flask url
    # http://127.0.0.1:5000/change
    changePass()
    return render_template("log.html")

# TODO:
@app.route("/clear")
def clear():
    # Whenever you wish to log out or clear the session info, you can type /clear at the end of the Flask address
    if 'customer' in session:
        session.pop('customer')

    if 'request' in session:
        session.pop('request')

    return redirect("/")


@app.route("/login", methods=['POST'])
def login():
    # Enters here when logging in
    email = request.form.get('email')
    passcode = request.form.get('password')
    # Receive your login information and send to the loginController's logincontroller()
    return logincontroller(email=email, password=passcode)

# TODO:
@app.route("/register/", defaults={'message': None})
@app.route('/register/<message>')
def register(message):
    # TODO: TO BE CONNECTED TO MYSQL BY STUDENTS
    # Redirects to register page

    # First must verify if user is already in DB, if not, then proceed with register

    # Example of an INSERT query:
    # INSERT
    # INTO
    # Customers(CustomerName, ContactName, Address, City, PostalCode, Country)
    # VALUES('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');

    # Also worth pointing out, password must be hashed before adding to DB:
    # sha256_crypt.encrypt(unhashed_password_here)
    # This is the example of hashing I utilize, but there are many forms of using hashing/encryption of passwords
    # Redirects to register page
    return render_template('register.html', message=message)


# TODO: VERIFICAR LO QUE HAY EN EL TEMPLATE DE LA PROFESORA
@app.route("/registerinfo", methods=['POST'])
def registerinfo():
    # TO BE ADDED BY STUDENTS
    # Processs the register info
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    pass1 = request.form.get('pass1')
    pass2 = request.form.get('pass2')

    # logincontroller.py -> registercontroller(_)
    routeName = registercontroller(fname, lname, email, pass1, pass2)

    return redirect(routeName)


@app.route("/shop")
def shop():
    # This is the shop's Flask portion
    # First we receive the list of products by accessing getProducts() from shopController
    products = getProducts()

    db = Dbconnect()
    params = []
    query = "SELECT * FROM product WHERE p_status = 'active' "

    # Filtro para la búsqueda por nombre
    searchQuery = request.args.get('search')
    if searchQuery:
        query += " AND (LOWER(p_name) LIKE %s OR LOWER(p_brand) LIKE %s) "
        params.append(f"%{searchQuery.lower()}%")
        params.append(f"%{searchQuery.lower()}%")

    # Filtro para la marca
    brandsSelected = request.args.getlist('brands')
    if(brandsSelected):
        numberBrands = ', '.join(['%s'] * len(brandsSelected)) 
        query += f"and p_brand IN ({numberBrands})"
        params.extend(brandsSelected)

    # Filtro para el color
    colorsSelected = request.args.getlist('color-types')
    if(request.args.getlist('color-types')):
        numberColors = ', '.join(['%s'] * len(colorsSelected)) 
        query += f"and p_color IN ({numberColors}) "
        params.extend(colorsSelected)

    # Filtro para el tipo de modelo
    modelsSelected = request.args.getlist('modelType')
    if(request.args.getlist('modelType')):
        numberModels = ', '.join(['%s'] * len(modelsSelected)) 
        query += f"and p_model_type IN ({numberModels}) "
        params.extend(modelsSelected)

    # Filtro para la conecetividad
    connectivitySelected = request.args.getlist('connectivity')
    if(request.args.getlist('connectivity')):
        numberConnectivity = ', '.join(['%s'] * len(connectivitySelected)) 
        query += f"and p_connectivity IN ({numberConnectivity})"
        params.extend(connectivitySelected)

    # Filtro para el ajuste de oreja
    placementSelected = request.args.getlist('earPlacement')
    if(request.args.getlist('earPlacement')):
        numberPlacement = ', '.join(['%s'] * len(placementSelected)) 
        query += f"and p_earplacement IN ({numberPlacement}) "
        params.extend(placementSelected)

    # Filtro para el orden ascendente
    sortingSelected = request.args.getlist('sortings')
    orderSelected = request.args.get('sort-order')

    if(sortingSelected and orderSelected):
        query += f" order By {', '.join(sortingSelected)} "
        if(orderSelected == 'descending'):   
            query += " DESC"

    products = db.select(query, params)

    # Then we create the shopping cart by accessing getCart in shopController
    getCart()

    # Find the different filter options for the products by accessing the functions from shopController
    # TODO: FILTERS TO BE CONNECTED TO MYSQL BY STUDENTS
    brands = getBrands()
    colors = getColors()
    modelType = getTypeModel()
    connectivity = getConnectivityModel()
    earPlacement = getEarPlacement()

    # Redirect to shop page with the variables used
    return render_template("shop-4column.html", products=products, brands=brands,
                           colors=colors, modelType=modelType, connectivity=connectivity, earPlacement=earPlacement,
                           brandsSelected=brandsSelected, colorsSelected=colorsSelected, modelsSelected=modelsSelected,
                           connectivitySelected=connectivitySelected, placementSelected=placementSelected,
                           sortingSelected=sortingSelected, orderSelected=orderSelected)

@app.route('/profile')
@login_required
def profile():
    if 'customer' not in session:
        return redirect(url_for('enterpage', message='enter'))

    db = Dbconnect()
    cursor = db.connection.cursor(pymysql.cursors.DictCursor)

    query = """
    SELECT 
        c.c_first_name AS first_name, 
        c.c_last_name AS last_name, 
        c.c_email AS email, 
        c.c_phone_number,
        a.ad_street AS street,
        a.ad_city AS city,
        a.ad_state AS state,
        a.ad_postal_code AS postal_code,
        pm.payment_email
    FROM customer c
    LEFT JOIN address a ON c.customer_ID = a.customer_ID
    LEFT JOIN payment_method pm ON c.customer_ID = pm.customer_ID
    WHERE c.customer_ID = %s
"""




    print("CUSTOMER ID:", session.get('customer'))

    cursor.execute(query, (session['customer'],))
    user = cursor.fetchone()

    if user is None:
        return render_template("profile.html", user=[], num="No disponible")

    return render_template("profile.html", user=[user], num=user['c_phone_number'])

# TODO:
@app.route("/addinfo", methods=["POST"])
def addinfo():
    postType = request.form.get('postType')

    if postType == 'addaddress':
        street = request.form.get('street')
        state = request.form.get('state')
        postal_code = request.form.get('postal_code')
        city = request.form.get('city')
        addaddresscontroller(street, state, postal_code, city)

    elif postType == 'addpayment':
        payment_email = request.form.get('payment_email')
        payment_postal_code = request.form.get('payment_postal_code')
        customer_ID = request.form.get('customer_ID')
        addpaymentcontroller(payment_email, payment_postal_code, customer_ID)
    return redirect(request.referrer)

# TODO:
@app.route("/editinfo", methods=["POST"])
def editinfo():

        if  request.form.get('number'):
            number = request.form['number']
            editnumbercontroller(number)
            return redirect("/profile")

        elif request.form.get('street') and request.form.get('city') and request.form.get('state') and request.form.get('postal_code'):
            street = request.form['street']
            city = request.form['city']
            state = request.form['state']
            postal_code = request.form['postal_code']
            # address_id = request.form.get('address_id')
            editaddresscontroller(street, city, state, postal_code)
            return redirect("/profile")

        elif request.form.get('paypal_email'):
            paypal_email = request.form['paypal_email']
            editpaymentcontroller(paypal_email)
            return redirect("/profile")

        elif all(request.form.get(k) for k in ['fname', 'lname', 'email']):
            fname = request.form['fname']
            lname = request.form['lname']
            email = request.form['email']
            editprofilecontroller(fname, lname, email)
            return redirect("/profile")

        return redirect(request.referrer)

@app.route("/password", methods=["GET", "POST"])
def password():
    user = getUser()

    if request.method == "GET":  # si se le da a reset change password en el perfil
        return render_template("change-password.html")  # te lleva a la página

    if request.method == "POST":  # si se hace submit al form de change password
        # pass_o, pass_n y pass_n1 es como están en change-password.html
        old_pass = request.form['pass_o']
        new_pass = request.form['pass_n']
        confirm_new_pass = request.form['pass_n1']

        if new_pass != confirm_new_pass:
            return "Passwords must match"

        # se guarda el current pass
        current_pass = user[0]['password']  # aquí se pone ['password'] y no ['pass']

        # se verifica si el pass viejo es el correcto
        if not sha256_crypt.verify(old_pass, current_pass):
            return "Incorrect old password"

        changePass(user[0]['email'], new_pass)  # toma el primer user que se encontró

        return redirect("/profile")


@app.route("/reset-password")
def resetpasswordpage():
    return render_template("reset-password.html")


# TODO:
from passlib.hash import sha256_crypt

@app.route("/resetpassword", methods=["POST"])
def resetpassword():
    email = request.form.get('email')
    newpass1 = request.form.get('newpass1')
    newpass2 = request.form.get('newpass2')

    if newpass1 != newpass2:
        return render_template('reset-password.html', message="Passwords do not match.")

    db = Dbconnect()
    
    # Verificar si el email existe
    result = db.select("SELECT * FROM customer WHERE c_email = %s", (email,))
    if not result:
        return render_template('reset-password.html', message="Email not found.")

    # Hashear nueva contraseña
    hashed_pass = sha256_crypt.encrypt(newpass1)

    # Actualizar en la base de datos
    db.execute("UPDATE customer SET c_password = %s WHERE c_email = %s", (hashed_pass, email))

    return redirect("/enter")


@app.route("/orders")
def orders():
    # TODO: TO BE CONNECTED TO MYSQL BY STUDENTS
    # Redirects us to the orders list page of the user
    # Fetches each order and its products from ordersController
    order1 = getorder1()
    products1 = getorder1products()
    order2 = getorder2()
    products2 = getorder2products()

    return render_template("orderlist.html", order1=order1, products1=products1, order2=order2, products2=products2)

# TODO:
@app.route("/addcart", methods=["POST"])
def addcart():
    # Get the relevant info for product to add to cart
    p_id = request.form.get('p_id')
    name = request.form.get('name')
    image = request.form.get('image')
    price = request.form.get('price')
    quantity = request.form.get('quantity')
    stock = request.form.get('stock')
    desc = request.form.get('desc')
    brand = request.form.get('brand')
    connectivity=request.form.get('connectivity')
    earplacement=request.form.get('earplacement')

    total = float(price) * int(quantity)
    # Find the add cart function in cartController
    addCartController(p_id, name, image, price, stock, quantity, total,desc, brand, connectivity,earplacement)
    # request.referrer means you will be redirected to the current page you were in
    return redirect("/shop")


@app.route("/delete", methods=["POST"])
def delete():
    p_id = request.form.get('p_id')

    deleteCartItem(p_id)

    return redirect(request.referrer)


# TODO: TO BE ADDED BY STUDENTS (Editing the session variable cart)
@app.route("/editcart", methods=["POST"])
def editcart():

    p_id = request.form.get('p_id')
    new_quantity = int(request.form.get('quantity', 1))
    
    # Ensure cart exists in session
    if 'cart' not in session or session['cart'] is None:
        return redirect(request.referrer)
    
    # Check if the product exists in the cart
    if p_id in session['cart']:
        item = session['cart'][p_id] #Fin the product that is in the cart
        
        # Makes sure that the new quantity doesn't exceed stock
        if new_quantity <= int(item['stock']):
            item['quantity'] = new_quantity
            item['total_price'] = float(new_quantity) * float(item['price'])

        else:
            # If the quantity the user entered exceeds the stock, set to max stock
            item['quantity'] = int(item['stock'])
            item['total_price'] = float(item['stock']) * float(item['price'])
        
        session['amount'] = 0
        session['total'] = 0

        for key, cart_item in session['cart'].items():
            session['amount'] += int(cart_item['quantity'])
            session['total'] += float(cart_item['total_price'])
        
        # Makes sure that the changes are save
        session.modified = True
    
    return redirect(request.referrer)
@app.route('/delete-cart-item/<int:product_id>', methods=['POST'])
def delete_cart_item(product_id):
    if 'cart' in session and str(product_id) in session['cart']:
        session['cart'].pop(str(product_id))  
        session.modified = True  

    return redirect(url_for('checkout'))  # Refresh checkout page

@app.route('/edit-checkout-item/<int:product_id>', methods=['POST'])
def edit_checkout_item(product_id):
    update_quantity = int(request.form.get('quantity'))
    key = str(product_id)
    
    if 'cart' in session and key in session['cart']:
        if update_quantity > 0:
            session['cart'][key]['quantity'] = update_quantity
            # Update the total price by converting price to a float
            session['cart'][key]['total_price'] = update_quantity * float(session['cart'][key]['price'])
        else:
            session['cart'].pop(key)
        session.modified = True
    
    return redirect(url_for('checkout'))


@app.route("/checkout")
def checkout():
    if 'customer' in session:
        user = getUserCheckout()
        
        # Imprimir para depurar el valor de user TODO: VERIFICAR!!!
        print(user)  # Añadir esta línea para verificar la estructura de user  TODO: VERIFICAR!!!
        
        total = 0.0
        
        # Asegurarse de que user tiene al menos 11 elementos (índice 10) 
        if len(user) > 10:
            # Formatear el número de teléfono si el índice 10 existe
            num = '{:03d}-{:03d}-{:04d}'.format(
                int(str(user[10])[:3]),
                int(str(user[10])[3:6]),
                int(str(user[10])[6:])
            )
        else:
            num = "Número no disponible"
    
        # Calcular el total del carrito
        for key, item in session['cart'].items():
            total += float(item['total_price'])
        
        return render_template("checkout.html", user1=user, num=num, total=total)

    else:
        session['checkout'] = True
        return redirect("/wrong")


@app.route("/invoice")
def invoice():
    # TODO: TO BE CONNECTED TO MYSQL BY STUDENTS
    # > invoiceController
    order = getOrder()
    products = getOrderProducts()
    # Total amount of items in this simulated order:
    amount = 3
    return render_template("invoice.html", order=order, products=products, amount=amount)


# @app.route("/filter")
# def filter():
#     # filter happens here
#     # not in function currently
#     return redirect("/shop")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
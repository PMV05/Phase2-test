import pymysql
from frontend_model.connectDB import *

#TODO: VER EL CODIGO DE LA PROFE

def getProductsModel():
    db = Dbconnect()
    query = "SELECT * FROM product  WHERE p_status = 'active';"
    productList = db.select(query)
    return productList 


# Filtro para las marcas de los audifonos
def getBrandsModel():
    # Simulating grabbing these filters via SQL from the database
    db = Dbconnect()
    query = ("SELECT DISTINCT p_brand "
             "FROM product "
             "WHERE p_status = 'active'"
             "ORDER BY p_brand;")
    brands = db.select(query)
    return brands

# Filtro para el color
def getColorsModel():
    db = Dbconnect()
    query = ("SELECT DISTINCT p_color "
             "FROM product "
             "WHERE p_status = 'active'"
             "ORDER BY p_color;")
    colors = db.select(query)
    return colors

# Filtro para el tipo de modelo
def getTypeModel():
    db = Dbconnect()
    query = ("SELECT DISTINCT p_model_type "
             "FROM product "
             "WHERE p_status = 'active'"
             "ORDER BY p_model_type;")
    modelType = db.select(query)
    return modelType

# Filtro para el tipo de conectividad
def getConnectivityModel():
    db = Dbconnect()
    query = ("SELECT DISTINCT p_connectivity "
             "FROM product "
             "WHERE p_status = 'active'"
             "ORDER BY p_connectivity;")
    connectivity = db.select(query)
    return connectivity

# Filtro para el tipo de ajuste
def getEarPlacementModel():
    db = Dbconnect()
    query = ("SELECT DISTINCT p_earplacement "
             "FROM product "
             "WHERE p_status = 'active';")
    earPlacement = db.select(query)
    return earPlacement

def searchProductsModel(searchQuery):
    db = Dbconnect()
    query = "SELECT * FROM product WHERE p_status = 'active' AND p_name LIKE %s"
    params = [f"%{searchQuery}%"]
    results = db.select(query, params)

    productList = []
    for res in results:
        productList.append({
            "id": res['product_ID'],
            "name": res['p_name'],
            "brand": res['p_brand'],
            "model_type": res['p_model_type'],
            "color": res['p_color'],
            "price": res['p_price'],
            "cost": res['p_cost'],
            "connectivity": res['p_connectivity'],
            "battery": res['p_battery'],
            "earplacement": res['p_earplacement'],
            "quantity": res['p_quantity'],
            "description": res['p_description'],
            "image": res['p_image'],
            "status": res['p_status']
        })
    return productList

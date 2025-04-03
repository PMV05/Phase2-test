import pymysql 
from frontend_model.connectDB import *

#TODO:
# getProductsModel crea una instancia para establecer una conceccion con la base de datos.
# Seleccionamos todos los productos de la tabla productos, que en el estatus aparezca como activo.
# Utilizamos el metodo seleccionado y lo guardamos en la variable de productList.
# Devuelve la lista de productos activos obtenidos de la base de datos.
def getProductsModel():
    db = Dbconnect()
    query = "SELECT * FROM product  WHERE p_status = 'active';"
    productList = db.select(query)
    return productList 


# Filtro para las marcas de los audifonos
# getBrandsModel crea una instancia para establecer una conceccion con la base de datos.
# Seleccionamos diferentes productos de la tabla product que aparezcan como activos, nos aseguramos que solo tengan marcas unicas.
# Ordenamos los brandas de forma acendente.
# Utilizamos el metodo seleccionado y lo guardamos en la variable de brands.
# Devuelve la lista de marcas de productos activos obtenidos de la base de datos.
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
# getColorsModel crea una instancia para establecer una conceccion con la base de datos.
# Seleccionamos todos los colores de los productos.
# Utilizamos el metodo seleccionado y lo guardamos en la variable de colors.
# Ordenamos los colores de forma acendente.
# Utilizamos el metodo seleccionado y lo guardamos en la variable de colors.
# Devuelve la lista de colores de productos activos obtenidos de la base de datos.
def getColorsModel():
    db = Dbconnect()
    query = ("SELECT DISTINCT p_color "
            "FROM product "
            "WHERE p_status = 'active'"
            "ORDER BY p_color;")
    colors = db.select(query)
    return colors

# Filtro para el tipo de modelo
# getTypeModel crea una instancia para establecer una conceccion con la base de datos.
# Seleccionamos todos los tipos de modelos de la tabla productos.
# Ordenamos todos los modemos de forma acendente.
# Utilizamos el metodo seleccionado y lo guardamos en la variable de .
# Devuelve la lista de tipos de modelos de productos activos obtenidos de la base de datos.
def getTypeModel():
    db = Dbconnect()
    query = ("SELECT DISTINCT p_model_type "
            "FROM product "
            "WHERE p_status = 'active'"
            "ORDER BY p_model_type;")
    modelType = db.select(query)
    return modelType

# Filtro para el tipo de conectividad
# getConnectivityModel crea una instancia para establecer una conceccion con la base de datos.
# Verifica la concectividad de los productos seleccionados de la tabla product que su estatus aparece activo.
# Ordenamos el tipo de conectividad de manera acendente.
# Devuelve la lista de tipos de conectividad de productos activos obtenidos de la base de datos.
def getConnectivityModel():
    db = Dbconnect()
    query = ("SELECT DISTINCT p_connectivity "
            "FROM product "
            "WHERE p_status = 'active'"
            "ORDER BY p_connectivity;")
    connectivity = db.select(query)
    return connectivity

# Filtro para el tipo de ajuste
# getEarPlaceModel crea una instancia para establecer una conceccion con la base de datos.
# Seleciona de la tabla de porduct todos lo audifonos dependiendo de la colocacion de la oreja. 
# Seleccionamos todos lo los productos que su estado aparece como activo.
# Devuelve la lista de tipos de colocación en el oído de productos activos obtenidos de la base de datos.
def getEarPlacementModel():
    db = Dbconnect()
    query = ("SELECT DISTINCT p_earplacement "
            "FROM product "
            "WHERE p_status = 'active';")
    earPlacement = db.select(query)
    return earPlacement



# Selecciona todos los producto relacionados al nombre entrados por el usuario.
# searchProductsModel crea una instancia para establecer una conceccion con la base de datos.
# Devuelve la lista 'productList' que contiene todos los productos activos que coinciden con la búsqueda.
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

from frontend_model.shopModel import *
# TODO:

def getProducts():
    products = getProductsModel()
    return products


def getBrands():
    return getBrandsModel()


def getColors():
    return getColorsModel()

# TODO:
def getEarPlacement():
    return getEarPlacementModel()

# TODO:
def getConnectivity():
    return getConnectivityModel()

# Search function connected to Model
def searchProducts(searchQuery):
    return searchProductsModel(searchQuery)
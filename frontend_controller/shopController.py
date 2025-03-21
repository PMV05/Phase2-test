from frontend_model.shopModel import *


def getProducts():
    products = getProductsModel()
    return products


def getBrands():
    return getBrandsModel()


def getColors():
    return getColorsModel()

# TODO:
def getVideoRes():
    return getVideoResModel()

# TODO:
def getWifi():
    return getWifiModel()
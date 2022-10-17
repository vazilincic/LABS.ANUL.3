from water import Water
from juice import Juice
from softDrink import SoftDrink

def product_originary(products: list):
    for product in Products:
        print(product.get_originary())

def product_description(products: list):
    for product in products:
        print(product.get_name(), product.get_quality())

products = [
    Water('Gura Cainarului'),
    Juice('Naturalis'),
    SoftDrink('CocaCola'),
]

# product_originary(products)
 product_description(products)

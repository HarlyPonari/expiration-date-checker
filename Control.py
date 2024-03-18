# Description: This file contains the control functions for the program.
import pickle
import Product as pd
from datetime import datetime as dt

def checkExpiration(product):
  if product.isExpired():
    # This should both print this and return this object
    print(product.getName(),":", product.getId(), " is expired")
    
    # This is so that the program will have a refrence to the expired product and could then remove it from the list
    return product

def saveProducts(products):
  with open("data/products.pk1", "wb") as file: 
    pickle.dump(products, file)

def loadProducts():
  with open("data/products.pk1", "rb") as file:
    products = pickle.load(file)
    return products

def editProduct(products, _id):
  for p in products:
    if p.getID() == _id:
      newP = InitializeProduct(p.getName())
      # Now we must remove the old product and add the new one
      p = newP
      return products


# When the data is sorted, we should alsdo check if the product is expired, or if it is out of items based on the time passed.
def sortProducts(products):
  for p in products:
    for p2 in products:
      if p.getDate() > p2.getDate():
        temp = p
        products[products.index(p)] = p2
        products[products.index(p2)] = temp

  return products

def InitializeProduct(product_name = "Omnipod 5"):

  print("Enter the expirary date of the", product_name, "(month/day/year including any zeros)")
  inDate = input()
  try: 
    inDate = dt.strptime(inDate, "%m/%d/%Y")
  except ValueError:
    print("Error: Please follow the format of MM/DD/YYYY including any zeros (05/05/2002)")
 
  print("Enter the ID of the", product_name)
  _id = input()
  try: 
    _id = int(_id)
  except ValueError:
    print("Error: Please enter a valid ID (integer format)")

  print("Changes will not be saved until you select the quit option")

  return pd.Product(_id, product_name, inDate)



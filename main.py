from datetime import datetime as dt

# For data serialization
import pickle

import json

import Control as ct
from enum import Enum

class Choice(Enum):
  Quit = 5
  CreateProduct = 1
  ReadList = 2
  Sort = 3
  Edit = 4


# def choiceOne():
  # This function should be first take in an ID and then the expiration date of the product.
  # Then it should add the object to the current list of products
  

def main():
  products = []
  
  changes = False 
  shouldClose = False
  # try:
  #   products.append(loadProducts()) 
  # except:
  #   print("Error couldn't load the file")
   
  while not shouldClose:
    choice = input("1: Create product\n2: Read list\n3: Sort\n4: Edit a product\n5: Quit\n")
    try:
      choice = int(choice)
 
    except TypeError:
      print(choice, "was not a valid choice")
    
    # Quitting the program
    if choice == Choice.Quit.value:
      
      if changes == True:
        print("Save your changes? (y/n)")
        save = input()
        if save == "y" or save == "Y":
          ct.saveProducts(products)
        else:
          print("Changes were not saved")
        
      shouldClose = True 

    # Creating a product
    elif choice == Choice.CreateProduct.value:
      products.append(ct.InitializeProduct())
      changes = True
      # ct.saveProducts(products)
    
    # Reading the product list
    elif choice == Choice.ReadList.value:
      products = ct.loadProducts()
      for p in products:
        print(p.__str__())

    # Editing the product
    elif choice == Choice.Edit.value:
      print("Enter the ID of the product you want to edit")
      _id = input()
      try:
        _id = int(_id)
        products = ct.loadProducts() 
      except ValueError:
        print("Error: Please enter a valid ID (integer format)")         
      for p in products:
        if p.getID() == _id:
          newP = ct.InitializeProduct()
          # Now we must change the object data inside of the list
          products[products.index(p)] = newP
          changes = True

    # Sorting the product list
    elif choice == Choice.Sort.value:
      products = ct.loadProducts()
      products = ct.sortProducts(products)
      ct.saveProducts(products)
      for p in products:
        print(p.__str__())


main() 


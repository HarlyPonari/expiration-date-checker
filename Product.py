import pickle
from datetime import datetime as dt

class Product:
  def __init__(self, _id, name, expDate):
    self.name = name
    self._id = _id
    self.expDate = expDate

  def getDate(self):
    return self.expDate

  def getName(self):
    return self.name
  
  def getID(self):
    return self._id
  
  def __str__(self):
    return f"{self._id}: {self.name} expires on {self.expDate}"

  def isExpired(self):
    return dt.now() > self.expDate   

  
  
  
  
  
  

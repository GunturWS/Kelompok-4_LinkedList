class Node:
  def __init__(self, value):
    self.__value = value
    self.__next = None
    self.__prev = None
  def setValue(self, value):
    self.__value = value
  def setNext(self, next):
    self.__next = next
  def setPrev(selv, prev):
    self.__prev = prev
  def getValue(self):
    return self.__value
  def getNext(self):
    return self.__next
  def getPrev(self):
    return self.__prev
  
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

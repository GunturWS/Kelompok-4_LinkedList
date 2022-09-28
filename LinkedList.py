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
   
  def add_end(self, value):
    new_node = Node(value)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      n = self.head
      while n.getNext() != None:
        n = n.getNext()
      n.setNext(new_node)
      self.tail = new_node
    self.length+=1
    
  def add_begin(self, value):
    new_node = Node(value)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.setNext(self.head)
      self.head.setPrev(new_node)
      self.head = new_node
    self.length+=1
    
  def

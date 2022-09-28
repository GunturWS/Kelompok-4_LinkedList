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
    
  #Method untuk menyisipkan node pada indeks tertentu
  def insert(self,value,index):
    if index ==   0:
      self.add_begin(value):
        else:
          count=1
          n=self.head
          new_node=Node(value)
          while count<index and n!=None
              n=n.getNext()
              count+=1
          if n == None:
              print("index yang dimasukkan melebihi panjang LinkedList")
          elif n.getNext() != None:
              new_node.setNext(n.getNext())
              n.getNext().setPrev(new_node)
              n.setNext(new_node)
              new_node.setPrev(n)
          else:
              new_node.setNext(n.getNext())
              n.setNext(new_node)
              new_node.setPrev(n)
              self.tail = new_node
         self.length+=1
    
    # Method untuk menampilkan nilai dari Node yang ada di linked list
    def printLL(self):
        n = self.head
        while n != None:
            print(n.getValue(), "-->", end=" ")
            n = n.getNext()
        print("None")
        
    # Method untuk mendapatkan Node pada indeks tertentu
    def getLL(self, index):
        if index == 0:
            return self.head.getValue()
        else:
            count=1
            n=self.head
            while count<index and n!=None:
                n=n.getNext()
                count+=1
            if n.getNext() == None:
                print("index yang dimaksud tidak ada")
            else:
                return n.getNext().getValue()
          

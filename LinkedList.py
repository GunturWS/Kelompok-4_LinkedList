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
    
    # Method untuk menghapus Node berdasarkan indeks
    def remove(self, index):
        if index == 0:
            self.head = self.head.getNext()
        else:
            count=1
            n=self.head
            while count<index and n!=None:
                n=n.getNext()
                count+=1
            if n == None or n.getNext() == None:
                print("index yang dimasukkan harus kurang dari panjang LinkedList")
            elif n.getNext().getNext() != None:
                n.getNext().getNext().setPrev(n)
                n.setNext(n.getNext().getNext())
            else:
                n.setNext(n.getNext().getNext())
                self.tail = n
        self.length-=1

    # Method untuk menghapus Node berdasarkan Value
    def removeByValue(self, value):
        if self.head == None:
            print("Tidak dapat menghapus, Linked List kosong")
            return
        if self.head.getValue() == value and self.head.getNext().getNext() == None:
            self.head = self.head.getNext()
            self.tail = self.head
            self.length-=1
            if self.tail.getValue() == value:
                self.head = None
                self.tail = None
                self.length-=1
                return
        elif self.head.getValue() == value:
            self.head = self.head.getNext()
            self.length-=1
        n = self.head
        while n.getNext() != None:
            if n.getNext().getValue() == value and n.getNext().getNext() != None:
                n.getNext().getNext().setPrev(n)
                n.setNext(n.getNext().getNext()) 
                self.length-=1
            if n.getNext().getValue() == value and n.getNext().getNext() == None:
                n.setNext(n.getNext().getNext()) 
                self.tail = n
                self.length-=1
                break
            n = n.getNext()

    # Method untuk menghapus value yang duplikat
    def removeDuplicate(self):
        n = self.head
        t = self.head.getNext()
        while n.getNext() != None:
            if n.getValue() == t.getValue():
                self.removeByValue(t.getValue())
            if t != None:
                t = t.getNext()
            if t == None:
                n = n.getNext()
                t = n.getNext()
                
    # Method untuk menukar Node
    def swap(self, index1, index2):
        if index1 >= self.length or index2 >= self.length:
            print("indeks yang dimasukkan melebihi panjang linked list")
        elif index1 == index2:
            print("tidak bisa menjalankan perintah, indeks yang dimasukkan sama")
        elif self.head.getValue() == self.getLL(index1):
                temp = self.getLL(index1)
                self.add_begin(self.getLL(index2))
                self.remove(index1+1)
                self.insert(temp, index2)
                self.remove(index2+1)
        elif self.head.getValue() == self.getLL(index2):
                temp = self.getLL(index2)
                self.add_begin(self.getLL(index1))
                self.remove(index2+1)
                self.insert(temp, index1)
                self.remove(index1+1)
        else:   
            n=self.head
            while n != None:
                    if n.getValue() == self.getLL(index1):
                            temp = self.getLL(index1)
                            self.insert(self.getLL(index2),index1)
                            self.remove(index1+1)
                            self.insert(temp,index2)
                            self.remove(index2+1)
                            break
                    elif n.getValue() == self.getLL(index2):
                            temp = self.getLL(index2)
                            self.insert(self.getLL(index1),index2)
                            self.remove(index2+1)
                            self.insert(temp,index1)
                            self.remove(index1+1)
                            break
                    n = n.getNext()

    # Method untuk mengubah Tail ke Head
    def swapHeadTail(self):
        self.swap(0,self.length-1)
       
    

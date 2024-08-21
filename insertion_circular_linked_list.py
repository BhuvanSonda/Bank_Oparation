class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Circular_linked_list:
    def __init__(self):
        self.head=None
        self.tail=None

    def displaly(self):
        temp=self.head
        #print(temp.data, "-->", end=" ")
        while temp.next != self.head:
            print(temp.data,"-->",end=" ")
            temp=temp.next
        print(temp.data, "-->", end=" ")

    def add_beging(self,data):
        if self.head is None:
            new=node(data)
            self.head= new
            self.tail=new
            self.tail.next=self.head
        else:
            new = node(data)
            new.next = self.head
            self.tail.next = new
            self.head = new

    def add_end(self,data):
        if self.head is None:
            new=node(data)
            self.head= new
            self.tail=new
            self.tail.next=self.head
        else:
            new = node(data)
            self.tail.next = new
            self.tail = new
            self.tail.next = self.head

    def add_position(self,position, data):
        if self.head is None:
            new = node(data)
            self.head = new
            self.tail = new
            self.tail.next = self.head
        else:
            new = node(data)
            temp=self.head
            for i in range(1,position-1):
                temp=temp.next
            new.next=temp.next
            temp.next=new


l=Circular_linked_list()
n1=node(20)
l.head=n1
l.tail=n1
l.tail.next=l.head
n2=node(30)
l.tail.next=n2
l.tail=n2
l.tail.next=l.head
l.add_beging(12)
l.add_beging(14)
l.add_end(100)
l.add_position(2,200)
k=1
while k:
    k=int(input("\nadd more data enter 1 (for exist enter 0) : "))
    if k ==0:
        break
    choice=int(input("where you want to add ?"
                     "\nfor beginning enter (1) :"
                     "\nfor end enter (2) : "
                     "\nfor position enter (3) :  "))
    if choice==1:
        add = int(input("enter data :"))
        l.add_beging(add)
    if choice==2:
        add = int(input("enter data :"))
        l.add_end(add)
    if choice==3:
        add = int(input("enter data :"))
        pos=int(input("enter position :"))
        l.add_position(pos,add)

    l.displaly()
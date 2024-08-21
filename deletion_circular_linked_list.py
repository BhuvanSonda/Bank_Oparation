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

    def delet_begining(self):
        temp=self.head
        self.head=temp.next
        self.tail.next=self.head

    def delete_end(self):
        temp=self.head
        while temp.next != self.tail:
            temp=temp.next
        temp.next=self.head
        self.tail= temp

    def delete_position(self,position):
        temp1=self.head
        temp2=temp1.next

        for i in range(1,position-1):
            temp2=temp2.next
            temp1=temp1.next
        temp1.next=temp2.next
        if temp2.next == self.tail:
            self.tail = temp1
        temp2.next = None




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
# l.delet_begining()
# l.delete_end()
l.delete_position(1)

l.displaly()
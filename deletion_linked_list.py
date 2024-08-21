class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Single_linked_list:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end="")
                temp = temp.next

    def insert_begining(self,data):
        new=node(data)
        new.next=self.head
        self.head=new

    def insert_end(self,data):
        new=node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        new.next=temp.next
        temp.next=new

    def insert_position(self, position, data):
        new=node(data)
        temp=self.head
        for i in range(1,position - 1):
            temp=temp.next
        new.next=temp.next
        temp.next=new

    def deletion_begining(self):
        temp=self.head
        self.head=temp.next
        temp.next=None

    def deletion_end(self):
        temp=self.head.next
        previous=self.head
        while temp.next is not None:
            temp=temp.next
            previous=previous.next
        previous.next=None

    def deletion_possition(self, position):
        temp=self.head.next
        previous=self.head
        for i in range(1,position - 1):
            temp=temp.next
            previous=previous.next
        previous.next=temp.next
        temp.next=None


l=Single_linked_list()
n1=node(14)
l.head=n1
n2=node(40)
n1.next=n2
n3=node(80)
n2.next=n3
n4=node(60)
n3.next=n4
l.insert_end(65)
l.insert_position(2,100)
#l.deletion_begining()
#l.deletion_end()
#l.deletion_possition(2)
l.display()
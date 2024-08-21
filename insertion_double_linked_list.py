class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None

class double_linked_list:
    def __init__(self):
        self.head=None

    def diplay(self):
        if self.head is None:
            print("Empty Double linked list")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<---> ",end="")
                temp=temp.next

    def insert_begining(self,data):
        new=node(data)
        temp=self.head
        temp.previous=new
        new.next=temp
        self.head=new

    def insertion_end(self,data):
        new=node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        new.previous = temp
        temp.next=new

    def insertion_position(self,position,data):
        new=node(data)
        temp=self.head
        for i in range(1,position-1):
            temp=temp.next
        new.previous=temp
        new.next=temp.next
        temp.next=new
        temp.next.previous=new


l=double_linked_list()
n1=node(10)
l.head=n1
n2=node(20)
n1.next=n2
n2.previous=n1
n3=node(30)
n2.next=n3
n3.previous=n2
l.insert_begining(25)
l.insertion_end(35)
l.insertion_position(3,45)
l.diplay()
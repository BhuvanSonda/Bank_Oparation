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

l=Circular_linked_list()
n1=node(20)
l.head=n1
l.tail=n1
l.tail.next=l.head
n2=node(30)
l.tail.next=n2
l.tail=n2
l.tail.next=l.head


l.displaly()
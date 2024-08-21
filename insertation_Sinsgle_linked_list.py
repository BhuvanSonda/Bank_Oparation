class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single_Linked_list:
    def __init__(self):
        self.head=None

    def Insertion_bigining(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new

    def Insertion_end(self,data):
        temp=self.head
        new = Node(data)
        while temp.next:
            temp=temp.next
        temp.next=new

    def Insertion_position(self,position,data):
        temp=self.head
        for i in range(1,position-1):
            temp=temp.next
        new=Node(data)
        new.next=temp.next
        temp.next=new


    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end="")
                temp=temp.next

L=single_Linked_list()
n1=Node(12)
L.head=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3

L.Insertion_bigining(25)
L.Insertion_end(60)
L.Insertion_position(2,666)
L.display()

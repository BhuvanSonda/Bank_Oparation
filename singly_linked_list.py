class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single_Linked_list:
    def __init__(self):
        self.head=None

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
#L.display()

n4=Node(52)
L.head=n4 #insert node at the begining
n4.next=n1
#

L.display()
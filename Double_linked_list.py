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

l=double_linked_list()
n1=node(10)
l.head=n1
n2=node(20)
n1.next=n2
n2.previous=n1
n3=node(30)
n2.next=n3
n3.previous=n2
l.diplay()
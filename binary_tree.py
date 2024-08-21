class node:
    def __init__(self,data):
        self.data=data
        self.right= None
        self.left=None

    def insert(self,data):
        if self.data is None:
            self.data = data
        elif data < self.data:
            if self.data is None:
                self.data=node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.data is None:
                self.right=node(data)
            else:
                self.right.insert(data)


    def inorder(node):
        if node:
            node.inorder(node.left)
            print(root.data)
            node.inorder(node.right)


print("Hello")
root=node("g")
kl=root.insert("c")
root.inorder()
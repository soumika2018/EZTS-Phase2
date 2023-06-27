class Node:
    def __init__(self,data):
        self.data=data
        self.l_child=None
        self.r_child=None
class Tree_ds:
    def __init__(self):
        self.root=None
        
        
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)
n6=Node(60)
n7=Node(70)
tree=Tree_ds()
tree.root=n1
#print(tree.root)
#print(n1)
n1.r_child=n2
n1.l_child=n3
n2.r_child=n4
n2.l_child=n5
n4.r_child=n6
n3.l_child=n7
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
print(n6)
print(n7)

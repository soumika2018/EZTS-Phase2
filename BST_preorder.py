lst=[1,2,4,5,7,4,8,3,4,5]
class Node:
    def __init__(self,data):
        self.data=data
        self.l_child=None
        self.r_child=None
class BST:
    def __init__(self,key):
        self.key=key
        self.l_child=None
        self.r_child=None
    def insert_node(self,data):
        if self.key is None:
            print("Empty")
            return
        if self.key==data:
            print("data element is already present")
            return
        if self.key>data:
            if self.l_child:
                self.l_child.insert_node(data)
            else:
                self.l_child=BST(data)
        else:
            if self.r_child:
                self.r_child.insert_node(data)
            else:
                self.r_child=BST(data)
    def pre_order(self):
        print(self.key,end=' ')
        if self.l_child:
            self.l_child.pre_order()
        if self.r_child:
            self.r_child.pre_order()
root=BST(45)        
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)
n6=Node(60)
n7=Node(70)
#tree=BST()
#tree.root=n1
#print(tree.root)
#print(n1)
n1.r_child=n2
n1.l_child=n3
n2.r_child=n4
n2.l_child=n5
n4.r_child=n6
n3.l_child=n7
'''print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
print(n6)
print(n7)'''
root.insert_node(20)
root.insert_node(30)
root.insert_node(40)
root.insert_node(22)
root.insert_node(34)
root.insert_node(64)
root.insert_node(32)
root.insert_node(76)
root.insert_node(26)
root.insert_node(55)
for i in lst:
    root.insert_node(i)
root.pre_order()

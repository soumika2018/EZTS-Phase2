class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
n1=Node("tej")
n2=Node("shashi")
n3=Node("vishnu")
n4=Node("mani")
n5=Node("harsha")
n2.next=n3
n3.prev=n2
print(n3.data)
print(n3.prev)

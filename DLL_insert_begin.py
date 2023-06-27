class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
        
    def insert_beginning(self,data):
           new_node=Node(data)
           temp=self.head
           temp.prev=new_node
           new_node.next=temp
           self.head=new_node
   
    def display(self):
        if self.head is None:
            print("doubly linked list is empty")
        else:
            temp=self.head
            while temp:
                if temp.next!=None:
                    print(temp.data,end=" <--> ")
                else:
                    print(temp.data,end="")
                temp=temp.next
     
obj=DLL()
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
n6=Node(70)
n5.next=n6
obj.display()
obj.insert_beginning(100)
print()
obj.display()

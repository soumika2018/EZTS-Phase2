# circular singly linked list 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        if self.head is None:
            print("circular linked list is empty")
        else:
            temp=self.head
            print(temp.data,'-->',end="")
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data,'-->',end="")
            print(temp.next.data)    
                
                
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)
n6=Node(60)
'''print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
print(n6)'''
obj=CLL()

obj.head=n1
obj.tail=n1
obj.tail.next=obj.head
print(obj.tail.next)
n1.next=n2
obj.tail=n2
obj.tail.next=obj.head
print(n1.next)
print(obj.tail.next)
print(n2.next)
n2.next=n3
obj.tail=n3
obj.tail.next=obj.head
print(obj.tail.next)
n3.next=n4
obj.tail=n4
obj.tail.next=obj.head
print(obj.tail.next)
n4.next=n5
obj.tail=n5
obj.tail.next=obj.head
print(obj.tail.next)
n5.next=n6
obj.tail=n6
obj.tail.next=obj.head
print(obj.tail.next)
obj.display()
print()


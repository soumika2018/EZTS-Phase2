'''you are given a circular linked list ,but you suspect that it might contain a loop.a loop occurs when a node's
next pointer points to a node that has been visited before in the traversal.your task is to write a function
detect_loop that detects if a loop exists in the circular linked list.'''
# circular singly linked list 
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_beg(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            self_tail=new_node
            self.tail.next=self.head
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=self.head
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
    def detect_loop(self):
        if self.tail.next==self.head:
            print("Loop exists")
                
n1=node(10)
n2=node(20)
n3=node(30)
n4=node(40)
n5=node(50)
n6=node(60)
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
#print(obj.tail.next)
n1.next=n2
obj.tail=n2
obj.tail.next=obj.head
#print(n1.next)
#print(obj.tail.next)
#print(n2.next)
n2.next=n3
obj.tail=n3
obj.tail.next=obj.head
#print(obj.tail.next)
n3.next=n4
obj.tail=n4
obj.tail.next=obj.head
#print(obj.tail.next)
n4.next=n5
obj.tail=n5
obj.tail.next=obj.head
#print(obj.tail.next)
n5.next=n6
obj.tail=n6
obj.tail.next=obj.head
#print(obj.tail.next)
obj.display()
#print()
obj.insert_beg(29)
obj.display()
obj.detect_loop()

            

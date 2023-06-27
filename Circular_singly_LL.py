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
            
    def insert_end(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            self.tail.next=new_node
            self.tail=new_node
            self.tail.next=self.head
            
    def insert_pos(self,pos,data):
        new_node=node(data)
        if self.head is None:
               self.head=new_node
               self_tail=new_node
               self.tail.next=self.head
        else:
            if pos==1:
                insert_beg(data)
            else:
                temp=self.head
                for i in range(1,pos-1):
                    temp=temp.next
                new_node.next=temp.next
                temp.next=new_node
                
    def delete_beg(self):
        if self.head is None:
            print("circular linked list not exists")
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
            self.tail.next=self.head
            
    def delete_end(self):
        temp1=self.head.next
        prev=self.head
        while temp1!=self.head:
            temp1=self.head.next
            prev=self.head
        temp1.next=None
        self.tail=prev
        self.tail.next=self.head
        
    def delete_pos(self,pos):
        if self.head is None:
            print("CLL is empty")
        elif pos==1:
            delete_end()
        else:
            temp=self.head.next
            prev=self.head
            for i in range(1,pos-1):
                temp=temp.next
                prev=prev.next
            prev.next=temp.next 
    
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
print()
obj.insert_end(30)
obj.display()
print()
obj.insert_pos(4,14)
obj.display()
print()
obj.delete_beg()
obj.display()
print()
#obj.delete_end()
#obj.display()
#print()
obj.delete_pos(3)
obj.display()
print()

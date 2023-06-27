class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    
    def insert_pos(self,pos,data):
        ne=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        ne.next=temp.next
        temp.next=ne

    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                if temp.next!=None:
                    print(temp.data,end=" -> ")
                else:
                    print(temp.data,end=" ")
                temp=temp.next 
obj=SLL()
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
obj.insert_pos(3,"100")
print()
obj.display()
        


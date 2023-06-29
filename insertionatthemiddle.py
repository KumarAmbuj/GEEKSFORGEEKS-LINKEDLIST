class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtTheEnd(self,data):
        newnode=Node(data)

        if self.head is None:
            self.head=newnode
            print('data inserted')
            return
        t=self.head
        while(t.next):
            t=t.next
        t.next=newnode
        print('Data inserted')



    def insertAtTheMiddle(self,n,data):
        newnode=Node(data)
        t=self.head
        while(t.data!=n):
            t=t.next
        newnode.next=t.next
        t.next=newnode


    def printdata(self):
        t=self.head
        while(t):
            print(t.data)
            t=t.next

l=LinkedList()
l.insertAtTheEnd(3)
l.insertAtTheEnd(5)
l.insertAtTheEnd(7)
l.insertAtTheEnd(9)
l.insertAtTheEnd(8)

l.insertAtTheMiddle(3,9)
l.insertAtTheMiddle(5,4)
l.insertAtTheMiddle(4,2)


l.printdata()
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
            print('data insereted')
            return

        t=self.head
        while(t.next):
            t=t.next
        t.next=newnode
        print('Data inserted')

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

l.printdata()







class Node:
    def __init__(self,data):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtBeginning(self, data):

        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode

        print(" node inserted")


    def deletefirstnode(self):
        value=self.head.data
        self.head=self.head.next
        print(value)
        print("##########")

    def printdata(self):
        t=self.head

        while(t):
            print(t.data)
            t=t.next


l=LinkedList()
l.insertAtBeginning(1)
l.insertAtBeginning(2)
l.insertAtBeginning(7)
l.insertAtBeginning(5)
l.insertAtBeginning(8)
l.insertAtBeginning(2)

l.deletefirstnode()
l.deletefirstnode()
l.deletefirstnode()

l.printdata()
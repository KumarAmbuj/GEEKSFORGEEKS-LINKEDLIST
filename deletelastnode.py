class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None


    def insertnode(self, data):

        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode

    def deletelastnode(self):
        t=self.head
        while(t.next.next):
            t=t.next

        t.next=None

    def printdata(self):
        t=self.head
        while(t):
            print(t.data,end='')
            t=t.next
        print()

l=LinkedList()
l.insertnode(4)
l.insertnode(5)
l.insertnode(8)
l.insertnode(5)
l.insertnode(3)
l.printdata()

l.deletelastnode()
print()
l.printdata()
print()

l.deletelastnode()
l.printdata()
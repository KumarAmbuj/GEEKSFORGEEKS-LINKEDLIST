 class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertnode(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode

    def printdata(self):
        t=self.head
        while(t):
            print(t.data,end=' ')
            t=t.next

    def removeduplicates(self):
        temp=self.head
        while(temp is not None and temp.next is not None):
            if(temp.data == temp.next.data):
                temp.next=temp.next.next
            else:
                 temp=temp.next
        print()

    def newlist(self):
        t=self.head
        while(t):
            print(t.data,end=' ')
            t=t.next


l=LinkedList()
l.insertnode(1)
l.insertnode(1)
l.insertnode(1)
l.insertnode(2)
l.insertnode(3)
l.insertnode(3)
l.insertnode(3)

l.printdata()
l.removeduplicates()
l.newlist()
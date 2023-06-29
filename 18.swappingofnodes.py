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

    def swapnode(self,x,y):
        prevx=None
        px=self.head
        while(px is not None and px.data!=x):
            prevx=px
            px=px.next


        prevy=None
        py=self.head
        while(py is not None and py.data!=y):
            prevy=py
            py=py.next


        if x==y:
            return

        if px is None or py is None:
            return

        if prevx is not None:
            prevx.next=py

        else:
            self.head=py


        if prevy is not None:
            prevy.next=px

        else:
            self.head=px


        temp=px.next
        px.next=py.next
        py.next=temp

        print()


    def newlist(self):
        t=self.head
        while(t):
            print(t.data,end=' ')
            t=t.next



l=LinkedList()
l.insertnode(1)
l.insertnode(2)
l.insertnode(5)
l.insertnode(8)
l.insertnode(4)
l.insertnode(9)
l.printdata()

l.swapnode(9,1)
l.newlist()
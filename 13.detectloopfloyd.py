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

    def makealoop(self):
        t=self.head
        t.next.next.next.next.next.next.next=t



    def detectloop(self):

        slowp=self.head
        fastp=self.head.next.next
        while(slowp and fastp and fastp.next):


            if(slowp == fastp):
                print('loop found')
                return

            slowp = slowp.next
            fastp = fastp.next.next

l=LinkedList()
l.insertnode(1)
l.insertnode(2)
l.insertnode(3)
l.insertnode(4)
l.insertnode(5)
l.insertnode(6)
l.insertnode(7)
l.insertnode(8)

l.makealoop()
l.detectloop()
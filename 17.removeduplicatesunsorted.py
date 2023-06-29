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
        t=self.head
        while(t is not None and t.next is not None):
            s=t
            while(s.next):
                if(t.data==s.next.data):
                    s.next=s.next.next

                else:
                    s=s.next

            t=t.next

        print()

    def newlist(self):
        t=self.head
        while(t):
            print(t.data,end=' ')
            t=t.next

l=LinkedList()
l.insertnode(12)
l.insertnode(21)
l.insertnode(43)
l.insertnode(41)
l.insertnode(21)
l.insertnode(12)
l.insertnode(11)
l.insertnode(12)
l.insertnode(12)
l.insertnode(43)
l.printdata()
l.removeduplicates()

l.newlist()



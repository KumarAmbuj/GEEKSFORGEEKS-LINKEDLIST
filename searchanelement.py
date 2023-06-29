class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None



    def insertnode(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return

        t=self.head
        while(t.next):
            t=t.next

        t.next=newnode

    def printdata(self):
        t=self.head
        while(t):
            print(t.data,end=' ')
            t=t.next

    def searchanelement(self,n):

        t=self.head
        count=0
        while(t):
            count = count + 1
            if(t.data==n):
                print('{} is present at {}'.format(n,count))
                return

            t=t.next


l=LinkedList()
l.insertnode(1)
l.insertnode(2)
l.insertnode(3)
l.insertnode(4)
l.insertnode(5)

l.printdata()

l.searchanelement(3)





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
            print(t.data, end=' ')
            t=t.next

        print()


    def getnooftimesoccurs(self,key):

        t=self.head
        count=0
        while(t):
            if(t.data==key):
                count=count+1

            t=t.next
        print(count)



l=LinkedList()
l.insertnode(9)
l.insertnode(5)
l.insertnode(8)
l.insertnode(0)
l.insertnode(5)

l.printdata()
l.getnooftimesoccurs(5)

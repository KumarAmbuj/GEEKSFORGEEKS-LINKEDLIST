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
            print(t.data, end=' ')
            t=t.next


    def nthnodefromlast(self,n):

        t=self.head
        count=0
        while(t):
            count=count+1
            t=t.next
        print()
        print(count)
        requirednode=count-n


        t=self.head
        count=0
        while(t):
            if(count==requirednode):
                return t.data
            count=count+1
            t=t.next


l=LinkedList()
l.insertnode(2)
l.insertnode(4)
l.insertnode(9)
l.insertnode(7)
l.insertnode(5)
l.insertnode(8)
l.insertnode(3)
l.insertnode(1)
l.insertnode(5)

l.printdata()

print('nthnodefromlast is ',l.nthnodefromlast(8))

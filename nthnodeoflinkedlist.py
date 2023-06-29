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

    def nthnode(self,n):
        current=self.head
        count=0

        while(current):
            if(count==n):
                return current.data
            count=count+1
            current =current.next



l=LinkedList()
l.insertnode(2)
l.insertnode(4)
l.insertnode(6)
l.insertnode(8)

n=2
print(' element at index {} is {}'.format(n,l.nthnode(2)))
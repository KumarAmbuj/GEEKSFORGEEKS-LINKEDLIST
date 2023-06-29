class Node:
    def __init__(self, data):
        self.data=data
        self.next=None



class LinkedList:

    def __init__(self):
        self.head=None


    def insertnode(self, data):
        newnode=Node(data)

        newnode.next=self.head
        self.head=newnode

    def deletemiddlenode(self,n):

        t=self.head
        while(t.next.data!=n):
            t=t.next

        data=t.next.data
        t.next=t.next.next
        print('deleted node is {}'.format(n))



    def printdata(self):
        t=self.head

        while(t):
            print(t.data)
            t=t.next




l=LinkedList()
l.insertnode(4)
l.insertnode(3)
l.insertnode(8)
l.insertnode(9)
l.insertnode(2)

l.printdata()
print()
l.deletemiddlenode(8)

l.printdata()
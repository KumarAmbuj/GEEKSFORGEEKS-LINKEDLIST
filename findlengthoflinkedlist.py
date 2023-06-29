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


    def lengthOfLinkedList(self):
        count=0
        t=self.head
        while(t):
            count=count+1
            t=t.next
        print()
        print('lenght of linked list is {}'.format(count))


l=LinkedList()
l.insertnode(2)
l.insertnode(4)
l.insertnode(5)
l.insertnode(7)
l.insertnode(9)

l.printdata()

l.lengthOfLinkedList()



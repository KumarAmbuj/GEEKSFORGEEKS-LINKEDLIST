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


    def lengthloop(self):
        slowp=self.head
        fastp=self.head

        while(slowp and fastp and fastp.next):
            slowp=slowp.next
            fastp=fastp.next.next



            if(slowp==fastp):
                count=1
                slowp=slowp.next
                while(slowp!=fastp):
                    count=count+1
                    slowp=slowp.next

                return count

l=LinkedList()
l.insertnode(1)
l.insertnode(2)
l.insertnode(3)
l.insertnode(4)
l.insertnode(5)
l.insertnode(6)
l.insertnode(7)

l.makealoop()
print(l.lengthloop())





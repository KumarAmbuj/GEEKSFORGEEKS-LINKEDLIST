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

    def printmiddlenode(self):
        t=self.head
        count=0
        while(t):
            count=count+1
            t=t.next

        if count%2==0:
            middle=int(count/2)

            count = 1
            t = self.head
            while (t):
                if (count == middle):
                    return t.data, t.next.data

                count = count + 1
                t = t.next

        else:
            middle=int(count/2)+1

            count = 1
            t = self.head
            while (t):
                if (count == middle):
                    return t.data

                count = count + 1
                t = t.next

        count=0
        t=self.head
        while(t):
            if(count==middle):
                return t.data

            count=count+1
            t=t.next

l=LinkedList()
l.insertnode(2)
l.insertnode(5)
l.insertnode(7)
l.insertnode(6)
l.insertnode(2)
l.insertnode(5)
l.insertnode(4)

l.printdata()

print(l.printmiddlenode())


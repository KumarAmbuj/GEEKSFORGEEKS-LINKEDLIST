class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



class Linkedlist:
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
        temp=self.head
        s=set()
        while(temp):
            if(temp in s):
                return True

            s.add(temp)
            temp=temp.next

        return False

l=Linkedlist()
l.insertnode(7)
l.insertnode(6)
l.insertnode(1)
l.insertnode(2)
l.insertnode(3)
l.insertnode(4)
l.insertnode(5)
l.insertnode(0)



l.makealoop()
if(l.detectloop()):
    print('loop found')
else:
    print('loop not found')






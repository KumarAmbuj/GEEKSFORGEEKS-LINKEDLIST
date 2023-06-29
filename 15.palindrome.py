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


    def ispalindrome(self):
        p=self.head
        q=self.head
        startsecond=None
        while(True):
            p=p.next.next

            if(p.next is None):
                startsecond=q.next.next
                break;

            if(p is None):
                startsecond=q.next
                break;

            q=q.next

        q.next=None

        list=[]

        t=startsecond
        while(t):
            list.append(t.data)
            t=t.next

        newlist=list[::-1]
        print(newlist)

        temp=self.head
        i=0
        while(temp and len(newlist)):
            if(temp.data!=newlist[i]):
                print('not a palindrome')
                break;
            temp=temp.next
            i=i+1

        else:
            print('palindrome')


l=LinkedList()
l.insertnode(1)
l.insertnode(2)
l.insertnode(3)
l.insertnode(4)
l.insertnode(3)
l.insertnode(2)
l.insertnode(1)

l.printdata()
l.ispalindrome()





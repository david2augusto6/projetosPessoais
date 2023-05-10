class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return f"Node[Data = {self.data,}]"

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insertBeg(self, e):
        new = Node(e, None, None)
        if self.head == None:
            self.head = self.tail = new
        else:
            new.prev = None
            new.next = self.head
            self.head.prev = new
            self.head = new
    
    def insertEnd(self, e):
        if self.head == None:
            self.head = Node(e)
        else:
            now = self.head
            while now.next != None:
                now = now.next
            new = Node(e)
            new.prev = now
            new.next = None
    
    def getNode(self, p):
        now = self.head
        if now == None:
            return None
        i = 0
        while i < p and now.next is not None:
            now = now.next
            if now == None: break
            i+=1
        return now

    def insertPos(self, p, e):
        new = Node(data)
        if self.head == None or p == 0:
            self.insertBeg(e)
        elif p > 0:
            t = self.getNode(p)
            if t == None or t.next == None:
                self.insertEnd(e)
            else:
                new = t.next
                new.prev = t
                t.next.prev = new
                t = new
    def show(self):
        
        while
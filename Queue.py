class Queue1:
    def __init__(self):
        self.items=[]
    
    def __str__(self):
        values=[str(x) for x in self.items]
        return " ".join(values)
    
    def isEmpty(self):
        if self.items==[]:
            return True
        else:
            return False
        
    def enqueue(self,values):
        self.items.append(values)
        return "The element is inserted at the end of Queue"
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.items.pop(0)
        
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.items[0]
        
    def delete(self):
        self.items=None

#implementation of Circular Queue
    
class CircularQueue:

    def __init__(self,maxSize):
        self.items=maxSize*[None]
        self.maxSize=maxSize
        self.start=-1
        self.top=-1

    def __str__(self):
        values=[str(x) for x in self.items]
        return " ".join(values)
    
    def isFull(self):
        if self.top + 1==self.start:
            return True
        elif self.start==0 and self.top+1==self.maxSize:
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.top ==-1:
            return True
        else:
            return False
        
    def enqueue(self,value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top+1==self.maxSize:
                self.top=0
            else:
                self.top+=1
                if self.start==-1:
                    self.start=0
        self.items[self.top]=value
        return "the element is inserted at end of queue"
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            firstElement=self.items[self.start]
            start=self.start
            if self.start==self.top:
                self.start=-1
                self.top=-1
            elif self.start+1==self.maxSize:
                self.start=0
            else:
                self.start+=1
            self.items[start]=None
            return firstElement
        
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items[self.start]
        
    def delete(self):
        self.items=self.maxSize*[None]
        self.top=-1
        self.start=-1

#Queue implementation using Linked List

class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

    def __str__(self):
        return str(self.value)
        
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def __iter__(self):
        curNode=self.head
        while curNode:
            yield curNode
            curNode=curNode.next

class Queue2:
    def __init__(self):
        self.linkedlist=LinkedList()
         
    def __str__(self):
        values=[str(x) for x in self.linkedlist]
        return " ".join(values)
    
    def enqueue(self,value):
        newNode=Node(value)
        if self.linkedlist.head==newNode:
            self.linkedlist.head=newNode
            self.linkedlist.tail=newNode
        else:
            self.linkedlist.tail.next=newNode
            self.linkedlist.tail=newNode

    def isEmpty(self):
        if self.linkedlist.head==None:
            return True
        else:
            return False
        
    def deque(self):
        if self.isEmpty():
            return "there is no element in the queue"
        else:
            tempNode=self.linkedlist.head
            if self.linkedlist.head==self.linkedlist.tail:
                self.linkedlist.head=None
                self.linkedlist.tail=None
            else:
                self.linkedlist.head=self.linkedlist.head.next
            return tempNode
    
    def peek(self):
        if self.isEmpty():
            return "there is no element in the queue"
        else:
            return self.linkedlist.head
        
    def delete(self):
        self.linkedlist.head=None
        self.linkedlist.tail=None

#queue using collection module

from collections import deque

customQueue=deque(maxlen=3)
customQueue.append(3)
customQueue.append(2)
customQueue.append(1)
print(customQueue.popleft())
print(customQueue.clear())

#queue using queue module

import queue as q

customQueue1=q.Queue(maxsize=3)
print(customQueue1.qsize())
customQueue1.put(1)
customQueue1.put(2)
customQueue1.put(3)
print(customQueue1.empty())
print(customQueue1.full())
print(customQueue1.get())

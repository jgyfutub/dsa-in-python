#stack implementation with no limit

class Stack1:
    def __init__(self):
        self.list=[]
    
    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return '\n'.join(values)
    
    def isempty(self):
        if self.list==[]:
            return True
        else:
            return False
    
    def push(self,value):
        self.list.append(value)
        return "the element has been successfully added"
    
    def pop(self):
        if self.isempty():
            return "there is no element in the stack"
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isempty():
            return "there is no element in the stack"
        else:
            return self.list[-1]
        
    def delete(self):
        self.list=None

#stack implementation with limits

class Stack2:
    def __init__(self,maxSize):
        self.maxSize=maxSize
        self.list=[]
    
    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False
        
    def isFull(self):
        if len(self.list)==self.maxSize:
            return True
        else:
            return False
        
    def push(self,value):
        if self.isFull():
            return "The stack is FULL"
        else:
            self.list.append(value)
            return "the element has successfully inserted"
        
    def pop(self):
        if self.isEmpty():
            return "there is no element in the stack"
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return "there is no element in the stack"
        else:
            return self.list[-1]
        
    def delete(self):
        self.list=None

#Stcak implementation using linked list

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class StackedLinkedList:
    def __init__(self):
        self.head=None

    def pop(self):
        node=self.head
        self.head=self.head.next
        node.next=None

class Stack3:
    def __init__(self):
        self.LinkedList=StackedLinkedList()

    def isEmpty(self):
        if self.LinkedList.head==None:
            return True
        else:
            return False
        
    def push(self,value):
        node=Node(value)
        node.next=self.LinkedList.head
        self.LinkedList.head=node

    def pop(self):
        if self.isEmpty() :
            return "There is no element in the Stack"
        else:
            nodeValue=self.LinkedList.head.value
            self.LinkedList.head=self.LinkedList.head.next
            return nodeValue
    
    def peek(self):
        if self.isEmpty() :
            return "There is no element in the Stack"
        else:
            nodeValue=self.LinkedList.head.value
            return nodeValue
        
    def delete(self):
        self.LinkedList.head=None

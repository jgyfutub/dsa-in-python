class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
 
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
 
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
    def createDSLL(self,nodeValue):
        newNode=Node(nodeValue)
        self.head=newNode
        self.tail=newNode
        newNode.prev=newNode
        newNode.next=newNode
        return "CDLL created"
    
    def insertCDLL(self,value,location):
        if self.head is None:
            return "CDLL dont exist"
        else:
            newNode=Node(value)
            if location==0:
                newNode.next=self.head
                newNode.prev=self.tail
                self.head.prev=newNode
                self.head=newNode
                self.tail.next=newNode
            elif location==1:
                newNode.next=self.head
                newNode.prev=self.tail
                self.head.prev=newNode
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                newNode.next=tempNode.next
                newNode.prev=tempNode
                newNode.next.prev=newNode
                tempNode.next=newNode
            return "The node has been inserted"
        
    def transverse(self):
        if self.head is None:
            print("no element to traverse")
        else:
            tempNode=self.head
            while tempNode:
                print(tempNode.value)
                if tempNode==self.tail:
                    break
                tempNode=tempNode.next

    def reverse_transverse(self):
        if self.head is None:
            print("no element to reverse traverse")
        else:
            tempNode=self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode==self.head:
                    break
                tempNode=tempNode.prev
            
    def searchCDLL(self,nodeValue):
        if self.head is None:
            print("no element to search")
        else:
            tempNode=self.head
            while tempNode:
                print(tempNode.value)
                if tempNode.value==nodeValue:
                    return tempNode.value
                if tempNode==self.tail:
                    return "value not in CDLL"
                tempNode=tempNode.next

    def delete(self,location):
        if self.head is None:
            print("no element to delete")
        else:
            if location==0:
                if self.head==self.tail:
                    self.head.prev=None
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=self.tail
                    self.tail.next=self.head
            if location==1:
                if self.head==self.tail:
                    self.head.prev=None
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=self.head
                    self.head.prev=self.tail
            else:
                curNode=self.head
                index=0
                while index < location-1:
                    curNode=curNode.next
                    index+=1
                curNode.next=curNode.next.next
                curNode.next.prev-curNode
                print("node has been deleted")
    
    def deleteAll(self):
        if self.head is None:
            print("no element to delete")
        else:
            self.tail.next=None
            tempNode=self.head
            while tempNode:
                tempNode.prev=None
                tempNode=tempNode.next
        self.head=None
        self.tail=None
        print("DLL has been deleted")
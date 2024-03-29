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
            node = node.next
    
    def createSLL(self,nodeValue):
        node=Node(nodeValue)
        node.next=node
        self.head=node
        self.tail=node
        return "CSLL has been created"
    
    def insertCLL(self,value,location):
        if self.head is None:
            return 
        else:
            newNode=Node(value)
            if location==0:
                newNode.next=self.head.next
                self.head=newNode
                self.tail.next=newNode
            elif location==1:
                newNode.next=self.tail.next
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index <location -1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=newNode
                newNode.next=nextNode
            return "the node has been succesfully inserted"
    
    def transverseSLL(self):
        if self.head is None:
            print("no element")
        else:
            tempNode=self.head
            while tempNode:
                print(tempNode.value)
                tempNode=tempNode.next
                if tempNode==self.tail.next:
                    break
    def searchSLL(self,nodeValue):
        if self.head is None:
            return "There is not any node in this CSLL"
        else:
            tempNode=self.head
            while tempNode:
                if tempNode.value==nodeValue:
                    return tempNode.value
                tempNode=tempNode.next
                if tempNode==self.tail.next:
                    return "the node does not exists in this CSLL"
    
    def deleteNode(self,location):
        if self.head is None:
            print("There is not any in CSLL")
        else:
            if location == 0:
                if self.head==self.tail:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.tail.next=self.head
            elif location==1:
                if self.head ==self.tail:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    node=self.head
                    while node is not None:
                        if node.next== self.tail:
                            break
                        node=node.next
                    node.next=self.head
                    self.tail=node
            else:
                tempNode=self.head
                index=0
                while index <location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=nextNode.next
    
    def deleteentireCSLL(self):
        self.head=None
        self.tail.next=None
        self.tail=None
                

circularSLL=CircularSinglyLinkedList()
circularSLL.createSLL(1)
print([node.value for node in circularSLL])
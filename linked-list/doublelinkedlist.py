class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None
    
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    
    def createDLL(self,nodevalue):
        node=Node(nodevalue)
        node.prev=None
        node.next=None
        self.head=node
        self.tail=node
        return "The DLL is created successfully"
    
    def insertNode(self,nodeValue,location):
        if self.head is None:
            print("node cant be inserted")
        else:
            newNode=Node(nodeValue)
            if location==0:
                newNode.prev=None
                newNode.next=self.head
                self.head.prev=newNode
                self.head=newNode
            if location==1:
                newNode.next==None
                newNode.prev=self.tail
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

    def transverse(self):
        if self.head is None:
            print("no element to traverse")
        else:
            tempNode=self.head
            while tempNode:
                print(tempNode.value)
                tempNode=tempNode.next

    def reverse_transverse(self):
        if self.head is None:
            print("no element to traverse")
        else:
            tempNode=self.tail
            while tempNode:
                print(tempNode.value)
                tempNode=tempNode.prev

    def search(self,nodeValue):
        if self.head is None:
            return "no element to traverse"
        else:
            tempNode=self.head
            while tempNode:
                if tempNode.value==nodeValue:
                    return tempNode.value
                tempNode=tempNode.next        
            return "node not here"
        
    def deleteNode(self,location):
        if self.head is None:
            print("There is not any element in DLL")
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=None
            elif location==1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=None
            else:
                curNode=self.head
                index=0
                while index < location-1:
                    curNode=curNode.next
                    index+=1
                curNode.next=curNode.next.next
                curNode.next.prev=None
            print("node deleted")
    
    def deleteAll(self):
        if self.head is None:
            print("no node in DLL")
        else:
            tempNode=self.head
            while tempNode:
                tempNode.prev=None
                tempNode=tempNode.next
            self.head=None
            self.tail=None
            print("DLL has been deleted")
    
doublyLL=DoublyLinkedList()
doublyLL.createDLL(5)

print([node.value for node in doublyLL])
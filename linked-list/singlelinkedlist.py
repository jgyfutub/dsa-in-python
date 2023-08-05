class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1

    def insert(self,insert,value):
        new_node=Node(value)
        temp_node=self.head
        if insert<0 or insert>self.length:
            return False
        elif self.length==0:
            self.head=new_node
            self.tail=new_node
        elif insert==0:
            self.prepend(value)
        else:
            for _ in range(insert-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
        self.length+=1
        return True
    
    def transverse(self):
        current=self.head
        while current is not None:
            print(current)
            current=current.next

    def search(self,target):
        current=self.head
        index=0
        while current is not None:
            if target== current.value:
                print(index)
                return True
            index+=1
            current=current.next
        return False
    
    def get(self,index):
        current=self.head
        if index==-1:
            return self.tail
        elif index<-1 or index>=self.length:
            return None
        for _ in range(index):
            current=current.next
        return current
    
    def set(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    
    def pop_first(self):
        if self.length==0:
            return None
        popped_node=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            popped_node.next=None
        self.length-=1
        return popped_node
    
    def pop(self):
        if self.length==0:
            return None
        popped_node=self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            temp=self.head
            while temp.next is not self.tail:
                temp=temp.next
            self.tail=temp
            temp.next=None
            return popped_node
    
    def remove(self,index):
        if index>=self.length or index<0:
            return None
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        prev_node=self.get(index-1)
        popped_node=prev_node.next
        prev_node.next=popped_node.next
        popped_node.next=None
        self.length-=1
        return popped_node
    
    def delete_all(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node is not None:
            result+=str(temp_node.value)
            if temp_node.next is not None:
                result+='->'
            temp_node=temp_node.next
        return result
        
new_ll=LinkedList()
new_ll.append(10)
new_ll.append(20)
new_ll.append(30)
new_ll.append(40)
new_ll.prepend(0)
new_ll.prepend(-10)
new_ll.insert(0,90)
new_ll.delete_all()
print(new_ll)
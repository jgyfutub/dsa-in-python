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

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head

    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node is not None:
            result+=str(temp_node.value)
            if temp_node.next is not None:
                result+='->'
            temp_node=temp_node.next
        return result
    
    def remove_duplicates(self):
        if self.head is None:
            return
        node_values = set()  # set to store unique node values
        current_node = self.head
        node_values.add(current_node.value)
        while current_node.next:
            if current_node.next.value in node_values:  # duplicate found
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node

    def isPalindrome(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
            
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
    
    def removeElements(self, head, val):
        dummy_head = Node(-1)
        dummy_head.next = head
 
        prev_node, curr_node = dummy_head, head
        while curr_node:
            if curr_node.val == val:
                prev_node.next = curr_node.next
            else:
                prev_node = curr_node
            curr_node = curr_node.next
 
        return dummy_head.next
    
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prehead = Node(-1)
 
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next
 
        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2
 
        return prehead.next
        
    def middleNode(self, head):
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            
        return head
    
    def nthToLast(self,n):
        pointer1=self.head
        pointer2=self.head

        for i in range(n):
            if pointer2 is None:
                return None
            pointer2=pointer2.next

        while pointer2:
            pointer1=pointer1.next
            pointer2=pointer2.next
        return pointer1
    
    def partition(self,x):
        curNode=self.head
        self.tail=self.head

        while curNode:
            nextNode=curNode.next
            curNode.next=None
            if curNode.value<x:
                curNode.next=self.head
                self.head=curNode
            else:
                self.tail.next=curNode
                self.tail=curNode
            curNode=curNode.next

        if self.tail.next is not None:
            self.tail.next=None

def sumList(LLa,LLb):
    n1=LLa.head
    n2=LLb.head
    carry=0
    ll=LinkedList()
    while n1 or n2:
        result=carry
        if n1:
            result+=n1.value
            n1=n1.next
        if n2:
            result+=n2.value
            n2=n2.next
        ll.append(int(result%10))
        carry=result/10

    return ll
    
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
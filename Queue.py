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
        
    
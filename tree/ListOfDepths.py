class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def add(self, val):
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)
    def __str__(self):
        return "({val})".format(val = self.val) + str(self.next)

class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def depth(tree):
    if tree is None:
        return 0
    if tree.left==None and tree.right ==None:
        return 1
    else:
        depthLeft=1+depth(tree.left)
        depthRight=1+depth(tree.right)
        if depthLeft<depthRight:
            return depthLeft
        else:
            return depthRight
    

def treeToLinkedList(tree, custDict = {}, d = None):
    if d==None:
        d=depth(tree)
    if custDict.get(d)==None:
        custDict[d]=LinkedList(tree.val)
    else:
        custDict[d].add(tree.val)
        if d==1:
            return custDict
    if tree.left !=None:
        custDict=treeToLinkedList(tree.left,custDict,d-1)
    if tree.right!=None:
        custDict=treeToLinkedList(tree.right.custDict,d-1)
    return custDict


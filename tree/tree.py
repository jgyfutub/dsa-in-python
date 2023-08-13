#tree terminology
#root->top node without parent
#edge->link between parent and link
#leaf->a node which does not have children
#sibling->children of same parent
#ancestor->parent,grandparent of a node
#depth of node->length of path from root to node
#height of node->a lenfth of path from the node to the deppest node
#depth of tree->depth of root node
#height of tree->height of root node
from Queue import Queue2 as queue
class Node:
    def __init__(self,data,childen=[]):
        self.data=data
        self.children=childen

    def __str__(self,level=0):
        ret=" "*level+str(self.data)+'\n'
        for child in self.children:
            ret+=child.__str__(level+1)
        return ret
    
    def addChild(self,TreeNode):
        self.children.append(TreeNode)

tree=Node('Drinks',[])
cold=Node('Cold',[])
hot=Node('Hot',[])
tree.addChild(cold)
tree.addChild(hot)
tree1=Node('Drinks1',[])
cold1=Node('Cold1',[])
hot1=Node('Hot1',[])
tree1.addChild(cold1)
tree1.addChild(hot1)
print(tree1)
print(tree)

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
newBT=TreeNode("Drinks")
leftChild=TreeNode("Hot")
rightChild=TreeNode("Right")
newBT.leftChild=leftChild
newBT.rightChild=rightChild

#preorder traversal

def preordertraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preordertraversal(rootNode.leftChild)
    preordertraversal(rootNode.rightChild)

#inorder traversal

def inOrdertraversal(rootNode):
    if not rootNode:
        return
    inOrdertraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrdertraversal(rootNode.rightChild)

#post order traversal

def postOrdertraversal(rootNode):
    if not rootNode:
        return
    postOrdertraversal(rootNode.leftChild)
    postOrdertraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrdertraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

def searchBT(rootNode,nodeValue):
    if not rootNode:
        return "the bt dont exist"
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value.data==nodeValue:
                return "Success"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "value is not in BT"

def insertNodeBT(rootNode,newNode):
    if not rootNode:
        rootNode=newNode
    else:
        customQueue=queue.Queue()
        customQueue.dequeue(rootNode)
        while not (customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild=newNode
                return "Inserted"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild=newNode
                return "Inserted"
            
def getDepeestNode(rootNode):
    if not rootNode:
        return 
    else:
        customQueue=queue.Queue()
        customQueue.dequeue(rootNode)
        while not (customQueue.isEmpty()):
            root=customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        deepestNode=root.value
        return deepestNode

def deleteDeepestNode(rootNode,dNode):
    if not rootNode:
        return 
    else:
        customQueue=queue.Queue()
        customQueue.dequeue(rootNode)
        while not (customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value is dNode:
                root.value=None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild=None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild=None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)

def deleteNodeBT(rootNode,node):
    if not rootNode:
        return "this bt does not exists"
    else:
        customQueue=queue.Queue()
        customQueue.dequeue(rootNode)
        while not (customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value.data==node:
                dNode=getDepeestNode(rootNode)
                root.value.data=dNode.data
                deleteDeepestNode(rootNode,dNode)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

def deleteBT(rootNode):
    rootNode.data=None
    rootNode.leftChild=None
    rootNode.rightChild=None
    return "whole BT deleted"

class BinaryTree:
    def __init__(self,size):
        self.customList=size*[None]
        self.lastUsedIndex=0
        self.maxSize=size

    def insertNode(self,value):
        if self.lastUsedIxed+1==self.maxSize:
            return "The Binary tree is full"
        self.customList[self.lastUsedIndex+1]=value
        self.lastUsedIndex+=1
        return "The value has succcessfully inserted"
     
    def searchNode(self,nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i]==nodeValue:
                return "Success"
        return "Not found"
    
    def preorderTraversal(self,index):
        if index>self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preorderTraversal(index*2)
        self.preorderTraversal(index*2+1)

    def inorderTraversal(self,index):
        if index>self.lastUsedIndex:
            return
        self.preorderTraversal(index*2)
        print(self.customList[index])
        self.preorderTraversal(index*2+1)

    def postorderTraversal(self,index):
        if index>self.lastUsedIndex:
            return
        self.preorderTraversal(index*2)
        self.preorderTraversal(index*2+1)
        print(self.customList[index])

    def levelOrderTraversal(self,index):
        for i in range(index,self.lastUsedIndex+1):
            print(self.customList[i])

    def deleteNode(self,value):
        if self.lastUsedIndex==0:
            return "There is no node to be deleted"
        for i in range(1,self.lastUsedIndex+1):
            if self.customList[i]==value:
                self.customList[i]=self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex]=None
                self.lastUsedIndex-=1
                return "The node has been deleted successfully"
            
    def deleteBT(self):
        self.customList=None
        return "The BT has deleted"
            
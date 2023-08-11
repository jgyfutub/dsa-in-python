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

preordertraversal(newBT)
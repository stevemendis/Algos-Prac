class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def branchSum(root):
    sums = []
    calcBranchSum (root,0,sums)
    return sums

def calcBranchSum(node , runningSums, sums):
    if node is None:
        return
    newRunningSum = runningSums + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return
    
    calcBranchSum(node.left, newRunningSum, sums)
    calcBranchSum(node.right, newRunningSum, sums)



n1 = BinaryTree(1)
n2 = BinaryTree(2)
n3 = BinaryTree(3)
n4 = BinaryTree(4)
n5 = BinaryTree(5)
n6 = BinaryTree(6)
n7 = BinaryTree(7)
n8 = BinaryTree(8)
n9 = BinaryTree(9)
n10 = BinaryTree(10)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8
n4.right = n9
n5.right = n10
print (BinaryTree)
print(branchSum(n1))

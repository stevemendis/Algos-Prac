# Time Complexity Avg : O(Log(n))
#                 Worst : O(n)

# Space Complexity Avg : O(Log(n))
#                 Worst : O(n)

# def findClosestValBST(tree, target):
#     return closestValHelpingFunc(tree, target, float("inf"))

# def closestValHelpingFunc(tree, target, closest):
#     if tree is None:
#         return closest
#     if abs(target - closest) > abs(target - tree.value):
#         closest = tree.value
#     if target < tree.value:
#         return closestValHelpingFunc (tree.left, target, closest)
#     elif target > tree.value:
#         return closestValHelpingFunc (tree.right, target, closest)
#     else:
#         return closest


# Iterative Method

# Time Complexity Avg : O(Log(n))
#                 Worst : O(n)

# Space Complexity Avg : O(1)
#                 Worst : O(1)

def findClosestValBST(tree, target):
    return closestValHelpingFunc(tree, target, float("inf"))

def closestValHelpingFunc(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest


# Need to make a tree and pass it to the given fucntion
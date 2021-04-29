# Type 1 - Using 2 For Loops 
# Time Complexity - O(n^2)
# Space Complexity - O(1)
# Not an optimal Approach

# def twoNumberSum (array , targetSum):
#     for i in range(len(array) - 1):
#         firstNumber = array[i]
        
#         for j in range (i+1, len(array)):
#             secondNumber = array[j]
    
#             if firstNumber + secondNumber == targetSum:
#                 return [firstNumber, secondNumber]
#     return []

# ******************-----------------------*************************

# Type 2 - Using HashTable or Dict in python or Object in Js 
# Time Complexity - O(n)
# Space Complexity - O(n)
# Better in Terms of Time

# def twoNumberSum(array, targetSum):
#     numbers = {}
#     for num in array:
#         # Assume x = num
#         # x + y = 10
#         # Thus, y = 10 - x
#         # check for y in numbers. if present return else add x in the hashtable.
#         # It will not create duplication as dict accepts only one number
#         if targetSum - num in numbers:   
#             return [targetSum-num, num]
#         else:
#             numbers[num] = True
#     return []

# ******************-----------------------*************************

# Type 3 - Optimal Solution by arranging all numbers in ascending order 
# Time Complexity - O(n(log(n)))
# Space Complexity - O(1)
# Better In Terms of Space
def twoNumberSum(array, targetSum):
    array.sort()
    print (array)
    leftPointer = 0
    rightPointer = len(array) - 1
    while leftPointer < rightPointer:
        currentSum = array[leftPointer] + array[rightPointer]
        if currentSum == targetSum:
            return [array[leftPointer] , array[rightPointer]]
        elif currentSum < targetSum :
            leftPointer += 1
        elif currentSum > targetSum :
            rightPointer -= 1
    return[]

print(twoNumberSum([5,6,3,2,1], 11))
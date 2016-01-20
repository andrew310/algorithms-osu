__author__ = 'Andrew, Myles, Robert'

def maxSubArrayEnum(numList):
    start, end, maxSum = 0, 0, 0

    for i in range(0, len(numList)):
        for j in range(i, len(numList)):
            tempSum = sum(numList[i:j])
            if maxSum < tempSum:
                maxSum = tempSum
                start, end = j, i
    print maxSum
    return (start, end, maxSum)

def maxSubArrayEnum2(numList):
    start, end, maxSum, newStart, tempSum = 0, 0, 0, 0, 0

    for i, j in enumerate(numList): #this is just one loop, i is the index and j is the value
        tempSum += j
        if maxSum < tempSum:
            maxSum = tempSum
            start, end = newStart, i
        elif tempSum < 0: #if we have a subarray that dips below zero, it is a negative sequence so just dump it and start over
            tempSum = 0
            newStart = i

    print maxSum
    return (start, end, maxSum)


myArray = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]


maxSubArrayEnum2(myArray)


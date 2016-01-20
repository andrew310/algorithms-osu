__author__ = 'Andrew, Myles, Robert'

def maxSubArrayEnum(numList):
    start, end, maxSum = 0, 0, 0

    for i in range(0, len(numList)):
        for j in range(i, len(numList)):
            tempSum = sum(numList[i:j])
            if maxSum < tempSum:
                maxSum = tempSum
                start, end = j, i
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

    return (start, end, maxSum)


def divideConquer(array, left, right):
    if (left == right): # if only one element
        return array[left]

    middle = (left+right)/2 #store the middle index, will be used to divide array into halves
    leftSub = divideConquer(array, left, middle) #leftSub will contain left half of array
    rightSub = divideConquer(array, middle+1, right) #rightSub will contain right half of array
    leftMax = 0
    rightMax = 0
    tempMax = 0
    for i in range(middle, -1, -1): #backwards loop starting at middle to 0, find max sub array of left sub
        tempMax += array[i]

        if(tempMax > leftMax):
            leftMax = tempMax

    tempMax = 0
    for i in range(middle+1, right): # loop for right sub, find max array of right sub
        tempMax += array[i]
        print tempMax
        if(tempMax > rightMax):
            rightMax = tempMax

    return max(max(leftMax, rightMax),leftMax+rightMax) #return max of three options


def maxSubArrayLT(numList):
    tempMax = maxSum = numList[0] #start with the first element of the array
    for x in numList[1:]:   #loop starting with the 2nc element in array
        tempMax = max(x, tempMax + x) #set next equal to max of current element, and next + current element
        maxSum = max(maxSum, tempMax) #compar maxSum to tempMax and set maxSum to the greater of the two
    return maxSum


myArray = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]


sumMSA = maxSubArrayLT(myArray)
print sumMSA

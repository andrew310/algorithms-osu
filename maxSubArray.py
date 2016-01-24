from ast import literal_eval
import sys
import time
__author__ = 'Andrew, Myles, Robert'

def maxSubArrayEnum(numList):
    start, end, maxSum = 0, 0, 0

    for i in range(0, len(numList)):
        for j in range(i, len(numList)):
            tempSum = sum(numList[i:j+1])
            if maxSum < tempSum:
                maxSum = tempSum
                start, end = i, j

    maxSumArray = numList[start:end+1]
    print "Max SubArray:",
    print maxSumArray, "\n"
    print "Max Sum:",
    print maxSum
    print "Runtime:",
    return (maxSum, maxSumArray)

def maxSubArrayEnum2(numList):
    maxSum, tempSum = 0, 0

    for i in range(0, len(numList)): #this is just one loop, i is the index and j is the value
        tempSum = 0
        for j in range(i, len(numList)):
            tempSum += numList[j]
            if (tempSum > maxSum):
                maxSum = tempSum
                start, end = i, j

    maxSumArray = numList[start:end+1]
    print "Max SubArray:",
    print maxSumArray, "\n"
    print "Max Sum:",
    print maxSum
    print "Runtime:",
    return (maxSum, maxSumArray)

def algo3Start(list):

    return divideConquer(list, 0, len(list)-1)

def divideConquer(array, left, right):
    if (left == right): # if only one element
        return array[left]

    middle = (left+right)/2 # store the middle index, will be used to divide array into halves
    leftSub = divideConquer(array, left, middle) # leftSub will contain left half of array
    rightSub = divideConquer(array, middle+1, right) # rightSub will contain right half of array
    leftMax = 0
    rightMax = 0
    tempMax = 0

    # combined funtions maxPrefix and maxSuffix from pseudocode here
    for i in range(middle, -1, -1): # backwards loop starting at middle to 0, find max sub array of left sub
        tempMax += array[i]
        if(tempMax > leftMax):
            leftMax = tempMax

    tempMax = 0
    for i in range(middle+1, right+1): # loop for right sub, find max array of right sub
        tempMax += array[i]
        startRight = middle+1
        if(tempMax > rightMax):
            rightMax = tempMax

    return max(max(leftMax, rightMax),leftMax+rightMax) #return max of three options

def maxSubArrayLT(numList):
    bestSum = -sys.maxint - 1
    bestStart = bestEnd = -1
    localStart = localSum = 0
    for i in range(0, len(numList)):
        localSum += numList[i]
        if localSum > bestSum:
            bestSum = localSum
            bestStart = localStart
            bestEnd = i
        if localSum <= 0: # if localSum dips below 0
            localSum = 0
            localStart = i + 1

    maxSumArray = numList[bestStart:bestEnd+1]
    #print "Max SubArray:"
    #print maxSumArray, "\n"
    print "Max Sum:",
    print bestSum
    #print "Runtime:",
    return (bestSum, maxSumArray)


#########FILE INPUT AND OUPUT##########
inFile = open("MSS_Problems.txt", "r")
outFile = open("MSS_Results.txt", "w")
appendFile = open("MSS_Results.txt", "a")

numbers = inFile.read()


def runAlgorithm(algorithm, note):
    outFile.write("\n")
    outFile.write(note)
    outFile.write("\n")
    for line in numbers.splitlines():
        lst = literal_eval(line)
        outFile.write(str(algorithm(lst)))
        outFile.write("\n")


runAlgorithm(maxSubArrayEnum, "Enumeration Results:")
runAlgorithm(maxSubArrayEnum2, "Iteration Results:")
runAlgorithm(algo3Start, "Divide & Conquer Results:")
runAlgorithm(maxSubArrayLT, "Linear Results:")


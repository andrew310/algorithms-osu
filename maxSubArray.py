__author__ = 'Andrew, Myles, Robert'
# course: cs325 project 1
# date: 1/23/2016
# name: Andrew Brown, Myles Chatman, Robert Ottolia
# description: tests 4 different algorithms to find the max sub array in a given array
from ast import literal_eval
import sys
import time
import random


##############################################################
# maxSubArrayEnum(numList)
# This algorithm finds the max sub array of a given array
# inputs: numList is an array of numbers, negative or positive
# returns: the maximum sum and subarray in tuple form
def maxSubArrayEnum(numList):
    start, end, maxSum = 0, 0, 0

    #nested loop over numbers
    for i in range(0, len(numList)):
        for j in range(i, len(numList)):
            tempSum = sum(numList[i:j+1]) #note this is performing a calculation over this subarray each go
            if maxSum < tempSum:
                maxSum = tempSum
                start, end = i, j

    maxSumArray = numList[start:end+1]
    return (maxSum, maxSumArray)


##############################################################
# maxSubArrayEnum2(numList)
# This algorithm finds the max sub array of a given array, but does so more efficiently than the algorithm above
# because you don't start from scratch with the calc each time, see line 43
# inputs: numList is an array of numbers, negative or positive
# returns: the maximum sum subarray, and the max sum, in a tuple
def maxSubArrayEnum2(numList):
    maxSum, tempSum = 0, 0

    for i in range(0, len(numList)): #this is just one loop, i is the index and j is the value
        tempSum = 0
        for j in range(i, len(numList)):
            tempSum += numList[j] #this is where we improve over algo 1
            if (tempSum > maxSum):
                maxSum = tempSum
                start, end = i, j

    maxSumArray = numList[start:end+1]
    return (maxSum, maxSumArray)


##############################################################
# algo3Start(numList)
# This function is a helper for divideConquer
# inputs: an array
# returns: the same array, with the two endpoint indices
def algo3Start(list):

    return divideConquer(list, 0, len(list)-1)


##############################################################
# divideConquer(array, left, right)
# This algorithm uses divide and conquer method for the max sum sub array problem
# it splits arrays into two and finds max sum for each subarray
# inputs: list, left index, right index
# returns: a tuple that contains the max sum, as well as the sub array
def divideConquer(array, left, right):
    if (left == right): # if only one element
        return (array[left], array)

    middle = (left+right)/2 # store the middle index, will be used to divide array into halves
    leftSub = divideConquer(array, left, middle) # leftSub will contain left half of array
    rightSub = divideConquer(array, middle+1, right) # rightSub will contain right half of array
    leftIndex = middle
    rightIndex = middle+1
    leftMax = array[middle]
    rightMax =array[middle+1]
    tempMax = 0

    # combined funtions maxPrefix and maxSuffix from pseudocode here
    for i in range(middle, -1, -1): # backwards loop starting at middle to 0, find max sub array of left sub
        tempMax += array[i]
        if(tempMax > leftMax):
            leftIndex = i
            leftMax = tempMax

    tempMax = 0
    for i in range(middle+1, right+1): # loop for right sub, find max array of right sub
        tempMax += array[i]
        startRight = middle+1
        if(tempMax > rightMax):
            rightIndex = i
            rightMax = tempMax

    print leftSub

    if leftMax == max(max(leftMax, rightMax),leftMax+rightMax):
        return (leftMax, leftSub)
    elif rightMax == max(max(leftMax, rightMax),leftMax+rightMax):
        return (rightMax, rightSub)
    else:
        return  (leftMax+rightMax, array[leftIndex:rightIndex+1])


##############################################################
# maxSubArrayLT(numList)
# This algorithm solves the same problem but does so with one loop over the array
# it dumps the high score if it dips to 0, because at that point you would be detracting from the max sum
# inputs: numList is an array of numbers, negative or positive
# returns: a tuple comtaining the sum, as well as the found sub array
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

inFile.close()
outFile.close()


#######TESTING ANALYSIS#######
import argparse
import math
import random
import operator
import cProfile
import sys
import numpy
import pstats
import signal

STORED_POWERS = list()				# Hold squares of numbers instead of computing it (faster)
STORED_SQR_DISTANCES = dict() 		# Index distances to cities for quicker lookup
STORED_POWERS_SIZE = 100 			# Limit to the size of the table holding computed powers
STORED_SQR_DISTANCES_SIZE = 3000	# Limits for indexindexing distances to cities
STORED_SQR_DISTANCES_MAX = 10000
MAX_SAMPLE_SIZE = 100 				# Used to limit items to check for swapping given large data input

SHUTDOWN = False

def getSquare(num):
	global STORED_POWERS
	global STORED_POWERS_SIZE

	# Lookup the square of the number in the table
	# If it's not there, just compute it
	if num <= STORED_POWERS_SIZE:
		return STORED_POWERS[num]
	else:
		return math.pow(num, 2);

def calculateSqrDistance(cities, city1, city2):
	x = 0
	y = 1

	# Check if result has been cached already (peformance)
	if ((city1, city2)) in STORED_SQR_DISTANCES:
		return STORED_SQR_DISTANCES[(city1, city2)]
	elif ((city2, city1)) in STORED_SQR_DISTANCES:
		return STORED_SQR_DISTANCES[(city2, city1)]

	# If we don't have it in the dictionary, compute it
	xDist = abs(cities[city2][x] - cities[city1][x])
	yDist = abs(cities[city1][y] - cities[city1][y])

	result = getSquare(xDist) + getSquare(yDist)

	# Store result in table, checking if it gets full
	if calculateSqrDistance.tableSize >= STORED_SQR_DISTANCES_SIZE:
		STORED_SQR_DISTANCES.popitem()
		calculateSqrDistance.tableSize -= 1

	STORED_SQR_DISTANCES[(city1, city2)] = result
	calculateSqrDistance.tableSize += 1

	return result
calculateSqrDistance.tableSize = 0

def calculateDistance(cities, city1, city2):
	result = math.sqrt(calculateSqrDistance(cities, city1, city2))

	result = int(round(result))

	return result
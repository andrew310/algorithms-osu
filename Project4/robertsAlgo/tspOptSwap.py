import math
import random
import sys
import time

STORED_SQR_DISTANCES = dict() 		# Index computations between cities for quicker lookup
									# The key is the (city1, city2) tuple, value is 
									# ((city1_x)^2 - (city2_x)^2) + ((city1_y)^2 - (city2_y)^2)
									# Note we still have to call sqrt on this result tied to the key 
STORED_SQR_DISTANCES_SIZE = 3000	# Limits for indexing computation between cities
STORED_SQR_DISTANCES_MAX = 10000	# Arbitrary max value the the dictionary can hold (want to prevent it getting too big)
MAX_SAMPLE_SIZE = 100 				# Used to limit items to check for swapping given large data input

def main():
	global STORED_SQR_DISTANCES_SIZE

	if len(sys.argv) != 2:
		print ("usage: python2 tspOptSwap.py <inputFile.txt>")
		sys.exit(1)

	# Get input file from which to read in data
	inputFilename = sys.argv[1]

	# Seeding for calculating random routes
	random.seed()

	# Get the data from the input text file
	# cities is a dictionary with the key being city ID,
	# values being a list containing [city X coord, city Y coord]
	cities = loadData(inputFilename)
	numCities = len(cities)

	# Run the algorithm
	print ("Calculating shortest route")
	startTime = time.time()
	bestDistance, bestRoute = calculateRoute(cities, numCities)
	endTime = time.time() - startTime
	print ("Best distance", bestDistance)
	print ("Time Taken: ", endTime)

	# Dump the results to the output file
	outputResults(inputFilename + '.tour', bestRoute, bestDistance)

# Rip the data from the input file and store in in a dictionary
def loadData(inFile):
	try:
		cities = dict()
		with open(inFile, 'U') as f:
			for line in f:
				# Input file is formatted as:
				# [city identifier](int) [city x-coord](int) [city y-coord](int)
				# Parse these into Python list
				data = [int(n) for n in line.split()]
				if data:
					# Mapping the city identifier in the dictionary
					# Key = city ID; Value = List of coordinates
					cities[data[0]] = [data[1], data[2]]
		return cities
	except Exception:
		print ("Error reading input file")
		sys.exit(1)

# Output algorithm results to the file
def outputResults(filename, route, distance):
	with open(filename, 'w') as f:
		# Write total distance
		f.write(str(distance))
		f.write("\n")

		# Write city ID's in order visited
		for i in route:
			f.write(str(i) + "\n")

# Given two cities, get the value ((city1_x)^2 - (city2_x)^2) + ((city1_y)^2 - (city2_y)^2)
# Look it up in the dictionary, or just calculate it then store it in
def calculateSqrDistance(cities, city1, city2):
	# Check if result has been cached already (peformance)
	if ((city1, city2)) in STORED_SQR_DISTANCES:
		return STORED_SQR_DISTANCES[(city1, city2)]
	elif ((city2, city1)) in STORED_SQR_DISTANCES:
		return STORED_SQR_DISTANCES[(city2, city1)]

	# If we don't have it in the dictionary, compute it
	# Hashing into cities gives us a list [city_X_coord, city_Y_coord]
	xDist = abs(cities[city2][0] - cities[city1][0])
	yDist = abs(cities[city1][1] - cities[city2][1])

	result = math.pow(xDist, 2) + math.pow(yDist, 2)
	# Store result in table, checking if it gets full
	if calculateSqrDistance.tableSize >= STORED_SQR_DISTANCES_SIZE:
		STORED_SQR_DISTANCES.popitem()
		calculateSqrDistance.tableSize -= 1

	STORED_SQR_DISTANCES[(city1, city2)] = result
	calculateSqrDistance.tableSize += 1

	return result
calculateSqrDistance.tableSize = 0

# Apply a square root to returned value from calculateSqrDistances to get actual distance
def calculateDistance(cities, city1, city2):
	result = math.sqrt(calculateSqrDistance(cities, city1, city2))
	result = int(round(result))

	return result

# Given a route, calculate it's distance
# Route is passed in as a sequential list of cities
def calculateRouteDistance(cities, route):
	# Origin city
	origin = route[0]

	# Create the actual ordering of routes from route list
	# e.g. city1 -> city2, city2 -> city3, etc
	routeCities = [(prevCity, city) for prevCity, city in zip(route, route[1:])]

	# Add the trip back to destination
	routeCities.append((route[-1], origin))

	# Calculate total distance sum
	total = int(sum([calculateDistance(cities, city1, city2) for (city1, city2) in routeCities]))

	return total

# Shuffle the city ID's randomly and return the randomly generated list
def getRandomRoute(cities):
	randomRoute = list(cities.keys())
	random.shuffle(randomRoute)

	return randomRoute

# Generate routes, both random & straight, and then determine which is better
# We use this as a starting point and then see if it can be improved
def determineStartingRoute(cities):
	randomRoute = getRandomRoute(cities)
	randomRouteDistance = calculateRouteDistance(cities, randomRoute)

	straightRoute = list(cities.keys())
	straightRouteDistance = calculateRouteDistance(cities, straightRoute)

	bestRoute = list()
	bestDistance = 0

	# Find the shortest route and return it
	if straightRouteDistance < randomRouteDistance:
		bestRoute = straightRoute
		bestDistance = straightRouteDistance
	else:
		bestRoute = randomRoute
		bestDistance = randomRouteDistance

	return (bestRoute, bestDistance)

def calculateRoute(cities, numCities):
	global MAX_SAMPLE_SIZE

	# Determine the best starting route
	bestRoute, bestDistance = determineStartingRoute(cities)

	print ("Preliminary best result:", bestDistance)

	# Everything below this point is trying to improve upon our route
	# Assume at first that we can find an improvement to the route
	NEXT_ITER = False
	IMPROVEMENT_AVAILABLE = True

	while IMPROVEMENT_AVAILABLE:

		prevResult = bestDistance
		for i in range(numCities-1):
			# Set the sample size of the cities to be selected for random swapping
			# We are swapping routes between cities in this sample and checking to see if that improves shortest distance
			sampleSize = (MAX_SAMPLE_SIZE < (numCities - (i+1))) and MAX_SAMPLE_SIZE or (numCities - (i+1))

			# Returns a list of size sampleSize of integers chosen from i+1...numCities
			# Used for random sampling without replacement
			for k in random.sample(range(i+1, numCities), sampleSize):
				# Pick random city in that range
				j = random.randint(i, k)

				# Perform a two or three opt swap randomly and see if that makes a better route
				if (j == i) or (j == k) or (j % 2 == 0):
					newRoute = twoOptSwap(bestRoute, i, k)
				else:
					newRoute = threeOptSwap(bestRoute, i, j, k)

				newDistance = calculateRouteDistance(cities, newRoute)
				
				# The route has been made shorter (impoved) 
				if newDistance < bestDistance:
					bestRoute = newRoute
					bestDistance = newDistance
					print ("Result after swapping:", bestDistance)

					# We have improved the route, compare it against a random one
					NEXT_ITER = True
					break
				# Otherwise, keep trying to find a better one
				else:
					NEXT_ITER = False
			# Go on to the next i, otherwise, try a random route and compare
			if NEXT_ITER:
				break

		# Try to get a better route randomly
		randomRoute = getRandomRoute(cities)
		randomRouteDistance = calculateRouteDistance(cities, randomRoute)
		if randomRouteDistance < bestDistance:
			bestRoute = randomRoute
			bestDistance = randomRouteDistance

		# Improved it as much as possible
		if bestDistance == prevResult:
			IMPROVEMENT_AVAILABLE = False

	# Calculate the distance and return it
	bestDistance = calculateRouteDistance(cities, bestRoute)

	return (bestDistance, bestRoute)

# https://en.wikipedia.org/wiki/2-opt
# Idea is to take a route that crosses over itself and reorder it so it does not
def twoOptSwap(route, i, k):
	# [::-1] reverses a list
	return list(route[0:i-1]) + list(route[i-1:k][::-1]) + list(route[k:])

# https://en.wikipedia.org/wiki/3-opt
def threeOptSwap(route, i, j, k):
	# [::-1] reverses a list
	return list(route[0:i-1]) + list(route[j-1:k-1]) + list(route[i-1:j-1][::-1]) + list(route[k-1:])

# Script point of entry
if __name__ == "__main__":
	main()
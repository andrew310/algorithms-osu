import sys
import slow
import greedyFaster
import time
filename = sys.argv[-1]
cities = []
cityCount = 0
print 'Argument List:', str(sys.argv)


try:
    with open(filename) as f:
        for line in f:
            cities.append([int(s) for s in line.split() if s.isdigit()])
            cityCount += 1
except IOError as e:
    print 'Error in opening file '+ filename
    sys.exit(-1)



# Output algorithm results to the file
def outputResults(filename, route, distance):
	with open(filename, 'w') as f:
		# Write total distance
		f.write(str(distance))
		f.write("\n")

		# Write city ID's in order visited
		for i in route:
			f.write(str(i[0]) + "\n")

startTime = time.time()
if cityCount > 500:
    tour, tourLength = greedyFaster.greedyFasterTSP(cities)
    outputResults(filename + ".TOUR", tour, tourLength)
else:
    tour, tourLength = slow.slowTSP(cities)
    outputResults(filename + ".TOUR", tour, tourLength)
endTime = time.time() - startTime
print ("Time Taken: ", endTime)




import sys
import greedy
import time
filename = sys.argv[-1]
cities = []
print 'Argument List:', str(sys.argv)


try:
    with open(filename) as f:
        for line in f:
            cities.append([int(s) for s in line.split() if s.isdigit()])
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
tour, tourLength = greedy.greedyTSP(cities)
endTime = time.time() - startTime
print ("Time Taken: ", endTime)
#heldKarp.heldKarp(cities)
outputResults(filename + ".TOUR", tour, tourLength)


import math

def cityDistance(c1, c2):
	# each input is an array with city, xcoord and ycoord in the 0, 1, 2 spots
	d = int(round(math.sqrt( (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2 )))
	return d


def greedyFasterTSP(cities):
    visited = list()
    mustVisit = cities

    current = mustVisit[0]

    visited.append(current)
    mustVisit.remove(current)

    tourLength = 0

    while(len(mustVisit) > 0):
        shortestPath = float('inf') # set to infinity
        #just looping once, only comparing distances to one city
        for i in range(0, len(mustVisit)):
            distance = cityDistance(current, mustVisit[i])
            if distance < shortestPath:
                shortestPath = distance
                nearestCity = mustVisit[i]
        #update tour length
        tourLength += shortestPath
        #add nearest city to the tour
        visited.append(nearestCity)
        mustVisit.remove(nearestCity)
        current = nearestCity

    lastDistance = cityDistance(visited[0], visited[len(visited)-1])

    tourLength += lastDistance

    print tourLength
    print len(visited)
    for city in visited:
        print city[0]


    return (visited, tourLength)





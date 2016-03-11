import math

def cityDistance(c1, c2):
	# each input is an array with city, xcoord and ycoord in the 0, 1, 2 spots
	d = int(round(math.sqrt( (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2 )))
	return d


def slowTSP(cities):
    #empty array to hold the tour
    visited = list()
    mustVisit = cities
    #city to start with
    current = mustVisit[0]
    #set up first city, can't start loop unless there is something in this array
    visited.append(current)
    mustVisit.remove(current)

    tourLength = 0

    #start comparisons
    while(len(mustVisit) > 0):
        shortestPath = float('inf') # set to infinity
        #compare each city in mustVisit to each city in visited
        #we are looping the list times itself to find the nearest city
        for i in range(0, len(visited)):
            for j in range(0, len(mustVisit)):
                distance = cityDistance(visited[i], mustVisit[j])
                if distance < shortestPath:
                    shortestPath = distance
                    #save this city to add to tlist
                    nearestCity = mustVisit[j]
        tourLength += shortestPath
        #add the city we found to the tour
        visited.append(nearestCity)
        mustVisit.remove(nearestCity)

    #add the distanve from the last city to the first city
    lastDistance = cityDistance(visited[0], visited[len(visited)-1])

    tourLength += lastDistance

    print tourLength
    print len(visited)
    for city in visited:
        print city[0]

    return (visited, tourLength)





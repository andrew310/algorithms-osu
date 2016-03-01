import math

def cityDistance(c1, c2):
	# each node is an array [x,y]
	d = int(round(math.sqrt( (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2 )))
	return d


def greedyTSP(cities):
    visited = list()
    mustVisit = cities

    current = mustVisit[0]

    visited.append(current)
    mustVisit.remove(current)

    tourLength = 0

    while(len(mustVisit) > 0):
        shortestPath = float('inf') # set to infinity
        for i in range(0, len(visited)):
            for j in range(0, len(mustVisit)):
                distance = cityDistance(visited[i], mustVisit[j])
                if distance < shortestPath:
                    shortestPath = distance
                    nearestCity = mustVisit[j]
        tourLength += shortestPath
        visited.append(nearestCity)
        mustVisit.remove(nearestCity)


    print tourLength
    print len(visited)
    for city in visited:
        print city[0]
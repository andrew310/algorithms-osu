import math

def cityDistance(c1, c2):
	# each input is an array with city, xcoord and ycoord in the 0, 1, 2 spots
	d = int(round(math.sqrt( (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2 )))
	return d

#for use with the 2-opt part
def totalDist(path):
    finalDistance = 0
    for i in range(1,len(path)):
        finalDistance += cityDistance(cities[path[i-1]], cities[path[i]])
    finalDistance += cityDistance(cities[path[0]], cities[path[len(path) - 1]])
    return finalDistance

def swapPath(path, c1, c2):
    np = []

    for x in range(0, c1):
        np.append(path[x])
    y = c2
    while c2 > c1 - 1:
        cp.append(path[c2])
        c2 = c2 - 1
    for i in range(y + 1, len(path)):
        np.append(path[i])
    return np


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

    lastDistance = cityDistance(visited[0], visited[len(visited)-1])

    tourLength += lastDistance

    #### 2-OPT #########
    swap = True
    while swap:
        swap = False
        dist = tourLength
        for i in range(i+1, len(visited)-1):
            for j in range(i + 1, len(visited)):
                optPath = swapPath(visited, i, j)
                optLength = totalDist(optPath)

                if optLength < tourLength:
                    del visited[:]
                    visited[:] = []
                    visited = optPath
                    swap = True

    print tourLength
    print len(visited)
    for city in visited:
        print city[0]


    return visited, tourLength





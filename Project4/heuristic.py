

def cityDistance(c1, c2):
	# each node is an array [x,y]
	d = int(round(math.sqrt( (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2 )))
	return d


def tsp(cities):

    mustVisit = cities

    while mustVisit:
        nearest =

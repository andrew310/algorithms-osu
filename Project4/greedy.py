
def greedyTSP(cities):
    visited = list()
    mustVisit = cities

    current = mustVisit[0]

    visited.append(current)
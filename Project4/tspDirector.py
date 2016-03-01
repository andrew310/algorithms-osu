import sys

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

print cities
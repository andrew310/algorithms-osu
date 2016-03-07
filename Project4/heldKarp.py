
import collections
import functools
import math


# NOTE: this is from https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
class memoized(object):
   '''Decorator. Caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned
   (not reevaluated).
   '''
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      if not isinstance(args, collections.Hashable):
         # uncacheable. a list, for instance.
         # better to not cache than blow up.
         return self.func(*args)
      if args in self.cache:
         return self.cache[args]
      else:
         value = self.func(*args)
         self.cache[args] = value
         return value
   def __repr__(self):
      '''Return the function's docstring.'''
      return self.func.__doc__
   def __get__(self, obj, objtype):
      '''Support instance methods.'''
      return functools.partial(self.__call__, obj)

def cityDistance(c1, c2):
	# each input is an array with city, xcoord and ycoord in the 0, 1, 2 spots
	d = int(round(math.sqrt( (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2 )))
	return d

def heldKarp(c):
    cities = c

    @memoized
    def getMin(subset, node):
        if len(subset) == 1:
            return cityDistance(cities[0], cities[node]), [0]

        elif len(subset) > 1:
            newSet = set(subset.copy())
            newSet.remove(node)
            minLength = float('inf') # set to infinity
            for x in newSet:
                result = getMin(frozenset(newSet), x)
                newMin = result[0] + cityDistance(cities[x], cities[node])
                if newMin < minLength:
                    minLength = newMin
                    path = [x] + result[1]
            return minLength, path


    subCities = set(range(1, len(cities)))
    shortestPath = float('inf') #set to infinity
    minLength = float('inf') # set to infinity
    for node in subCities:
        x = getMin(frozenset(subCities), node)
        newMin = x[0] + cityDistance(cities[node], cities[0])
        if newMin < minLength:
            minLength = newMin
            path = [0, x] + x[1]
    sol = path
    print minLength
    print sol
    return minLength, sol


#Lattice paths
#How many such routes are there through a 20×20 grid?
#runtime - 0.00000002s
from math import factorial

#this method works only if gridsize is even
def route_counter(gridsize):
    m = gridsize
    routes = factorial(2*m)/(factorial(m)**2)
    return int(routes)

print(route_counter(20))

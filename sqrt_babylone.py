# mise en place de l algorythme de babylone
# algorithme iteratif
#http://www.xm1math.net/algobox/exemples/babylone.html

import math

def babylone(a):
	x = 1
	y = a
	while (abs(y - x) > 0.00000001):
		x = (x + y) / 2
		y = a / x
		if (x < y):
			print (str(x) + "< racine <" + str(y))
		else:
			print (str(y) + "< racine <" + str(x))

def sqrt(nb):
	nb = float(nb)
	x, y = 1, nb
	while (abs(y - x) > 0.00000000001):
		x, y = (x + y) / 2, nb / x
	return (x)

babylone(4.0)
print ('')
babylone(18.0)
print ('')
babylone(5.0)
print ('')
babylone (10000000)

print (math.sqrt(4.0))
print (math.sqrt(18.0))
print (math.sqrt(5.0))
print (math.sqrt(10000000))

print ('')

print (sqrt(4))
print (sqrt(18))
print (sqrt(5.0))
print (sqrt(10000000.0))
